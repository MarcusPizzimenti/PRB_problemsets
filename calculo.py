#!/usr/bin/env python3
import math
print("Insira o raio: ")
raio = float(input())
area = round(math.pi*raio**2., 3)
perim = round(2*math.pi*raio, 3)
print(area, perim)
