import matplotlib.pyplot as plt
import numpy as np
def plot(xpoints,ypoints,filename,title):
	plt.plot(xpoints,ypoints)
	plt.xlabel('N')
	plt.ylabel('ave_order')
	plt.title(title)
	plt.savefig('plot/'+filename)
	plt.show()