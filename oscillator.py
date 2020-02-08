
import numpy as np



class Oscillator:

  #Initialize every params of this oscillator.
  # Default params are for a common oscillator.
  def __init__(self, sigmaS=3, sigmaF=1.5, Af = 0.5, toM=0.35, K=10, q0=0, v0=0):

    self.sigmaS = sigmaS
    self.sigmaF = sigmaF
    self.Af = Af
    self.toM = toM
    self.toS = K*toM
    self.Q = q0
    self.V = v0
    self.Vs= []
    self.ts= []


  # Function useful for Euler method.
  def _F(self, V, sigmaF):
    return V-self.Af*np.tanh((sigmaF/self.Af)*V)

  # Function useful for Euler method.
  def _f_V(self, V, sigmaF, q, i):

    return -((self._F(V, sigmaF)+q-i))*(1/self.toM)

  # Function useful for Euler method.
  def _f_Q(self, q, V):
    return (-q + self.sigmaS*V)/self.toS

  # Compute the next state of this oscillator.
  # Also, store its previous states.
  def next_state(self, inj, delta, t, inj_exogène=0):

    self.V = self.V + self._f_V(self.V, self.sigmaF, self.Q, (inj+inj_exogène) )*delta
    self.Q = self.Q + self._f_Q(self.Q, self.V)*delta

    self.Vs.append(self.V)
    self.ts.append(t)
    return self.V
