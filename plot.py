import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.ticker import FuncFormatter


def plot(xpoints, ypoints1, name1, ypoints2, name2, ypoints3, name3, ylable, filename, title, test_count, test_range,
         is_db):
	def to_db(y):
		return 20 * np.log10(y)

	if is_db == True:
		ypoints1 = to_db(ypoints1)
		ypoints2 = to_db(ypoints2)
		ypoints3 = to_db(ypoints3)
	plt.figure()
	plt.plot(xpoints, ypoints1, marker='o', label=name1)
	plt.plot(xpoints, ypoints2, marker='s', label=name2)
	plt.plot(xpoints, ypoints3, marker='^', label=name3)
	plt.xlabel('N')
	if is_db == True:
		plt.ylabel(ylable + '/dB')
	else:
		plt.ylabel(ylable)
	plt.title(title)
	plt.legend()
	folder_path = f"./plot/test_count={test_count} in {test_range}"
	os.makedirs(folder_path, exist_ok=True)
	plt.savefig(folder_path + '/' + filename)
