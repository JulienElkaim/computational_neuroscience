from period import *
from generators import *


Periods(
  oscillators=gen_oscillators(3, mode="to"),
  synapsor=gen_synapses,
  synapsor_mode="neutral",
  trigger= gen_trigger
).launch().plot("sub")

