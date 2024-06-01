import matplotlib.pyplot as plt

def plot(xpoints, ypoints1, name1, ypoints2, name2, ypoints3, name3, ylable, filename, title):
	plt.figure()
	plt.plot(xpoints, ypoints1, marker='o', label=name1)
	plt.plot(xpoints, ypoints2, marker='s', label=name2)
	plt.plot(xpoints, ypoints3, marker='^', label=name3)
	plt.xlabel('N')
	plt.ylabel(ylable)
	plt.title(title)
	plt.legend()
	plt.savefig('plot/' + filename)
