from pathlib import Path
import platform
import ctypes
from ctypes.util import find_library
import sys

if platform.system() == "Windows":
    buildFolder = Path("iq-neuron/out/build/x64-Debug")
    libiqPath = str(buildFolder / "iq-network.dll")
    libizPath = str(buildFolder / "iz-network.dll")
    liblifPath = str(buildFolder / "lif-network.dll")
else:
    buildFolder = Path("iqif")
    libiqPath = buildFolder / find_library("iq-network")
    libizPath = buildFolder / find_library("iz-network")
    liblifPath = buildFolder / find_library("lif-network")

try:
    libiq = ctypes.CDLL(libiqPath)
    #libiq = ctypes.CDLL(libiqPath)
except OSError:
    print("Unable to load iq shared library.")
    sys.exit()

try:
    libiz = ctypes.CDLL(libizPath)
    #libiz = ctypes.CDLL(find_library("iz-network"))
except OSError:
    print("Unable to load iz shared library.")
    sys.exit()

try:
    liblif = ctypes.CDLL(liblifPath)
    #liblif = ctypes.CDLL(find_library("lif-network"))
except OSError:
    print("Unable to load lif shared library.")
    sys.exit()

print("All libs loaded. Congrats!")

class iqnet(object):
    def __init__(self, par, con):
        #libiq.iq_network_new.argtypes = None
        libiq.iq_network_new.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        libiq.iq_network_new.restype = ctypes.c_void_p

        libiq.iq_network_num_neurons.argtypes = [ctypes.c_void_p]
        libiq.iq_network_num_neurons.restype = ctypes.c_int

        libiq.iq_network_send_synapse.argtypes = [ctypes.c_void_p]
        libiq.iq_network_send_synapse.restype = ctypes.c_void_p

        libiq.iq_network_set_biascurrent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        libiq.iq_network_set_biascurrent.restype = ctypes.c_int

        libiq.iq_network_set_neuron.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        libiq.iq_network_set_neuron.restype = ctypes.c_int

        libiq.iq_network_set_weight.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        libiq.iq_network_set_weight.restype = ctypes.c_int

        libiq.iq_network_set_surrogate_tau.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiq.iq_network_set_surrogate_tau.restype = ctypes.c_int

        libiq.iq_network_set_vmax.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        libiq.iq_network_set_vmax.restype = ctypes.c_int

        libiq.iq_network_set_vmin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        libiq.iq_network_set_vmin.restype = ctypes.c_int

        libiq.iq_network_potential.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiq.iq_network_potential.restype = ctypes.c_int

        libiq.iq_network_spike_count.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiq.iq_network_spike_count.restype = ctypes.c_int

        libiq.iq_network_spike_rate.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiq.iq_network_spike_rate.restype = ctypes.c_float

        libiq.iq_network_set_num_threads.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiq.iq_network_set_num_threads.restype = ctypes.c_void_p

        b_par = par.encode('utf-8')
        b_con = con.encode('utf-8')
        self.obj = libiq.iq_network_new(b_par, b_con)

    def num_neurons(self):
        return libiq.iq_network_num_neurons(self.obj)

    def send_synapse(self):
        return libiq.iq_network_send_synapse(self.obj)

    def set_biascurrent(self, neuron_index, biascurrent):
        return libiq.iq_network_set_biascurrent(self.obj, neuron_index, biascurrent)

    def set_neuron(self, neuron_index, rest, threshold, reset, a, b, noise):
        return libiq.iq_network_set_neuron(self.obj, neuron_index, rest, threshold, reset, a, b, noise)

    def set_weight(self, pre, post, weight, tau):
        return libiq.iq_network_set_weight(self.obj, pre, post, weight, tau)

    def set_surrogate_tau(self, s_tau):
        return libiq.iq_network_set_surrogate_tau(self.obj, s_tau)

    def set_vmax(self, neuron_index, vmax):
        return libiq.iq_network_set_vmax(self.obj, neuron_index, vmax)

    def set_vmin(self, neuron_index, vmin):
        return libiq.iq_network_set_vmin(self.obj, neuron_index, vmin)

    def potential(self, neuron_index):
        return libiq.iq_network_potential(self.obj, neuron_index)

    def spike_count(self, neuron_index):
        return libiq.iq_network_spike_count(self.obj, neuron_index)

    def spike_rate(self, neuron_index):
        return libiq.iq_network_spike_rate(self.obj, neuron_index)

    def set_num_threads(self, num_threads):
        return libiq.iq_network_set_num_threads(self.obj, num_threads)

class iznet(object):
    def __init__(self, par, con):
        #libiz.iz_network_new.argtypes = None
        libiz.iz_network_new.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        libiz.iz_network_new.restype = ctypes.c_void_p

        libiz.iz_network_num_neurons.argtypes = [ctypes.c_void_p]
        libiz.iz_network_num_neurons.restype = ctypes.c_int

        libiz.iz_network_send_synapse.argtypes = [ctypes.c_void_p]
        libiz.iz_network_send_synapse.restype = ctypes.c_void_p

        libiz.iz_network_set_biascurrent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        libiz.iz_network_set_biascurrent.restype = ctypes.c_int

        libiz.iz_network_set_neuron.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
        libiz.iz_network_set_neuron.restype = ctypes.c_int

        libiz.iz_network_set_weight.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_int]
        libiz.iz_network_set_weight.restype = ctypes.c_int

        libiz.iz_network_set_vmax.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        libiz.iz_network_set_vmax.restype = ctypes.c_int

        libiz.iz_network_set_vmin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        libiz.iz_network_set_vmin.restype = ctypes.c_int

        libiz.iz_network_potential.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiz.iz_network_potential.restype = ctypes.c_float

        libiz.iz_network_adaptive_term.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiz.iz_network_adaptive_term.restype = ctypes.c_float

        libiz.iz_network_spike_count.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiz.iz_network_spike_count.restype = ctypes.c_int

        libiz.iz_network_spike_rate.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiz.iz_network_spike_rate.restype = ctypes.c_float

        libiz.iz_network_set_num_threads.argtypes = [ctypes.c_void_p, ctypes.c_int]
        libiz.iz_network_set_num_threads.restype = ctypes.c_void_p

        b_par = par.encode('utf-8')
        b_con = con.encode('utf-8')
        self.obj = libiz.iz_network_new(b_par, b_con)

    def num_neurons(self):
        return libiz.iz_network_num_neurons(self.obj)

    def send_synapse(self):
        return libiz.iz_network_send_synapse(self.obj)

    def set_biascurrent(self, neuron_index, biascurrent):
        return libiz.iz_network_set_biascurrent(self.obj, neuron_index, biascurrent)

    def set_neuron(self, neuron_index, a, b, c, d, k, rest, threshold, noise):
        return libiz.iz_network_set_neuron(self.obj, neuron_index, a, b, c, d, k, rest, threshold, noise)

    def set_weight(self, pre, post, weight, tau):
        return libiz.iz_network_set_weight(self.obj, pre, post, weight, tau)

    def set_vmax(self, neuron_index, vmax):
        return libiz.iz_network_set_vmax(self.obj, neuron_index, vmax)

    def set_vmin(self, neuron_index, vmin):
        return libiz.iz_network_set_vmin(self.obj, neuron_index, vmin)

    def potential(self, neuron_index):
        return libiz.iz_network_potential(self.obj, neuron_index)

    def adaptive_term(self, neuron_index):
        return libiz.iz_network_adaptive_term(self.obj, neuron_index)

    def spike_count(self, neuron_index):
        return libiz.iz_network_spike_count(self.obj, neuron_index)

    def spike_rate(self, neuron_index):
        return libiz.iz_network_spike_rate(self.obj, neuron_index)
    
    def set_num_threads(self, num_threads):
        return libiz.iz_network_set_num_threads(self.obj, num_threads)

class lifnet(object):
    def __init__(self, par, con):
        #liblif.lif_network_new.argtypes = None
        liblif.lif_network_new.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        liblif.lif_network_new.restype = ctypes.c_void_p

        liblif.lif_network_num_neurons.argtypes = [ctypes.c_void_p]
        liblif.lif_network_num_neurons.restype = ctypes.c_int

        liblif.lif_network_send_synapse.argtypes = [ctypes.c_void_p]
        liblif.lif_network_send_synapse.restype = ctypes.c_void_p

        liblif.lif_network_set_biascurrent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        liblif.lif_network_set_biascurrent.restype = ctypes.c_int

        liblif.lif_network_set_neuron.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int]
        liblif.lif_network_set_neuron.restype = ctypes.c_int

        liblif.lif_network_set_weight.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_int]
        liblif.lif_network_set_weight.restype = ctypes.c_int

        liblif.lif_network_set_vmax.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        liblif.lif_network_set_vmax.restype = ctypes.c_int

        liblif.lif_network_set_vmin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        liblif.lif_network_set_vmin.restype = ctypes.c_int

        liblif.lif_network_potential.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.lif_network_potential.restype = ctypes.c_float

        liblif.lif_network_spike_count.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.lif_network_spike_count.restype = ctypes.c_int

        liblif.lif_network_spike_rate.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.lif_network_spike_rate.restype = ctypes.c_float

        liblif.lif_network_set_num_threads.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.lif_network_set_num_threads.restype = ctypes.c_void_p

        b_par = par.encode('utf-8')
        b_con = con.encode('utf-8')
        self.obj = liblif.lif_network_new(b_par, b_con)

    def num_neurons(self):
        return liblif.lif_network_num_neurons(self.obj)

    def send_synapse(self):
        return liblif.lif_network_send_synapse(self.obj)

    def set_biascurrent(self, neuron_index, biascurrent):
        return liblif.lif_network_set_biascurrent(self.obj, neuron_index, biascurrent)

    def set_neuron(self, neuron_index, g, rest, threshold, reset, noise):
        return liblif.lif_network_set_neuron(self.obj, neuron_index, g, rest, threshold, reset, noise)

    def set_weight(self, pre, post, weight, tau):
        return liblif.lif_network_set_weight(self.obj, pre, post, weight, tau)

    def set_vmax(self, neuron_index, vmax):
        return liblif.lif_network_set_vmax(self.obj, neuron_index, vmax)

    def set_vmin(self, neuron_index, vmin):
        return liblif.lif_network_set_vmin(self.obj, neuron_index, vmin)

    def potential(self, neuron_index):
        return liblif.lif_network_potential(self.obj, neuron_index)

    def spike_count(self, neuron_index):
        return liblif.lif_network_spike_count(self.obj, neuron_index)

    def spike_rate(self, neuron_index):
        return liblif.lif_network_spike_rate(self.obj, neuron_index)

    def set_num_threads(self, num_threads):
        return liblif.lif_network_set_num_threads(self.obj, num_threads)

class ilifnet(object):
    def __init__(self, par, con):
        #liblif.ilif_network_new.argtypes = None
        liblif.ilif_network_new.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        liblif.ilif_network_new.restype = ctypes.c_void_p

        liblif.ilif_network_num_neurons.argtypes = [ctypes.c_void_p]
        liblif.ilif_network_num_neurons.restype = ctypes.c_int

        liblif.ilif_network_send_synapse.argtypes = [ctypes.c_void_p]
        liblif.ilif_network_send_synapse.restype = ctypes.c_void_p

        liblif.ilif_network_set_biascurrent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        liblif.ilif_network_set_biascurrent.restype = ctypes.c_int

        liblif.ilif_network_set_neuron.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        liblif.ilif_network_set_neuron.restype = ctypes.c_int

        liblif.ilif_network_set_weight.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        liblif.ilif_network_set_weight.restype = ctypes.c_int

        liblif.ilif_network_set_vmax.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        liblif.ilif_network_set_vmax.restype = ctypes.c_int

        liblif.ilif_network_set_vmin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        liblif.ilif_network_set_vmin.restype = ctypes.c_int

        liblif.ilif_network_potential.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.ilif_network_potential.restype = ctypes.c_int

        liblif.ilif_network_spike_count.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.ilif_network_spike_count.restype = ctypes.c_int

        liblif.ilif_network_spike_rate.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.ilif_network_spike_rate.restype = ctypes.c_float

        liblif.ilif_network_set_num_threads.argtypes = [ctypes.c_void_p, ctypes.c_int]
        liblif.ilif_network_set_num_threads.restype = ctypes.c_void_p

        b_par = par.encode('utf-8')
        b_con = con.encode('utf-8')
        self.obj = liblif.ilif_network_new(b_par, b_con)

    def num_neurons(self):
        return liblif.ilif_network_num_neurons(self.obj)

    def send_synapse(self):
        return liblif.ilif_network_send_synapse(self.obj)

    def set_biascurrent(self, neuron_index, biascurrent):
        return liblif.ilif_network_set_biascurrent(self.obj, neuron_index, biascurrent)

    def set_neuron(self, neuron_index, inv_g, rest, threshold, reset, noise):
        return liblif.ilif_network_set_neuron(self.obj, neuron_index, inv_g, rest, threshold, reset, noise)

    def set_weight(self, pre, post, weight, tau):
        return liblif.ilif_network_set_weight(self.obj, pre, post, weight, tau)

    def set_vmax(self, neuron_index, vmax):
        return liblif.ilif_network_set_vmax(self.obj, neuron_index, vmax)

    def set_vmin(self, neuron_index, vmin):
        return liblif.ilif_network_set_vmin(self.obj, neuron_index, vmin)

    def potential(self, neuron_index):
        return liblif.ilif_network_potential(self.obj, neuron_index)

    def spike_count(self, neuron_index):
        return liblif.ilif_network_spike_count(self.obj, neuron_index)

    def spike_rate(self, neuron_index):
        return liblif.ilif_network_spike_rate(self.obj, neuron_index)

    def set_num_threads(self, num_threads):
        return liblif.ilif_network_set_num_threads(self.obj, num_threads)


