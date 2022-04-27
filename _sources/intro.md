# Strategie di network forming con tecniche SDN per reti di sensori per applicazioni di mobile IoT

Le reti di sensori wireless, comunemente chiamate WSN Wireless Sensor Networks, vengono usate per molte applicazioni a
lungo termine, come ad esempio:
* Applicazioni militari
* Città intelligenti e servizi alla popolazione
* Industria 4.0 e smart factories

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
<img src="images/WSN_topo.jpg" alt="fishy" class="bg-primary mb-1" width="700px">

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
sensibile  