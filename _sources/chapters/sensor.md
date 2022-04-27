# Reti di sensori

Una rete di sensori solitamente consiste in device:
* sorgenti, i sensori che campionano l'ambiente e producono informazioni utili
* terminazioni, le base station o i clusterhead
* usati dagli utenti finali

I nodi sensori vengono installati in zone geografiche d'interesse, dove grazie alle loro caratteristiche di costo 
ridotto, auto-organizzazione e intercambiabilità permettono di avere un piano di raccolta dati fungibile e capillare.
Per poter raggiungere l'obiettivo di avere una rete auto-organizzante per monitorare ambienti ho bisogno di campionare
il fenomeno d'interesse, codificarlo e trasmettere questa rappresentazione verso un nodo consumatore dell'informazione
attraverso un protocollo di routing.

Un'ipotesi che spesso viene fatta è che i nodi consumatori siano più potenti dei nodi campionatori. In figura vediamo 
uno scenario tipo di rete di sensori. È da osservare la presenza della nuvoletta che rappresenta la Wide Area Network
che metterà in comunicazione il data center di elaborazione dati e l'utente finale.
```{margin} Clustertree
Struttura a grafo aciclico in cui ogni nodo è un cluster di nodi rappresentati da un super nodo detto clusterhead
```

:::{figure-md} markdown-fig
<img src="../images/WSN_topo.jpg" alt="fishy" class="bg-primary mb-1" width="700px">

Scenario tipo organizzato come **cluster-tree**!
:::

Com'è composto il singolo device sensore? A grandi linee possiamo pensarlo come composto dai seguenti blocchi in figura:

```{margin} Precisazione sullo schema a blocchi
I blocchi tratteggiati sono opzionali 
```

:::{figure-md} markdown-fig
<img src="https://i.imgur.com/eSAKY8c.png" alt="mcu" class="bg-primary mb-1" width="700px">

Schema a blocchi di com'è composto un sensore intelligente
:::

Le reti di sensori sono molto particolari per i seguenti motivi:
1. I nodi sensori sono limitati in termini di batteria (energia), capacità computazionale e memoria. Il parametro più 
sensibile è proprio la durata della batteria. Data la natura wireless delle comunicazioni bisogna fare un bilancio di 
tratta e ricordarsi che la *path loss* è il fattore predominante nel dispendio necessario per trasmettere da A a B.<br>
$ FSPL = P_T G_T G_R (\frac{λ}{4πd})^2 $ <br> dunque vediamo come la riduzione della potenza al ricevitore segue una legge
quadratica $ d^{-2} $. Questo è un problema che induce a progettare bene gli algoritmi di routing, in quanto una trasmissione 
completamente 1-hop è impensabile, servono algoritmi di routing multi-hop con le loro peculiarità.
2. Dato il costo ridotto dei dispositivi sensori è possibile installare un gran numero di dispositivi. Avere un gran numero 
di dispositivi significa coprire meglio il territorio ed essere più capillari (e di conseguenza efficaci) nel monitoraggio.
D'altro canto non tutti i dispositivi verrebbero usati, avrei una certa percentuale inutilizzata e questo riduce l'efficienza 
della rete. Come in molti altri casi la questione sta nel trovare un equilibrio accettabile.

```{margin} Grado di connessione
È la distribuzione di porbabilità del numero di collegamenti logici che un dispositivo ha con i suoi vicini 
```

3. Dopo il rollout, i nodi si organizzano in una rete e cooperano per portare a termine un compito. In generale non c'è 
un nodo coordinatore centrale che orchestra tutto quanto. Inoltre data la natura della rete dopo verrà dimostato come il
fallimento o guasto casuale nelle reti di sensori che soddisfano un criterio di normalità sulla distribuzione dei gradi 
di connessione, non vengono influenzati in modo rilevante dai guasti random.
4. La topologia della rete cambia di frequente poiché oiltre ai guasti dobbiamo tenere conto anche dei cicli di 
sleep/operazione del dispositivo, oltre che al cambio di ruolo che ogni nodo ricoprirà (vedi capitoli successivi).

