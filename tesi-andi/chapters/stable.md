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

# Distribuzioni stabili

La discussione che segue non ha la pretesa di esaustività ma soltanto di portare alla luce gli aspetti principali e quali
sono le conseguenze dell'uso e delle presenza di distribuzioni stabili nel modello del sistema.

## Introduzione
I processi stabili hanno attratto un'attenzione sempre maggiore, una descrizione sistematica della teoria dei processi
"atipici" e cioè con code pesanti la possiamo trovare in {cite:p}`brookes_1955` oppure {cite:p}`feller-vol-2` ed infine in

Il teorema limite centrale offre la giustificazione fondamentale per usare una trattazione più semplificata alle distribuzioni
stabili, possiamo estenderlo ed enunciare che: le distribuzioni stabili sono le distribuzioni limite della somma di
distribuzioni normalizzate, indipendenti ed identicamente distribuite. Il caso gaussiano come distribuzione limite è solo
il caso più famoso ed ampiamente studiato. I processi gaussiani si prestano ad una trattabilità matematica molto agevole
e quindi permettono di ottenere degli ottimi indizi anche nel caso in cui io abbia variabili aleatorie qualunque, da qui
la "fama" dei processi gaussiani. Inoltre c'è da dire che i processi gaussiani sono stati i primi ad essere compresi
completamente e ad esssere utilizzati nella pratica in quanto ottimi strumenti di modellazione analitica. Il problema sta
in tutti quei casi di modellazione di processi stocastici soggetti a larghe fluttuazioni. Solitamente si modella le larghe
fluttuazioni probabilistiche come processi *non* stazionari e si riduce l'orizzonte di osservazione ad un intervallo
opportuno, sufficiente piccolo, sufficiente a conferire a quel processo delle caratteristiche di stazionarietà. Basti
pensare all'uso di strumenti come la STFT (short time Fourier transform) per l'analisi di segnali vocali o multimediali
i quali vengono in alcuni casi modellati come processi gaussiani non stazionari.

```{note} Overdispersion
È la caratterstica per cui un campione mostra una varianza maggiore di quella prevista. Questa varianza anomala avviene
per colpa della varianza che diverge nell'espressione della mia pdf.
```

Il problema della distribuzione gaussiana usata per modellare è che non riesce a catturare le caratteristiche di grandi
fluttuazioni dalla media come ad esempio fenomeni di overdispersion.
Le distribuzioni stabili non hanno queste limitazioni. In generale, queste distribuzioni hanno delle code che decadono con
una "power-law".

```{note} Power-law decay
Con decadimento con legge esponenziale intendiamo una relazione fra due quantità tale per cui una variazione nella prima
risulta in un cambio proporzionale nella seconda indipendentemente dalle loro dimensioni iniziali (pensiamo all'area ed
al legame con la lunghezza del lato)
```

Nelle distribuzioni stabili si ha poche "intuizioni applicate", la più famosa è al "Teoria del Cigno Nero" del dott. Nassim
Taleb la quale spiega come un evento molto sorprendente venga erroneamente spiegato a posteriori nonstante la conoscenza
a posteriori dell'evento. Più in particolare nella sua teoria del cigno nero, applicata principalmente nel mondo della
finanza quantitativa, riesce a spiegare e dare degli indizi su:
1. il ruolo di eventi spoporzionatamente intensi (o di alto profilo), difficili da prevedere ed eventi rari che sono oltre
le tecniche solitamente usate in discipline come tecnologia e finanza (ad esempio le medie storiche sono inaffidabili)
2. La non commensurabilità della probabilità di due eventi estremi consecutivi (poiché vigono leggi degli eventi rari)

Tornando alle distribuzioni a code pesanti, possiamo dire che queste dipendano in generale da un parametro $ \alpha $ il
quale ha come intervallo di definizione $ 0 \le \alpha \le 2 $. Più piccolo è $ \alpha$, tanto più lento sarà il decadimento
e tanto più saranno pesanti, o grasse, le code. Una nota importante da fare è la seguente: le distribuzioni fat-tailed
hanno sempre varianza infinita e se $ \alpha \le 1 $ allora anche la media non converge.

Negli ultimi decenni, i dati con code pesanti sono stati raccolti nelle discipline più disparate:
* economia
* telecomunicazioni
* idrologia

In tutti questi campi nel corso degli anni, i dati raccolti, hanno suggerito distribuzioni non gaussiane come modello.

Le distribuzioni non gaussiane hanno l'ottimo pregio che permettono di modellare un range molto più ampio di comportamenti
probabilistici se messi a confronto con distribuzioni gaussiane. Mentre da un lato ho dei modelli molto più espressivi
grazie alle distribuzioni stabili, il costo che pago è una parametrizzazione molto più ricca e complicata da stimare.
Questo poiché le distribuzioni gaussiane sono completamente identificate dalla loro funzione di autocovarianza e media,
ciò non è più vero nelle distribuzioni stabili.

Seguo l'esposizione di {cite:p}`brookes_1955` nell'enunciare quattro definizioni equivalenti di distribuzioni stabili.
### Definizione $1$
Una variabile aleatoria  $X$ è *stabile* se per dei numeri $A$ e $B$ esistono dei valori positivi $C$ e $D$ tali che

$AX_1+BX_2 \,{\buildrel d \over =}\, CX+D $ <br> dove $X_1$ e $ X_2$ sono campioni di $X$ e $=^d$ denota l'uguaglianza in distribuzione. La
distribuzione $X$ stabile viende detta *simmetrica* se la pdf di $X$ è uguale a quella di $-X$

### Teorema {cite:p}`feller-vol-2`

Per ogni distribuzione stabile della variabile aleatoria $X$, esiste un numero $\alpha \in [0,2]$ tale che il numero $C$
nella definizione precedente soddisfa <br> $ C^{\alpha} = A^{\alpha}+B^{\alpha}$ <br> il numero $\alpha$ viene chiamato
*indice di stabilità* o *esponente caratteristico*. Una distribuzione stabile con variabile aleatoria $X$ con indice
$\alpha$ viene definita $\alpha$-stabile.

### Definizione $2$

Una variabile aleatoria $X$ viene detta stabile se per ogni $n \ge 2$, è possibile trovare due numeri positivi $C_n$ e
$D_n$ tali che <br> $ X_1+ X_2+ X_3+ ... + X_n \,{\buildrel d \over =}\, C_nX+ D_n $ <br> dove ${X_i}_{i=1}^{n} $ sono campioni iid estratti da
$X$. Nel libro di {cite:p}`feller-vol-2` l'autore dimostra l'equivalenza fra le due definizioni in quanto se la definizione
$1$ è vera allora per induzione sarà verificata anche la definizione $2$, per il viceversa consultare {cite:p}`feller-vol-2`.

### Osservazioni

Sempre nel libro ({cite:p}`feller-vol-2` teorema VI.1.1) vediamo che se la definizione $2$ è vera allora vediamo che
necessariamente che <br>$C_n = n^{1/2}$ <br> per qualche $ 0 <= \alpha <= 2 $. Questo $\alpha$ è ovviamente l'esponente
caratteristico.

### Osservazione importante {cite:p}`GeSaTaq`

Consideriamo la sequenza $\displaystyle \textbf{X} = (X_i)_{i=-\infty}^{\infty}$ di variabile aleatorie. Fissiamo un
numero $\delta > 0$. Per ogni $n \ge 1$, definiamo la trasformazione $T_n$ come la mappa che dato il vettore aleatorio
$\textbf{X}$ produce $T_n\textbf{X} ={(T_nX)_i}_{-\infty}^{\infty}$ con
 <br> $\displaystyle (T_nX)_i =\frac{1}{n^{\delta}} \sum_{j=in}^{(i+1)n-1}X_j$ <br> Le trasformazioni $T_n$ con $n \ge 1$
sono chimamate *trasformazioni rinormalizzanti di gruppo* con *esponentec critico* $\delta$.

#### Lemma 1
<br> $T_{mn} = T_mT_n$ <br>
Nella monografia {cite:p}`brookes_1955` viene dimostrato come $T_{mn} = T_mT_n$ cioè la trasformazione $T_m$ seguita
dalla trasformazione $T_n$ sia euivalente alla trasformazione $T_{mn}$ e dunque la famiglia di trasformazioni
${T_N, n \ge 1}$ formano un gruppo.

#### Definizione di punto fisso
Una sequenza $\textbf{X}=(X_i)_{i=-\infty}^{\infty}$ viende detta *punto fisso* del gruppo di trasformazioni rinormalizzanti
se $T_n\textbf{X}\,{\buildrel d \over =}\,\textbf{X}$ per ogni $n \ge 1$, cioè se la distribuzione di $\textbf{x}$ è
invariante sotto $T_n$ per ogni $n \ge 1$.

La sequenza $\textbf{X}=(X_i)_{i=-\infty}^{\infty}$ di variabili aleatorie i.i.d $\alpha$-stabili è un punto fisso delle
trasformazioni $T_n$ con $\delta =\frac{1}{\alpha}$ poiché:
<br> $(T_n\textbf{X})_i = \frac{1}{n^{\frac{1}{\alpha}}}(X_{in}+X_{in+1}+ \cdot + X_{i(n+1)-1}) \,{\buildrel d \over =}\, X_i$
<br> e poiché i campioni della sequenza $X_i$ sono indipendenti per ipotesi, ottengo per linearità anche l'indipendenza delle
$(T_n\textbf{X})$.

### Applicazioni

La teoria dei gruppi di trasfomazioni rinormalizzanti pone le basi per un metodo estrememante veloce per produrre e
simulare variabili aleatorie con code pesanti in modo corretto. Segue una simulazione di come analizzare una distribuzione
di somma di Pareto usando il package matlab {cite:p}`STBL`.

Consideriamo una variabile aleatoria $X$ la cui distribuzione cumulativa è data da: <br>
$\displaystyle Prob[X \leq x] = \begin{cases}
          1-x^{-\frac{3}{4}} & \text{ x > 1 }\\
          0  & \text{altrove}
     \end{cases}$ <br>

Posso campionare molto facilmente da questa, poiché inverto la CDF ottenendo: <br>
$X = u^{-\frac{4}{3}}$ dove $u \approx \textbf{U}(0,1)$ <br> i vari $X_i$ sono i.i.d.

Possiamo vedere come dalla coda di questa ditribuzione ed osservando che $\alpha=\frac{4}{3}$ qui avrò una media infinita.
In questo caso, come minimo, non posso apllicare il teorema limite centrale. Tiriamo fuori il gruppo di trasformazioni
rinormalizzanti ed in particolare consideriamo la somma riscalata dal fattore $n$ come nella definizione:
$X^{+n} = \displaystyle n^{-\frac{4}{3}} \sum_{i=1}^{n}X_i $ in cui al solito ipotizziamo che i vari campio siano i.i.d.

Si può dimostrare {cite:p}`GeSaTaq` come la somma precedentemente descitta converga ad una distribuzione stabile
$S(\alpha_0,\beta_0,\gamma_0,\delta_0)$. A questo punto possiamo verificare ciò che troviamo nel libro citato. Generiamo
$X^{+100}_i$ una sequenza di 100 campioni ed applichiamo la trasformazione, come mostrato nel seguente listato:

```{code}
    N = 300;
    sampsize = 100;
    s = RandStream.create('mrg32k3a','NumStreams',1,'Seed',50); % For reproducibility
    X = zeros(N,1);
    for i = 1:N
        % Generate a normalized sum of Pareto-type random variables
        Samp = 1./rand(s,sampsize,1).^(4/3);
        X(i) = sum(Samp)/sampsize^(4/3); % Normalize sum
    end
    % estimate parameters
    p = stblfit(X,'ecf',statset('Display','iter'));
    % plot data with fit parameters
    xmax = 15;
    H = figure(1);
    set(H,'Position', [517 626 939 410]);
    clf;
    title('Stable fit to sums of Pareto random variables');
    subplot(1,2,1)
    hold on
    stem(X(X < xmax),stblpdf(X(X<xmax),p(1),p(2),p(3),p(4),'quick'));
    x = 0:.1:xmax;
    plot(x,stblpdf(x,p(1),p(2),p(3),p(4),'quick'),'r-')
    hold off
    xlabel(['\alpha_0 = ',num2str(p(1)),'  \beta_0 = ',num2str(p(2)),'  \gamma_0 = ',num2str(p(3)),'  \delta_0 = ',num2str(p(4))]);
    legend('Data','Fit stable density')
    subplot(1,2,2)
    CDF = prctile(X,[1:75]);
    cmin = CDF(1);
    cmax = CDF(end);
    x = cmin:.1:cmax;
    estCDF = stblcdf(x,p(1),p(2),p(3),p(4));
    plot(CDF,[.01:.01:.75],'b.',x,estCDF,'r-')
    legend('Empirical CDF','Estimated CDF','Location','northwest')
```

:::{figure-md} markdown-fig
<img src="C:\\Users\\DULLA\\Pictures\\Cattura_STBL.JPG" alt="mcu" class="bg-primary mb-1" width="700px">

Risultato dell'interprete
:::

Questo risultato ci dice che l'uso dei metodi statistici classici è inefficace nel dimostrare la convergenza dei vari
campioni $X_i$. Il package STBLFIT descritto nella repository {cite:p}`STBL` mostra come ottenre un fit accurato e a quale
distribuzione stabile convergeranno i miei dati. Ci tornerà molto utile nell'ultimo capitolo quado tenteremo un fit dei
dati raccolti *live* nella rete.