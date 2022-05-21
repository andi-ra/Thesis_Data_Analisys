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

+++ {"pycharm": {"name": "#%% md\n"}}

# Allocazione ottima delle risorse

Questo capitolo risolve il problema dell'equilibrio su reti. Per la risoluzione di questo problema si usa
l'algoritmo di Frank & Wolfe. In particolare, per la risoluzione del problema di ottimizzazione che deriva nel
calcolo di equilibrio su reti. Non approfondisco le ipotesi che portano a questa formulazione ma mi limito ad enunciare
il problema di programmazione convessa.

Introduciamo preliminarmente la notazione adottata. Siano
* $G = <N, A>$ un grafo orientato;
* $P$ un insieme di coppie origine/destinazione (O-D);
* $d_p$ la domanda tra la coppia origine/destinazione $p \in P$;
* $K_p$ l’insieme dei cammini che connettono la coppia p;
* $K$ l’insieme di tutti i cammini, ossia $K = \textbf{U}_{p \in P} K_p$;
* $\delta_{a,k}$ una funzione indicatrice dell'appartenenza dell'arco $a$ al percorso $k$

Il flusso del cammino k è $h_k$, con $h_k ≥ 0$. Il flusso di un arco $a \in A$, indicato con $v_a$, è dato
dalla somma dei flussi dei cammini che attraversano l’arco, ossia <br>
$ \displaystyle v_a = \sum_{k \in K} h_k \delta_{a,k}$

 Il costo di un cammino k, denotato con sk, `e la somma dei costi degli archi appartenenti al cammino k <br>
$ \displaystyle s_k = \sum_{a \in A} s_a(v) \delta_{a,k}$

Per ogni coppia origine-destinazione p, la somma dei flussi dei cammini deve essere uguale alla domanda d_p, ossia 
abbiamo il vincolo
$ X = \sum_{k \in Kp} h_k = d_p $ 

Il costo della rete $S(v)$ è la somma totale dei costi degli utenti, ossia
$\displaystyle  S(v) = \sum_{k \in K} h_k s_k = \sum_{k \in K}\sum_{a \in A} h_k \delta_{a,k} s_a(v) =  \sum_{a \in A} s_a(v) v_a$

Il problema di assegnamento di traffico in una rete di trasporto riguarda la previsione di flussi
lungo gli archi della rete derivanti dalle scelte che ogni singolo utente effettua per determinare
li cammino dalla propria origine alla propria destinazione. Nel seguito introdurremo i principi
di ottimalit`a di Wardrop, che sono usualmente adottati nella formulazione del problema di
assegnamento di traffico

## I principi di ottimalità di Wardrop
Nel problema di assegnamento di traffico usualmente due principi di ottimalit`a di Wardrop sono
adottati:
- il primo principio è basato sull’analisi di un comportamento intuitivo per una rete di traffico, secondo cui ogni 
utente tende a minimizzare il proprio tempo di viaggio, di conseguenza questo principio è detto di tipo user equilibrium;
- il secondo principio, di tipo system optimum, corrisponde alla situazione in cui deve essere minimizzato il tempo 
complessivo di viaggio di tutti gli utenti.

## Equilibrio di tipo system optimum
Analizziamo brevemente la formulazione del problema nel caso in cui ci sia un controller che gestisce la rete in modo centralizzato.
L’obiettivo sarebbe quello di minimizzare il costo totale della rete (il tempo totale di trasporto) definito come segue

$\displaystyle S =  \sum_{a \in A} s_a(v)v_a $

con i vincoli di soddisfacimento delle domande delle varie coppie e i vincoli di non negatività delle variabili. Di 
conseguenza, il problema da risolvere sarebbe il seguente problema di ottimizzazione vincolata:

$\displaystyle min_{h,v} \sum_{a \in A} s_a(v)v_a$ <br> $\displaystyle \qquad  \sum_{k \in Kp} h_k = d_p \qquad \forall p \in P$ <br> 
$\displaystyle \qquad v_a = \sum_{k \in K} h_k \delta_{a,k} \qquad \forall a \in A $ <br> $\qquad h \ge 0$ 

Questo problema può essere trasformato in un problema di ottimizzazione convessa risolvibile con il metodo di Frank&Wolfe.

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
import numpy as np
import sympy
import sympy as sym
from sympy import init_printing
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
from IPython.display import display, Math

x1, x2, x3 = sym.symbols('x1, x2, x3')
x = sym.Matrix([[x1], [x2], [x3]])
Q = sym.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0.1]])
c = sym.Matrix([[0], [0], [0.55]])

print("Matrice di adiancenza della rete")
print(Q)
print("Vettore dei costi aggiuntivi, offset ")
print(c)
```

Adesso posso visualizzare la funzione obiettivo quadratica del mio problema:

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
init_printing()

obj = 0.5 * (x.T * Q * x) + c.T * x
obj
```

Adesso visualizzo anche l'obiettivo al punto iniziale:

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
cost = obj.subs({x1: 0.4, x2: 0.3, x3: 0.3})
display(Math(r'D(x_0): {:.4f}'.format(cost[0])))
```

Adesso posso visualizzare la funzione con lo step size e l'aggiornamento

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
x1_bar, x2_bar, x3_bar = sym.symbols('\overline{x_1}, \overline{x_2}, \overline{x_3}')
x_bar = sym.Matrix([[x1_bar], [x2_bar], [x3_bar]])
d_k = x_bar - x
display(Math(r'd_k: '))
d_k
```

Adesso visualizzo il punto iniziale e mi calcolo il nuovo punto

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
a = sym.symbols('\\alpha')
x_k = x + a * d_k

display(Math(r'x_{k+1}: '))
x_k
```

+++ {"pycharm": {"name": "#%% md\n"}}

Adesso mi calcolo il gradiente

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
grad = x.T * Q + c.T
display(Math(r'\nabla: '))
grad.T
```

Adesso mi calcolo ${\alpha}$ come forma chiusa e nella cella successiva sostituisco i valori:

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
alpha = -(grad * d_k) / (d_k.T * Q * d_k)[0]
alpha
```

Adesso sostituisco i valori e verifico:

    1. I valori tornano con Gallagher
    2. La direzione scelta con Q
    3. Calcolo del nuovo punto con il quale calcolare la direzione di discesa
$\begin{align} \overline{x}_{k+1} = argmin {<\nabla f(x_k), x>} \quad \forall	 x \in C \end{align}$

Punto iniziale scelto per far partire l'algoritmo, uso il seguente:

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
result_x = x.subs({x1: 0.4, x2: 0.3, x3: 0.3})
result_x
```

+++ {"pycharm": {"name": "#%% md\n"}}

Uso questa soluzione iniziale:

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
result_x_bar = x_bar.subs({x1_bar: 1, x2_bar: 0, x3_bar: 0})
result_x_bar
```

Mi calcolo la nuova direzione

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
result_d_k = d_k.subs({x1: 0.4, x2: 0.3, x3: 0.3, x1_bar: 1, x2_bar: 0, x3_bar: 0})
result_d_k
```

Adesso mi calcolo lo step size con la line minimization

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
step_result = alpha.subs({x1: 0.4, x2: 0.3, x3: 0.3, x1_bar: 1, x2_bar: 0, x3_bar: 0})
step_result
```

Il nuovo punto è

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
calc_x = np.array(x.subs({x1: 0.4, x2: 0.3, x3: 0.3}))
calc_a = np.array(a.subs({a: step_result}))
calc_d_k = np.array(d_k.subs({x1: 0.4, x2: 0.3, x3: 0.3, x1_bar: 1, x2_bar: 0, x3_bar: 0}))
new_point = calc_x + calc_a * calc_d_k
new_point
```

#### Seconda iterazione
Adesso inizio con la nuova iterazione. Inizio col punto che mi sono appena calcolato e pongo:

$\begin{align} \overline{x}_{1} = argmin {<\nabla f(x_0), x>} \quad \forall	 x \in C \end{align}$

Questo me lo calcolo con le condizioni KKT per i problemi con vincoli di simplesso. Dunque il nuovo punto che userò è
soluzione del seguente problema

$\begin{align} minimize \sum_{i=1}^{n} \frac{\partial f(x_{k})}{\partial x_{i}}(x_{i}-x_{i}^k) \\ st
\sum_{i=1}^{n} x_{i} = 1
\end{align}$

La soluzione a questo problema è un punto $\bar{x}_{k} $ il quale ha tutte le coordinate uguali
a zero eccezione fatta per una sola coordinata la quale è uguale ad 1. La j-esima coordinata corrisponde a quella
coordinata con valore minimo di derivata (vedi le condizioni di KKT per il problema)

$\begin{align} j = argmin \frac{\partial f(x_{k})}{\partial x_{i}}\quad \forall i =1 ... n \end{align}$

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
gradient = grad.subs({x1: new_point[0][0], x2: new_point[1][0], x3: new_point[2][0]})
display(Math(r'\nabla f(x_1): '))
gradient
```

Adesso applico le KKT e calcolo il nuovo punto che userò per la direzione di discesa

idx_oracle = np.argmax(np.abs(grad))
mag_oracle = alpha * np.sign(-grad[idx_oracle])

+++

Definisco la per il singolo step dell'iterazione poi la lancio dalla funzione FW (principale)

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
def step_iteration(x_k: np.ndarray):
    grad = (x_k.T.dot(Q) + c.T).ravel()
    idx_oracle = np.argmin(np.abs(grad))
    mag_oracle = np.sign(grad[idx_oracle])
    d_t = -x_k.copy()
    d_t[idx_oracle] += mag_oracle
    g_t = - d_t.T.dot(grad).ravel()
    step_size = -grad.dot(d_t) / (d_t.T.dot(Q)).dot(d_t)
    step_size = np.minimum(step_size, 1.)
    x_k = x_k + step_size * d_t
    return x_k, g_t, d_t
```

Questa è la funzione principale in cui metto tutto insieme

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
Q = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0.1]])
c = np.array([[0], [0], [0.55]])
```

Esecuzione e test obiettivo, direzione se è di discesa, certificato duale

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
x_k = np.array([[0.4], [0.3], [0.3]])
s_k = np.array([[1], [0], [0]])
grad = x_k.T.dot(Q) + c.T
point, dual_value, direction = step_iteration(x_k)
display(Math(r'<\nabla f(x_2),d_2> : {:.4f}'.format(direction.T.dot(grad.T).ravel()[0])))
display(Math(r'Dual(x_2): {:.4f}'.format(dual_value.ravel()[0])))
print("Direzione di discesa: ")
print(direction)
print("Punto calcolato")
print(point)
```

```{code-cell} ipython2
---
pycharm:
  name: '#%%

    '
---
for i in range(1,321):
    point, dual_value, direction = step_iteration(point)
display(Math(r'<\nabla f(x_3),d_3> : {:.4f}'.format(direction.T.dot(grad.T).ravel()[0])))
display(Math(r'Dual(x_3): {:.4f}'.format(dual_value.ravel()[0])))
print("Direzione di discesa: ")
print(direction)
print("Punto calcolato")
print(point)
obj = 0.5*(point.T.dot(Q)).dot(point) + c.T.dot(point)
display(Math(r'Objective(x_3): {:.4f}'.format(obj.ravel()[0])))
```
