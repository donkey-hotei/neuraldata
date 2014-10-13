import numpy as np 
import matplotlib.pyplot as pyplot

def create_waveform(times, data):
	plt.plot(times, data, '-g')
	plt.title("Waveform")
	return plt

def add_line()