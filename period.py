from oscillator import *
from generators import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from itertools import cycle

class Periods:

  def __init__(self, delta=0.01, nb_period = 30000, oscillators=[], synapsor=gen_synapses, synapsor_mode="normal", trigger=gen_trigger):
    self.nb = nb_period
    self.periods = nb_period
    self.delta = delta
    self.t = 0.0
    self.oscillators= oscillators
    self.synapses = synapsor(len(self.oscillators), mode=synapsor_mode)
    self.trigger = trigger(len(self.oscillators))
    self.synapsesTRIGGER = 100
    self.synapsesDISABLER = 200
    self.plot_colors = cycle([
      "#00FF00",
      "#5B60A2",
      "#A01080",
      "#FF0000",
      "#0000FF",
      "#00FFFF",

    ])

  def areSynapsesON(self):
    if int(self.t) >= self.synapsesTRIGGER and int(self.t) <= self.synapsesDISABLER  :
      return True
    return False

  def launch(self):
    while(self.nb != 0):
      self.next_period()
    return self

  def plot(self, mode="normal"):
    if mode == "normal":
      return self._plot()
    if mode == "sub" or "subplot":
      return self.subplot()
    return self._plot()

  def _plotylims(self):
    minval = -5
    maxval = 5
    # for osc in self.oscillators:
    #   for V in osc.Vs:
    #     if V > maxval:
    #       maxval = V
    #     if V < minval:
    #       minval = V


    return (minval,maxval)

  def _plot(self):
    mpl.rcParams['toolbar'] = 'None'

    for osc in self.oscillators:
      plt.plot(osc.ts,osc.Vs, linewidth=0.5)
    plt.ylim(self._plotylims())
    plt.axvspan(0, self.synapsesTRIGGER, facecolor='#000000', alpha=0.1)
    plt.axvspan(self.synapsesDISABLER, self.periods*self.delta, facecolor='#000000', alpha=0.1)

    windowTitle = str(len(self.oscillators))+\
    " oscillators, connected at "+ \
    str(self.synapsesTRIGGER)+\
    " and disconnected at "+\
    str(self.synapsesDISABLER)

    plt.gcf().canvas.set_window_title(windowTitle)
    plt.show()
    return self

  def subplot(self):


    mpl.rcParams['toolbar'] = 'None'
    plot_colors = [next(self.plot_colors) for _ in range(len(self.oscillators))]

    fig = plt.figure(constrained_layout=True)
    gs = fig.add_gridspec(len(self.oscillators)+2, 1)

    for i,osc in enumerate(self.oscillators):
      ax = fig.add_subplot(gs[i,:])
      ax.set_title("Oscillator "+str(i+1)+" [σs->{} σf->{} τm->{}, K->{} ]".format(
        osc.sigmaS, osc.sigmaF, osc.toM, int(osc.toM/osc.toS)
        )
      )
      ax.set_ylim(self._plotylims())
      ax.plot(osc.ts,osc.Vs, linewidth=0.5, c=plot_colors[i])
      ax.axvspan(0, self.synapsesTRIGGER, facecolor='#000000', alpha=0.1)
      ax.axvspan(self.synapsesDISABLER, self.periods*self.delta, facecolor='#000000', alpha=0.1)

    axG = fig.add_subplot(gs[-2:,:])
    axG.set_title("Every Oscillators")
    axG.set_ylim(self._plotylims())
    axG.axvspan(0, self.synapsesTRIGGER, facecolor='#000000', alpha=0.1)
    axG.axvspan(self.synapsesDISABLER, self.periods*self.delta, facecolor='#000000', alpha=0.1)
    for i,osc in enumerate(self.oscillators):
      axG.plot(osc.ts,osc.Vs, linewidth=0.5, c=plot_colors[i])

    plt.subplots_adjust( right = 1, left = 0,
            hspace = 0.1, wspace = 0)
    windowTitle = str(len(self.oscillators))+\
    " oscillators, connected at "+ \
    str(self.synapsesTRIGGER)+\
    " and disconnected at "+\
    str(self.synapsesDISABLER)
    plt.gcf().canvas.set_window_title(windowTitle)
    plt.show()
    return self


  def next_period(self):

    for i, oscillator in enumerate(self.oscillators):
      # Synapses entre les oscillateurs

      sig_i = 0
      if self.areSynapsesON():
        for synapse in self.synapses:
          if synapse["post-synaptique"] == i:
            sig_i += synapse["poids-synaptique"] * self.oscillators[synapse["pre-synaptique"]].Vs[-1]

      oscillator.next_state(sig_i,self.delta,self.t, self.do_i_push(i))

    self.t+= self.delta
    self.nb-=1

  def do_i_push(self, i):
    if self.trigger[i] == int(self.t):

      return 1
    return 0

