# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:29:13 2024

@author: user
"""

# Klass va obyektlar

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu

    def info(self):
        inf = f"{self.model}, RAM: {self.ram}, SSD: {self.hdd}, CPU: {self.cpu}"
        return inf

macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1")
print(macbook.info())
