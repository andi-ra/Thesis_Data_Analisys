"""
Example use of SimComponents to simulate a packet queue with M/M/1 characteristics.
Copyright 2014 Dr. Greg M. Bernstein
Released under the MIT license
"""
import random
import functools
import simpy
import matplotlib.pyplot as plt
from SimComponents import PacketGenerator, PacketSink, SwitchPort, PortMonitor

if __name__ == '__main__':
    # Set up arrival and packet size distributions
    # Using Python functools to create callable functions for random variates with fixed parameters.
    # each call to these will produce a new random value.
    adist = functools.partial(random.expovariate, 0.01)
    sdist = functools.partial(random.expovariate, 0.05)  # mean size 100 bytes
    samp_dist = functools.partial(random.expovariate, 0.005)
    port_rate = 1.5

    env = simpy.Environment()  # Create the SimPy environment
    # Create the packet generators and sink
    ps = PacketSink(env, debug=False, rec_arrivals=True)
    pg = PacketGenerator(env, "Greg", adist, sdist)
    switch_port = SwitchPort(env, port_rate, qlimit=100000)
    # Using a PortMonitor to track queue sizes over time
    pm = PortMonitor(env, switch_port, samp_dist)
    # Wire packet generators, switch ports, and sinks together
    pg.out = switch_port
    switch_port.out = ps
    # Run it
    env.run(until=8000000)
    print("Last 10 waits: " + ", ".join(["{:.3f}".format(x) for x in ps.waits[-10:]]))
    print("Last 10 queue sizes: {}".format(pm.sizes[-1000:]))

    fig, axis = plt.subplots()
    axis.plot(pm.sizes)
    axis.set_title("Line plot for System Occupation")
    axis.set_xlabel("time")
    axis.set_ylabel("customers in system")
    plt.show()

    print("Last 10 sink arrival times: " + ", ".join(["{:.3f}".format(x) for x in ps.arrivals[-10:]]))
    print("average wait = {:.3f}".format(sum(ps.waits) / len(ps.waits)))
    print(
        "received: {}, dropped {}, sent {}".format(switch_port.packets_rec, switch_port.packets_drop, pg.packets_sent))
    print("loss rate: {}".format(float(switch_port.packets_drop) / switch_port.packets_rec))
    print("average system occupancy: {:.3f}".format(float(sum(pm.sizes)) / len(pm.sizes)))
    fig, axis = plt.subplots()
    axis.hist(ps.waits, bins=10000, density=True)
    axis.set_title("Histogram for Sojourn times")
    axis.set_xlabel("number")
    axis.set_ylabel("normalized frequency of occurrence")
    plt.show()
    fig, axis = plt.subplots()
    axis.hist(ps.arrivals, bins=100, density=True)
    axis.set_title("Histogram for Sink Interarrival times")
    axis.set_xlabel("time")
    axis.set_ylabel("normalized frequency of occurrence")
    plt.show()
