---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# SDN e controller

Con SDN ci riferiamo al nuovo approccio adottato negli ultimi anni dal networking. Al cuore di questa nuova modalità vi 
è il paradigma match-action. Il paradigma match-action rappresenta un grosso cambio di mentalità e soprattutto di 
tecnologia, in quanto la rete fa molto più affidamento al software. Fino alla prima metà del decennio scorso (e tuttora
in molti casi "enterprise") la rete di telecomunicazioni era suddivisa in parte di *accesso* e parte di *trasporto*. La 
porzione di accesso doveva (definita in grgo l'ultimo miglio) connetteva l'utente finale con i dispositivi del centro 
della rete. Questa porzione periferica doveva essere economica per permettere una capillare penetrazione nel territorio,
poiché i clienti finali sono distribuiti sul territorio. La parte di trasporto è quella più vicina al concetto classico
di rete. Un sistema di apparati che cooperano al fine di connettere un punto A ad un punto B attraverso i loro flussi
informativi. In una concezione di questo tipo dell'infrastruttura totale di telecomunicazione, il software risiedeva in
due punti molto diversi fra loro per la funzione che avevano. Questi due punti sono:
1. nel dispositivo router che calcola le rotte fra A e B e di queste ne sceglie la migliore
2. nel sistema di gestione e raccolta allarmi centrale dell'operatore (per la fatturazione, il troubleshooting...)

```{margin} NOC
Network operation center, è il luogo (o i luoghi) da cui l'operatore può elaborare gli alert e problemi della rete da 
remoto e fare troubleshooting per risolvere problemi tecnici e garantire un'operazione fluida della rete
```

Il software più evoluto e simile ad un sistema di gestione, era quello che risiedeva nei NOC dell'operatore. Per quanto 
riguarda il primo putno invece, cioè la ricerca delle rotte ammissibili e la scelta della migliore fra queste, gli 
algoritmi rimanevano ancora di tipo distribuito oppure asincrono e dstribuito. Con l'avvento delle tecnologie cloud e 
con l'esplosione della domanda e della varietà di requisiti richiesti, le reti con funzioni di routing classico non erano 
più sufficienti. Questo ha portato a postulare una rete molto più fluida in totale controtendenza con l'ossificazione di 
internet.
```{note}
Con ossificazione di Internet si intende la perdita di flessibilità della rete Internet. Informalmente possiamo dire che 
quella che era partita come una rete agile e resistente, è diventata una rete in cui i protocolli sono "scritti sulla pietra".
A testimonianza di ciò, basti pensare alle difficoltà nel deployment della rete multicast WAN, oppure gli scogli che sta 
incontrando il rollout di IPv6. Per un approfondimento sulla rigidità della rete Internet consultare {cite:p}`L23`.
```
Per risolvere questo problema, si è accantonata la vecchia gestione della rete con i suoi algoritmi distribuiti, a favore
di una concentrazione delle capacità elaborative verso un unico dispositivo, chiamato controller. Questa migrazione delle
capacità elaborative, che informalmente possiamo definire come "migrazione dell'intelligence di rete", ha concentrato la
funzione di elaborazione delle rotte e la scelta della migliore, dai vari dispositivi router ad un unico dispositivo 
controllore. Questo ha richiesto una rivisitazione completa di come uno switch eseguiva il primo dei due punti elencati.
Per prima cosa, ha richiesto che il cotroller si prendesse carico di come raccogliere le informazioni topologiche di rete.
Seconda cosa, il controller si prende carico di ottimizzare qualunque funzionale di costo definito sul grafo ottenuto dal
passso precedente. Terza cosa, ha richiesto un metodo per la disseminazione dei risultati edl passo precedente ad ogni 
singolo elemento di rete. Questo approccio, ha richiesto una completa ristrutturazione, non tanto degli algoritmi, quanto
della raccolta delle informazioni di rete e della disseminazione dei segnali inter-router. Quest'ultimo aspetto è stato
possibile ottenerlo con le nuove tecniche software applicate al networking. 
 
Questo approccio molto più orientato al software, ha trovato enormi applicazioni e benefici nelle reti cloud e nel datacenter
networking. Nelle architetture datacenter abbiamo quantità massive di dispositivi da interconnettere. La sfida delle reti cloud e 
del datacenter networking non nasce solo dal fatto che vi sia una quantità massiva di dispositivi, ma la sfida principale
è rappresentata dal fatto che questi dispositivi devono supportare i servizi più disparati una volta fatto il rollout.
Ragioniamo con un esempio: come posso creare una rete che un giorno sia ottimizzata per applicazioni di computing e il 
giorno successivo sia ottimizzato per appliazioni che richiedono un I/O elevato. È impensabile pensare a una rete nuova 
per ogni singola applicazione.  Dunque come risolviamo questo problema? Risolviamo con una rete molto più plastica ed 
adattabile. Casi di successo come le reti datacenter sono una testimonianza dell'utilità di questo approccio. 
```{margin} OpenStack
OpenStack è una piattaforma di orchestrazione e management in tecnologia virtuale. Si affida ad una virtualizzazione di
tutte le risorse, usando un hypervisor esterno, esponendo le risorse suddivise in base al loro scopo e configurazione
```
Come riportato dalla Openstack Foundation nel
loro whitepaper  {cite:p}`OSTCK` l'operatore cinese China Mobile ha fatto il rollout della sua rete 5G con ottimi risultati. 
Il caso di successo di China Mobile è uno dei tanti che testimonia la potenza delle tencologie SDN nelle reti di nuova
generazione. 

Qui stiamo parlando di tecnologie per ambienti mobile IoT, dunque oltre alle difficoltà insite nell'ambiente IoT, abbiamo 
l'inaffidabilità dovuta a oggetti mobili in ambienti potenzialmente ostili alla radiopropagazione. 
* Che relazione hanno le tecniche SDN nei dataceter con il mondo IoT?
* Quali sono gli strumenti che posso utilizzare?

La prima domanda trova risposta nell'osservazione dei modelli matematici che sottendono entrambi i mondi. Possiamo 
dimostrare che dal punto di vista del controllo, una WSN non è semplicemente una enorme rete di sensori  da controllare.
Una rete WSN, specialmente se osservata dal punto di vista dei processi di genesi e network forming, condivide molto con
il mondo del controllo del cloud datacenter networking. Un risultato sorprendente lo troviamo nell'articolo 
{cite:p}`CHRISTOPHER2021101840` in cui viene descritto l'algortimo JSDR ossia Jellyfish Sensor Dynamic Routing. 
Questo algoritmo prende a prestito molto di quello era l'algoritmo originale Jellyfish per datacenter networking.   
Andando più nel dettaglio, questo algoritmo JSDR proviene in realtà da un altro algoritmo di routing per datacenter che 
sfrutta le proprietà dei grafi casuali e le teorie sul network forming. Nell'articolo {cite:p}`10.5555/2228298.2228322`
gli autori dimostrano come Jellyfish, un algoritmo di routing basato su un processo di network forming casuale, porti ad 
grafo di Erdos-Renyi. Questo grafo di Erdos-Renyi è la rappresentazione topologica di quello che succede fra gli switch 
che vengono interconnessi fra loro, grazie ad un arco, con una certa probabilità *p*. Si può dimostare come la distribuzione di
probabilità dell'esistenza di un certo arco fra lo switch $s_i$ e lo switch $s_j$ sia una poisson con parametro $\lambda=p$.
La cosa più sorprendente sono le prestazioni che l'algoritmo Jellyfish riesce ad ottenere. Se poniamo a confronto il throughput
medio di un'organizzazione topologica della rete secondo un fat-tree e una Jellyfish (cioè un grafo casuale), vediamo che 
il grafo di switch casuale di Erdos-Renyi ha un throuput medio maggiore. Dunque con un'organizzazione totalmente casuale 
della rete riesco, in media, ad ottenere prestazioni migliori. Per approfondimenti consultare {cite:p}`CHRISTOPHER2021101840`

:::{figure-md} markdown-fig
<img src="https://reproducingnetworkresearch.files.wordpress.com/2012/06/fattree.png?w=180&h=180" alt="fishy" class="bg-primary mb-1" width="400px">

Topologia Fat-Tree nel routing datacenter
:::

:::{figure-md} markdown-fig
<img src="https://reproducingnetworkresearch.files.wordpress.com/2012/06/jellyfish.png?w=180&h=180" alt="fishy" class="bg-primary mb-1" width="400px">

Topologia Jellyfish nel routing datacenter
:::

Quella che segue è soltanto un'intuizione alla base e non una dimostrazione.
Parte del successo di Jellyfish lo possiamo intuire usando la teoria dei "piccoli mondi". La teoria dei "piccoli mondi"
nasce da un esperimento fatto nel secolo scorso in cui una serie persone dovevano usare i loro contatti per iviare delle
lettere da una parte all'altra delgi Stati Uniti. In pratica, prendendo delle 
persone a caso e chiedendo loro di spedire la lettera da una parte all'altra del mondo, tutte le lettere che sono arrivate 
a destinazione, avevano in media una lunghezza di 5-6 persone intermedie. Dunque per mandare una lattera dagli US in Giappone, 
si usavano soltanto 5-6 persone in media.

```{margin} diametro di una rete
Il diametro di una rete è il più lungo dei cammini minimi all'interno della rete
```
Questo risultato soprendente lo rivediamo anche nel routing in datacenter. In pratica, nella topologia fat-tree ho un
diametro della rete maggiore rispetto al diametro della rete Jellyfish. Questo fatto, unito alla teoria dei piccoli mondi,
permette di postulare che il routing casuale, applicato in queste reti, non sia poi così naive come sembri. L'articolo 
menzionato mostra altri risultati sorprendenti.

Vedendo l'algoritmo JSDR, le sue performance e la relazione che ha con il mondo del routing in datacenter, la domanda ora 
diventa: 
* similmente al caso Jellyfish, possiamo estendere gli algoritmi odierni sfruttando i processi di network forming? 
* Se sì, otteniamo gli stessi vantaggi anche nel mondo IoT?

Partiamo dalla seconda domanda. Dando per buono, per ora, che possiamo usare i processi di network forming per ottenere 
algoritmi più performanti, come posso essere sicuro che effettivamente ho un vantaggio? Dobbiamo definire cosa per noi è
un vantaggio. Un vantaggio in termini di perfomance in una rete deve essere misurato tramite l'uso di una qualche metrica.
Le metriche più comuni che oggi vengono usate sono:

* throughput 
* latenza
* probabilità di perdita di pacchetto
* probabilià di disconnessione
* robustezza della rete

Un aspetto che sarà fondamentale nella trattazione seguente è:
    che tipo di routing si può usare?

Questa domanda è fondamentale in quanto, se usiamo il routing classico, allora otterrò le odierne WSN. Mentre invece se 
migrassi verso un approccio molto software-oriented, ottengo una SDN per sensori. Quest'ultima cosa comporta l'
installazione di un controller. 

Adesso la domanda fondamentale: 
    Che vantaggio mi porta l'aggiunta di un elemento "estraneo" al mondo IoT come il controller?

Rispondiamo a questa domanda, ed alla prima, con una serie di casi d'uso in cui è possibile ottenere ottime prestazioni
e aprire scenari impossibili da coprire con le reti attuali. Si propone una trattazione di algoritmi per i seguenti casi:
* Allocazione ottima delle risorse
* Controllo della congestione
* Aumento della robustezza della rete
  
Ognuno di questi casi verrà esaminato nel corrispondente paragrafo nel capitolo finale. Ciascuna delle sezioni sull'
analisi dei risultati illustrerà le risposte alle domande tramite emulazione nell'ambiente GNS3.

## NetApp e controller

Con la parola NetApp ci riferiamo ai moduli che implementano gli algoritmi proposti all'interno del controller. 
L'architettura di rete è costituita da più piani logici o fisici di interconnessione fra i dispositivi, come in figura:

:::{figure-md} markdown-fig
<img src="https://d3i71xaburhd42.cloudfront.net/5c61431e479245b1235b30de20aa89ebc188189c/6-Figure2-1.png" alt="fishy" class="bg-primary mb-1" width="700px">

Rappresentazione dei vari piani di connessione, cortesia di {cite:p}`OrdonezLucena2017NetworkSF`
:::

Per ottenere un'architettura come quella in figura, è necessario utilizzare un controller centrale che possa creare i 
collegamenti logici attraverso un routing intelligente fra i vari dispositivi.

Andando più nel dettaglio con l'architettura del sistema controller, possiamo che sono due i design pattern fondanti:
1. Publish-subscribe
2. Decorator

Iniziamo descrivendo il secondo design pattern. Il pattern decorator è un pattern che permettere di aggiornare le funzionalità
a runtime della mia classe. In python la questione è diversa. L'esecuzione del codice avviene in due fasi diverse:
* Import time
* Execution time
Nell'import time abbiamo che l'interprete esegue tutte le istruzioni di importazione di librerie esterne e dichiara classi,
metodi, funzioni e variabili globali. Questo viene fatto **prima** che venga eseguita qualunque istruzione di codice.

```{code-cell} ipython2
registry = []

def register(func):
    print("registering (%s)" % func)
    registry.append(func)
    return func

print("List before decoration "+str(registry))

@register    # Questa funzione viene eseguita prima dl contenuto della funzione decorata
def f1():
    print("Running f1()")
print("List after decoration"+str(registry))

f1()
```

Questo design pattern viene sfruttato per esrguire una registrazione dei metodi e delle classi nel controller. In queste
classi ho codificato il comportamento che deve avere il controller. Giusto qualche esempio:
Il seguente listato mostra un pezzo della dichiarazione di una classe OFP (OpenFlow) Hello message packet. In questa classe
si trova il comportamento che il controller deve adottare. Nella convenzione Ryu il risultato è una classe, il cui pezzo
inziziale, è come sotto:

    @_register_parser       # primo decorator che registra questa classe come parser di un pacchetto OpenFlow
    @_set_msg_type(ofproto.OFPT_HELLO)   # Secondo decorator "stacked" che dice che tipo di evento crea (OFPT_HELLO)
    class OFPHello(MsgBase):
        """
        Hello message
        When connection is started, the hello message is exchanged between a
        switch and a controller.

Per ogni tipo di messaggio OpenFlow devo seuire la procedura accennata sopra e cioè:
* Dichiarare che tipo di messaggio sto parlando
* Decorare la classe se sto descrivendo un parser, cioè una classe che descrive come comportarsi con quel pacchetto
* Decorare la classe dicendo che tipo di evento scateno alla ricezione del pacchetto in oggetto
* Dichiarare metodi e variabili locali relativi al parsing di quel pacchetto

Per quale motivo dichiarare quale evento viene scatenato alla ricezione e parsing di quel pacchetto?

Poiché ragiono con un design pattern principale che è publish-subscribe, un design pattern di tipo reattivo che reagisce 
a degli eventi esterni. Dunque ciò che faccio è usare gli eventi come input al mio sistema. A questo punto ci chiediamo:

Il mio controller riceve pacchetti o riceve eventi? 

Il controller riceve pacchetti, nessuno switch può emettere eventi... Può solo generare pacchetti secondo la specifica 
di OpenFlow desiderata. Allora cosa c'entrano gli eventi? Osserviamo la seguente figura:

:::{figure-md} markdown-fig
<img src="C:\\Users\\Andi\\Desktop\\Rebel\\Thesis_Data_Analisys\\assets\\Cattura.JPG" alt="fishy" class="bg-primary mb-1" width="800px">

Architettura del controller (immagine temporanea)
:::

Quello che è il loop centrale è la socket in ascolto. Il sottosistema a valle della socket in ascolto è tutta la parte
di controller che si occupa di:
* fare il parsing del pacchetto
* riconoscere il pacchetto ed estrarre le info rilevanti
* popolare una classe (o struct dati) che sarà la struttura dati che contiene le informazioni dell'evento
* Sfruttare i meccanismi di publish interni
* propagare l'evento ai event handler che hanno fatto subscribing a quel preciso evento
 
Quello che chiamo UoW cioè Unit of Work (nome preso da {cite:p}`percival2020architecture`) è un tipo di comportamento.
Ad esempio, come mi comporto quando ricevo un HELLO? Come mi comporto quando ricevo un PACKET_IN? E via dicendo con tutti
i pacchetti definiti dalla specifica OpenFlow. Tutti questi comportamenti che devo tenere ogni volta che ricevo un certo
pacchetto (anche solo per generare l'evento e notificare gli altri) lo codifico in questi UoW. Poiché questi UoW durante
le varie release variano leggermente, non è bene dichiarare una nuova classe per ogni release. Ciò che faccio è usare una
sorta di repository dei tipi di pacchetti e chiedere ad ogni classe di istanziare il comportamento corretto in base a:
* Versione di OpenFlow 
* Tipo di pacchetto

Oltre a codificare i comportamenti che il controller deve intraprendere quando riceve un pacchetto, con questi UoW ci
specifico anche che tipo di processing fare con le info che il controller ha a disposizione. Per esempio se voglio
specificare come un certo Switch debba processare un certo pacchetto io posso toccare la sua pipeline di processing del 
pacchetto usando dei pacchetti OpenFlow (ad esempo FlowMod) prodotti secondo le istruzioni di questo UoW. Segue un listato
di esempio:

    if ofproto.OFP_VERSION == ofproto_v1_0.OFP_VERSION:
                    rule = nx_match.ClsRule()
                    rule.set_dl_dst(addrconv.mac.text_to_bin(lldp.LLDP_MAC_NEAREST_BRIDGE))
                    rule.set_dl_type(ETH_TYPE_LLDP)
                    actions = [ofproto_parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, self.LLDP_PACKET_LEN)]
                    dp.send_flow_mod(
                        rule=rule, cookie=0, command=ofproto.OFPFC_ADD,
                        idle_timeout=0, hard_timeout=0, actions=actions,
                        priority=0xFFFF)
                        
In questo modulo del controller Ryu (il UoW) vediamo come dopo un controllo della versione creo un oggetto che mi servirà
per il matching dei vari campi del pacchetto LLDP. La variabile `actions` contiene il codice della specifica OpenFlow che 
corrisponde al comportamento che voglio che lo switch abbia. In questo caso io controller voglio che lo switch abbia una
flow rule relativa ai pacchetti LLDP. Questa flow rule, che codifica il comportamento desiderato, riusciamo ad intuirla 
vedendo la variabile "action". Dal listato si vede che lo switch dovrà inviare indietro al controller (tramite packet in) 
il pacchetto LLDP che ha fatto matching. Questo descritto ora è il comportamento previsto dalle specifiche OpenFlow per 
quanto riguarda la topology discovery. Questo descritto è soltanto un esempio di quali comportamenti posso codificare nel
switch. Ve ne sono molti altri, invito a guardare la repository del progetto per vedere come si codifica ogni singolo 
comportamento, logica e funzione di rete.

Questi moduli sono coloro che fattivamente una volta prese le info di rete, calcoleranno lo stato desiderato e 
dissemineranno le istruzioni ai vari switch per arrivare a quello stato desiderato. Vista così l'implementazione più 
naturale dei vari algoritmi è quella iterativa. Non uso ricorsione, tutti gli algoritmi sono di tipo iterativo in quanto
dimostro che esista una sequenza di passi finita che porterà il mio sistema dallo stato attuale (il punto A) ad un punto
B (lo stato desiderato) attraverso piccoli passi nello spazio dei comportamenti ammissibili.

Nell'ultimo capitolo espongo i risultati delle simulazioni ottenuti con questi UoW, invito a consultare la repository del
progetto per il codice sorgente alla base di queste simuzlazioni. 