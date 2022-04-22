import matplotlib.pyplot as plt
import numpy as np


def reject_outliers(data, m=2):
    if m is None:
        return data

    return data[abs(data - np.mean(data)) < m * np.std(data)]


class Histogram:
    def __init__(self, data_list, outlier_m=2):
        self.data_list = data_list
        self.outlier_m = outlier_m

    def show(self):
        x = np.array(self.data_list)
        x = reject_outliers(x, self.outlier_m)
        result = plt.hist(x, bins=20, color='c', edgecolor='k', alpha=0.65)
        plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)

        min_ylim, max_ylim = plt.ylim()
        plt.text(x.mean() * 1.1, max_ylim * 0.9, 'Mean: {:.2f}'.format(x.mean()))
        plt.show()
