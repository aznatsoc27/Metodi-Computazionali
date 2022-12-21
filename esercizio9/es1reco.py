import numpy as np

class Hit:
    def __init__ (self, mod, sens, t):
        self.modulo=mod
        self.sensore=sens
        self.tempo=t

    def __lt__ (self, other):
        return self.tempo < other.tempo

    def __sub__ (self, other):
        return self.tempo - other.tempo

class Event:
    def __init__ (self, nhit, tsi, tsf, dt, arrhit):
        self.numhit= nhit
        self.timestampi= tsi
        self.timestampf= tsf
        self.tempo= dt
        self.arrayhit= arrhit

