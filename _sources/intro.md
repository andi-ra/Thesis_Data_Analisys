# SDN forming per mobile IoT

Le reti di sensori wireless, comunemente chiamate WSN Wireless Sensor Networks, vengono usate per molte applicazioni a
lungo termine, come ad esempio:
* Applicazioni militari
* Città intelligenti e servizi alla popolazione
* Industria 4.0 e smart factories
* veicoli intelligenti

Tutte queste applicazioni innovative e fondamentali nei prossimi decenni possono trarre molto valore dalle reti di 
sensori. Più in generale possiamo pensare ad una rete come ad un modello che cerca di catturare la complessità delle 
relazioni e delle varie ricombinazioni ed interazioni fra loro e gli agenti fra i quali si esplicano queste relazioni.
Con agenti intendiamo qualunque entità che ha interesse nell'interagire con gli altri, questa interazione può avvenire
per ottenere un guadagno (non solo monetario), oppure per vincoli del sistema in cui acquisisce valore la rete.

Queste reti e relazioni giocano un ruolo molto importante negli scambi economici, ad esempio: scambio e commercio di beni
in mercati decentralizzati, ricerca e sviluppo e relazioni e partnership fra aziende ed infine trattati commerciali
fra nazioni. Dobbiamo studiare le reti non solo per la loro espressività ed efficacia nel modellare relazioni economiche,
ma soprattutto perché il modello di rete usato nelle telecomunicazioni, così come inteso nelle reti sociali o economiche,
seguono dei precisi schemi di genesi. Questi processi di genesi della rete sono ancora oggetto di ricerca ma con le
risposte che ad oggi abbiamo, attingendo dalle reti sociali ed economiche, possiamo trarre importanti lezioni e spunti
di riflessione. 

In prima battuta, dobbiamo dire che i processi di genesi e "formazione di reti" sono classificabili in due modi:
* Distribuiti, reti economiche e sociali prive di un controllo dall'alto
* Centralizzate, reti di telecomunicazione controllate dall'alto e progettate

Il primo punto ha acquisito un'importanza sempre maggiore in un'ottica di reti di oggetti, le cosiddette reti di "social
things", oggetti che usano i loro peculiari pattern di comunicazione, per trasmettersi informazioni. 

Il motivo principale per cui ci preoccupiamo di scoprire quali sono i modelli di formazione, cercare di approfondirli e
cercare di controllarli è perché la struttura a rete fa da discrimine fra una rete che non funziona e una rete che 
"funziona" e soprattutto riuscendo ad ottenere una vista in questi processi possiamo valutare i vari trade-off che 
caratterizzano queste reti. Queste sono alcune delle domande interessanti che nascono:
* Come fanno queste relazioni ad essere importanti nel determinare il risultato di una trasmissione dati?
```{margin} Random deployment
È l'attività di distribuzione, installazione ed operazione dei dispositivi in posizioni geografiche totalmente causali 
```
* Come possiamo predire reti che è probabile che si formino quando faccio un *random deployment* e lascio i dispositivi 
liberi di connettersi con i propri vicini?
* Quanto sono efficienti le reti che si formano e come fa questa efficienza a dipendere dal "valore" che ogni dispositivo
ha?

Per una trattazione più indirizzata verso gli aspetti legati all'economia dei modelli a reti e i punti in comune con le 
reti di telecomunicazioni consultare gli articoli di {cite:p}`Jackson2003`, {cite:p}`starr1999exchange`.

Un primo obiettivo che mi pongo in questo manoscritto, è quello di considerare le differenze fra i vari modelli di network
forming, strategie e differenze. 

Valuteremo inoltre, le differenze fra un approccio totalmente distribuito ed uno 
centralizzato nel tentativo di dare risposta alla domanda: quanto mi costa il *non* usare un controllo centralizzato della 
rete? Come misuro questo costo?