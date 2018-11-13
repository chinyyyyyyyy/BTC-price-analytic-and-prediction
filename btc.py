import sys
sys.path.append("C:\Users\chinyeiei\Anaconda3\Lib\site-packages\pandas")
import pandas as pd
import numpy as np
import matplotlib as plt

file = open("btcdata.csv","r")

day = []
price = []
for line in file:
    l = line.strip().split(",")
    day.append(l[0])
    price.append(l[1])
print(day)
