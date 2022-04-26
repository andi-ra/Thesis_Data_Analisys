# Simulation 1
# ------------

# import simpy
# from SimComponents import PacketGenerator, PacketSink, SwitchPort, PortMonitor
# import random
import functools
import random

import numpy as np
import simpy
from matplotlib import pyplot as plt


class Packet(object):
    """ A very simple class that represents a packet.
        This packet will run through a queue at a switch output port.
        We use a float to represent the size of the packet in bytes so that
        we can compare to ideal M/M/1 queues.

        Parameters
        ----------
        time : float
            the time the packet arrives at the output queue.
        size : float
            the size of the packet in bytes
        id : int
            an identifier for the packet
        src, dst : int
            identifiers for source and destination
        flow_id : int
            small integer that can be used to identify a flow
    """

    def __init__(self, time, size, id, src="a", dst="z", flow_id=0):
        self.time = time
        self.size = size
        self.id = id
        self.src = src
        self.dst = dst
        self.flow_id = flow_id

    def __repr__(self):
        return "id: {}, src: {}, time: {}, size: {}". \
            format(self.id, self.src, self.time, self.size)


class PacketGenerator(object):
    """ Generates packets with given inter-arrival time distribution.
        Set the "out" member variable to the entity to receive the packet.

        Parameters
        ----------
        env : simpy.Environment
            the simulation environment
        adist : function
            a no parameter function that returns the successive inter-arrival times of the packets
        sdist : function
            a no parameter function that returns the successive sizes of the packets
        initial_delay : number
            Starts generation after an initial delay. Default = 0
        finish : number
            Stops generation at the finish time. Default is infinite


    """

    def __init__(self, env, id, adist, sdist, initial_delay=0, finish=float("inf"), flow_id=0):
        self.id = id
        self.env = env
        self.adist = adist
        self.sdist = sdist
        self.initial_delay = initial_delay
        self.finish = finish
        self.out = None
        self.packets_sent = 0
        self.action = env.process(self.run())  # starts the run() method as a SimPy process
        self.flow_id = flow_id

    def run(self):
        """The generator function used in simulations.
        """
        yield self.env.timeout(self.initial_delay)
        while self.env.now < self.finish:
            # wait for next transmission
            yield self.env.timeout(self.adist())
            self.packets_sent += 1
            p = Packet(self.env.now, self.sdist(), self.packets_sent, src=self.id, flow_id=self.flow_id)
            self.out.put(p)


class PacketSink(object):
    """ Receives packets and collects delay information into the
        waits list. You can then use this list to look at delay statistics.

        Parameters
        ----------
        env : simpy.Environment
            the simulation environment
        debug : boolean
            if true then the contents of each packet will be printed as it is received.
        rec_arrivals : boolean
            if true then arrivals will be recorded
        absolute_arrivals : boolean
            if true absolute arrival times will be recorded, otherwise the time between consecutive arrivals
            is recorded.
        rec_waits : boolean
            if true waiting time experienced by each packet is recorded
        selector: a function that takes a packet and returns a boolean
            used for selective statistics. Default none.

    """

    def __init__(self, env, rec_arrivals=False, absolute_arrivals=False, rec_waits=True, debug=False, selector=None):
        self.store = simpy.Store(env)
        self.env = env
        self.rec_waits = rec_waits
        self.rec_arrivals = rec_arrivals
        self.absolute_arrivals = absolute_arrivals
        self.waits = []
        self.arrivals = []
        self.debug = debug
        self.packets_rec = 0
        self.bytes_rec = 0
        self.selector = selector
        self.last_arrival = 0.0

    def put(self, pkt):
        if not self.selector or self.selector(pkt):
            now = self.env.now
            if self.rec_waits:
                self.waits.append(self.env.now - pkt.time)
            if self.rec_arrivals:
                if self.absolute_arrivals:
                    self.arrivals.append(now)
                else:
                    self.arrivals.append(now - self.last_arrival)
                self.last_arrival = now
            self.packets_rec += 1
            self.bytes_rec += pkt.size
            if self.debug:
                print(pkt)


class SwitchPort(object):
    """ Models a switch output port with a given rate and buffer size limit in bytes.
        Set the "out" member variable to the entity to receive the packet.

        Parameters
        ----------
        env : simpy.Environment
            the simulation environment
        rate : float
            the bit rate of the port
        qlimit : integer (or None)
            a buffer size limit in bytes or packets for the queue (including items
            in service).
        limit_bytes : If true, the queue limit will be based on bytes if false the
            queue limit will be based on packets.

    """

    def __init__(self, env, rate, qlimit=None, limit_bytes=True, debug=False):
        self.store = simpy.Store(env)
        self.rate = rate
        self.env = env
        self.out = None
        self.packets_rec = 0
        self.packets_drop = 0
        self.qlimit = qlimit
        self.limit_bytes = limit_bytes
        self.byte_size = 0  # Current size of the queue in bytes
        self.debug = debug
        self.busy = 0  # Used to track if a packet is currently being sent
        self.action = env.process(self.run())  # starts the run() method as a SimPy process
        self.droppacket = 0
        self.packet = None

    def run(self):
        while True:
            msg = (yield self.store.get())
            if (self.droppacket == 0):
                self.busy = 1
            self.byte_size -= msg.size
            yield self.env.timeout(msg.size * 8.0 / self.rate)
            # ADDITION - VIGNESH
            self.packet = msg

            self.out.put(msg)
            self.busy = 0
            # self.droppacket = 0
            if self.debug:
                print(msg)

    def put(self, pkt):
        global cwndsrc1
        global cwndsrc2
        global thresh1
        global thresh2
        self.packets_rec += 1
        tmp_byte_count = self.byte_size + pkt.size

        if self.qlimit is None:
            self.byte_size = tmp_byte_count
            return self.store.put(pkt)
        if self.limit_bytes and tmp_byte_count >= self.qlimit:
            self.packets_drop += 1
            return

        elif not self.limit_bytes and len(self.store.items) >= self.qlimit - 1:
            self.packets_drop += 1

            # CHANGED - VIGNESH

            # Find out whose packet has been dropped
            source = self.packet.src
            # print("Packet dropped: " + source)
            # Backoff CWND 	and thresh for this packet's source
            if source == "S1":
                cwndsrc1 = 1
                thresh1 = thresh1 / 2
            elif source == "S2":
                cwndsrc2 = 1
                thresh2 = thresh2 / 2

        elif self.droppacket == 1:
            self.packets_drop += 1
            # self.droppacket = 0



        else:
            self.byte_size = tmp_byte_count
            return self.store.put(pkt)


class PortMonitor(object):
    """ A monitor for an SwitchPort. Looks at the number of items in the SwitchPort
        in service + in the queue and records that info in the sizes[] list. The
        monitor looks at the port at time intervals given by the distribution dist.

        Parameters
        ----------
        env : simpy.Environment
            the simulation environment
        port : SwitchPort
            the switch port object to be monitored.
        dist : function
            a no parameter function that returns the successive inter-arrival times of the
            packets
    """

    def __init__(self, env, port, dist, count_bytes=False):
        self.port = port
        self.env = env
        self.dist = dist
        self.count_bytes = count_bytes
        self.sizes = []
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(self.dist())
            if self.count_bytes:
                total = self.port.byte_size
            else:
                total = len(self.port.store.items) + self.port.busy
            self.port.droppacket = 0
            self.sizes.append(total)


def constArrival():  # Constant arrival distribution for generator 1
    global cwndsrc1
    # print("TEST CWND 1: " + str(cwndsrc1))
    if cwndsrc1 < thresh1:
        cwndsrc1 = cwndsrc1 * 2
        if (cwndsrc1 > thresh1):
            cwndsrc1 = thresh1

    interval = 1 / cwndsrc1
    return interval


def constArrival2():
    global cwndsrc2
    # print("TEST CWND 2: " + str(cwndsrc2))
    if cwndsrc2 < thresh2:
        cwndsrc2 = cwndsrc2 * 2
        if (cwndsrc2 > thresh2):
            cwndsrc2 = thresh2

    interval = 1 / cwndsrc2
    return interval


def distSize():
    return 1


def distSize2():
    global pm
    global switch_port
    global qavg
    global avgqueue
    global bufSize
    global cwndsrc1
    global cwndsrc2

    global thresh1
    global thresh2
    # print("BUFFER SIZE")
    # print(pm.sizes)
    if (len(pm.sizes) != 0):
        # If greater than max threshold, always drop packet.
        # Queue length calculation method - EWMA.
        qavg = (1 - w) * qavg + w * pm.sizes[-1]
        avgqueue.append(qavg)
        # qavg = (1 - w)*qavg + w*len(switch_port.store.items)
        if (qavg > Qmax):
            # Then drop the packet
            switch_port.droppacket = 1

            # Find out whose packet has been dropped
            source = switch_port.packet.src
            # Backoff CWND for this packet's source
            if source == "S1":
                thresh1 = cwndsrc1 / 2
                cwndsrc1 = 1
            elif source == "S2":
                thresh2 = cwndsrc2 / 2
                cwndsrc2 = 1
        # print("Packet dropped: " + source)
        # If greater than min threshold, drop with probability p = queuesize/buffersize
        elif (qavg > Qmin):
            p = qavg / (bufSize * 10)
            if random.randint(0, 100) < (p * 100):
                switch_port.droppacket = 1
                # Find out whose packet has been dropped
                source = switch_port.packet.src
                # print("Packet dropped: " + source)
                # Backoff CWND 	and thresh for this packet's source
                if source == "S1":
                    cwndsrc1 = 1
                    thresh1 = thresh1 / 2
                elif source == "S2":
                    cwndsrc2 = 1
                    thresh2 = thresh2 / 2
    return 0.25





if __name__ == '__main__':
    # RED Parameters

    Qmax = 1900
    Qmin = 400
    p = 0
    qavg = 10

    avgqueue = []
    # Other
    bufSize = 2000
    linerate = 100.0
    # Weight calculation
    # w = 0.05
    # L + 1 + ((1 - w)^(L+1) - 1)/w < Qmin


    # Congestion Windows
    cwndsrc1 = 10
    cwndsrc2 = 10
    thresh1 = 9
    thresh2 = 15
    # Set up arrival and packet size distributions
    # Using Python functools to create callable functions for random variates with fixed parameters.
    # each call to these will produce a new random value.
    adist = functools.partial(random.expovariate, 0.005)
    sdist = functools.partial(random.expovariate, 0.0001)  # mean size 100 bytes
    samp_dist = functools.partial(random.expovariate, 2.5)
    port_rate = 1000.0

    env = simpy.Environment()  # Create the SimPy environment
    # Create the packet generators and sink
    ps = PacketSink(env, debug=False, rec_arrivals=True)
    pg = PacketGenerator(env, "Greg", adist, sdist)
    switch_port = SwitchPort(env, port_rate, qlimit=10000)
    # Using a PortMonitor to track queue sizes over time
    pm = PortMonitor(env, switch_port, samp_dist)
    # Wire packet generators, switch ports, and sinks together
    pg.out = switch_port
    switch_port.out = ps
    # Run it
    env.run(until=8000)
    print("Last 10 waits: " + ", ".join(["{:.3f}".format(x) for x in ps.waits[-10:]]))
    print("Last 10 queue sizes: {}".format(pm.sizes[-100:]))
    print("Last 10 sink arrival times: " + ", ".join(["{:.3f}".format(x) for x in ps.arrivals[-10:]]))
    print("average wait = {:.3f}".format(sum(ps.waits) / len(ps.waits)))
    print(
        "received: {}, dropped {}, sent {}".format(switch_port.packets_rec, switch_port.packets_drop, pg.packets_sent))
    print("loss rate: {}".format(float(switch_port.packets_drop) / switch_port.packets_rec))
    print("average system occupancy: {:.3f}".format(float(sum(pm.sizes)) / len(pm.sizes)))

    fig, axis = plt.subplots()
    axis.hist(ps.waits, bins=100)
    axis.set_title("Histogram for waiting times")
    axis.set_xlabel("time")
    axis.set_ylabel("normalized frequency of occurrence")
    fig.savefig("WaitHistogram.png")
    plt.show()
    fig, axis = plt.subplots()
    axis.hist(ps.waits, bins=100)
    axis.set_title("Histogram for System Occupation times")
    axis.set_xlabel("number")
    axis.set_ylabel("normalized frequency of occurrence")
    fig.savefig("QueueHistogram.png")
    plt.show()
    fig, axis = plt.subplots()
    axis.hist(ps.arrivals, bins=100)
    axis.set_title("Histogram for Sink Interarrival times")
    axis.set_xlabel("time")
    axis.set_ylabel("normalized frequency of occurrence")
    # fig.savefig("ArrivalHistogram.png")
    plt.show()
