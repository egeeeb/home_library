import matplotlib.pyplot as plt
import numpy as np


class PieChart:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def show(self):
        labels = list(self.data_dict.keys())
        values = list(self.data_dict.values())

        explode = np.zeros((len(values),))
        max_i = np.argmax(values)
        explode[max_i] = 0.1

        fig1, ax1 = plt.subplots()
        ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()
