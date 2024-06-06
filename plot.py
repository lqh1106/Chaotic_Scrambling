import matplotlib.pyplot as plt
import os


def plot(xpoints, ypoints1, name1, ypoints2, name2, ypoints3, name3, ylable, filename, title, test_count, test_range):
	plt.figure()
	plt.plot(xpoints, ypoints1, marker='o', label=name1)
	plt.plot(xpoints, ypoints2, marker='s', label=name2)
	plt.plot(xpoints, ypoints3, marker='^', label=name3)
	plt.xlabel('N')
	plt.ylabel(ylable)
	plt.title(title)
	plt.legend()
	folder_path = "./plot/test_count=" + str(test_count) + ' in ' + str(test_range)
	os.makedirs(folder_path, exist_ok=True)
	plt.savefig(folder_path + '/' + filename)
