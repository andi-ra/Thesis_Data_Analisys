---
jupytext:
cell_metadata_filter: -all formats: md:myst text_representation:
extension: .md format_name: myst format_version: 0.13 jupytext_version: 1.11.5 kernelspec:
display_name: Python 3 language: python name: python3
---

# Ingegnerizzazione del traffico

In questo capitolo vado a mostrare gli aspetti di modellazione del sistema, enunciare il problema e gli algoritmi
proposti.

Introduzione Il routing in una rete è un’operazione complessa che coinvolge molti attori e protcolli che permettono
l’organizzazione fra tutti questi componenti indipendenti fra di loro. Le ragioni della complessità sono molteplici:

Il routing richiede un grado di coordinazione fra i vai nodi nella rete o nel segmento di rete considerato piuttosto che
solo fra due nodi. Ad esempio pensiamo i protocolli di livello 2 e livello 4.

L’architettura di routing deve risolvere tutti quei casi di guasti e malfunzionamenti dei collegamenti o dei nodi,
redirezionare il traffico ed aggiornare i database informativi di ogni device.

Per ottenere delle performance buone, l’algoritmo di routing può essere costretto a modificare le sue rotte
precedentemente calcolate quando parti o segmenti di rete diventano congestionati.

Difficoltà e obiettivi nel routing Le due funzioni principali di un algoritmo di routing sono:

```{margin} Routing table
È la struttura dati che un dispositivo ha al suo interno in cui troviamo una lista di destinatari, la distanza e come
raggiungere quel preciso destinatario ed in più altre informazioni a seconda del protocollo finale che la userà
```

È la struttura dati che un dispositivo ha al suo interno in cui troviamo una lista di destinatari, la distanza e come
raggiungere quel preciso destinatario ed in più altre informazioni a seconda del protocollo finale che la userà

la selezione delle rotte fra le varie coppie origine destinazione

la consegna dei messaggi alla corretta destinazione una volta scelta la rotta

La seconda funzione può sembrare banale una volta usate le routing table. Ciò non è sempre vero, in quanto questo
concetto è molto semplice nel caso che io possa fare affidamento sull’infrastruttura di rete. Nel caso in cui questo non
sia vero e quindi io ho a che fare con una infrastruttura non affidabile, diventa fondamentale il modo in cui scelgo il
next-hop.

```{margin} Next-hop
È il dispositivo successivo rispetto al device sotto esame, all’interno del percorso che unisce topologicamente due
punti di interesse, ad esempio possono essere una coppia origine-destinazione
```

In quanto è possibile che 2 scelte diverse di next-hop portino allo stesso destinatario nella topologia, ma un next-hop
è stato disconnesso poiché il collegamento prescelto non è più disponibile. Non mi concentro sulla seconda funzione e
sul capire cosa succede nel caso che un collegamento non sia disponibile ma mi concentrerò sulla prima funzione e come
influisce sulle performance della rete.

Vi sono due metriche principali sulla performance di una rete che sono influenzati dall’algoritmo di routing:

1. Throughput, la quantità di servizio offerta dalla rete

2. Latenza media dei pacchetti, la qualità del servizio offerto dalla rete

Il routing interagisce con il controllo di flusso per determinare queste metriche di performance attraverso un controllo
a catena chiusa.

:::{figure-md} markdown-fig
<img src="https://miro.medium.com/max/1400/1*q_J7uLY97EyiFdYXOXuG0g.png" alt="mcu" class="bg-primary mb-1" width="700px">

Immagine **temporanea**
:::