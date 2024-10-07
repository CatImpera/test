import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time

for i in range(1000):
	with open('/home/tim314159/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/1.12.2_pipe_input_lua/.minecraft/mods/advancedMacros/macros/turn', 'r') as f:
		line = f.read()
		print(line)
	
