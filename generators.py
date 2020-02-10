from oscillator import *
from random import randrange as rdmint

"""
Every kind of generators:

- Oscillators, generate a list of nb oscillators.
- Synapses, generate a matrice of synapses between nbn oscillators.
- Triggers, generate a list of trigerring time for each ith oscillators.
"""


#Return a list of oscillators.
#Oscillators output depends on the mode used.
def gen_oscillators(nb, mode ="sigmaS"):
  if mode =="sigmaS":
    return [
      Oscillator(
        sigmaS=rdmint(200,500,1)/100,
        sigmaF=1.5,
        Af=0.5,
        toM=0.35,
        K=10
      )
      for n in range(nb)
    ]
  elif mode=="K":

    return [
      Oscillator(
        sigmaS=3,
        sigmaF=1.5,
        Af=0.5,
        toM=0.35,
        K=rdmint(10,20)
      )
      for n in range(nb)
    ]

  elif mode=="tau":

    return [
      Oscillator(
        sigmaS=3,
        sigmaF=1.5,
        Af=0.5,
        toM=rdmint(25,45,1)/100,
        K=10
      )
      for n in range(nb)
    ]
  elif mode=="tauK":

    return [
      Oscillator(
        sigmaS=3,
        sigmaF=1.5,
        Af=0.5,
        toM=rdmint(25,45,1)/100,
        K=rdmint(10,20)
      )
      for n in range(nb)
    ]


  return [
    Oscillator(
      sigmaS=3,
      sigmaF=1.5,
      Af=0.5,
      toM=0.35,
      K=10
    )
    for n in range(nb)
  ]






#Return a list of synapses (Synapses Matrix).
#Their params depends on the mode used.
def gen_synapses(nbn, mode ="normal"):
  if mode=="neutral":
    return [
      {
        "pre-synaptique": i_pre,
        "post-synaptique": i_post,
        "poids-synaptique": 0 if i_pre == i_post else 0.3
      }
      for i_pre in range(nbn)
      for i_post in range(nbn)
    ]
  elif mode=="low-neutral":
    return [
      {
        "pre-synaptique": i_pre,
        "post-synaptique": i_post,
        "poids-synaptique": 0 if i_pre == i_post else 0.1
      }
      for i_pre in range(nbn)
      for i_post in range(nbn)
    ]
  elif mode=="random":
    return [
      {
        "pre-synaptique": i_pre,
        "post-synaptique": i_post,
        "poids-synaptique": 0 if i_pre == i_post else rdmint(-100,100,1)/100
      }
      for i_pre in range(nbn)
      for i_post in range(nbn)
    ]

  else: # "normal" mode
    return [
      {
        "pre-synaptique": i_pre,
        "post-synaptique": i_post,
        "poids-synaptique": 0 if i_pre == i_post else 1
      }
      for i_pre in range(nbn)
      for i_post in range(nbn)
    ]




#Return a list of trigger time for each oscillator.
# No mode implemented.
def gen_trigger(nb):
  return [i for i in range(nb)]

