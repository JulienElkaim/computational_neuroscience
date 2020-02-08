import numpy as np
import matplotlib.pyplot as plt
import math


toM = 0.35
toS = 3.5
Af = 0.5
sigmaS = 3
sigmaF = 1.5
K = 10
V0 = 0
q0 = 0
delta = 0.01

def F(V, sigmaF):
    return V-Af*np.tanh((sigmaF/Af)*V)

def f_V(V, sigmaF, q, i, t):
    return -((F(V, sigmaF)+q-i))*(1/toM)

def f_Q(q, V):
    return (-q + sigmaS*V)/toS


def euler(V, sigmaF, q, i):
    t = 0
    T = 50
    list_V = []
    list_Q = []
    list_T = []
    list_I = []
    while t < T:
        if t<= 30:
            i = np.sin(2*t + 1.5708)
        else:
            i = 0
        V = V + f_V(V, sigmaF, q, i, t)*delta
        q = q + f_Q(q, V)*delta
        t += delta
        #print("Temps: ", t, V)
        list_V.append(V)
        list_T.append(t)
        list_Q.append(q)
        list_I.append(i)
    return list_V, list_T, list_Q, list_I

Vs,Ts, Vq, I = euler(0, sigmaF, 0, 0)
plt.plot(Ts, Vs)
plt.plot(Ts, I)
plt.show()
