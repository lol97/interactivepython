"""
	Code for updated graph
	the data was generated by data.csv
	learn from youtube/sentdex
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
	pullData = open('data.csv', 'r').read()
	print(pullData)
	dataArray = pullData.split('\n')
	xar = []
	yar = []
	for line in dataArray:
		if len(line) > 1 :
			x, y = line.split(',')
			xar.append(int(x))
			yar.append(int(y))

	ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()