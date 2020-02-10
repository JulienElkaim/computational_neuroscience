from period import *
from generators import *

nb_oscillators = 4


Periods(
  oscillators=gen_oscillators(nb_oscillators, mode="tau"),
  synapses=gen_synapses(nb_oscillators, mode="neutral") ,
  trigger_times= gen_trigger(nb_oscillators)
).launch().plot("sub_and_joined")

