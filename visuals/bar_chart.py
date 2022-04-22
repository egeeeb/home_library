import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as mticker


class BarChart:
    def __init__(self, data_dict, top=None):
        self.data_dict = data_dict
        self.top = top

    def show(self):
        items = list(self.data_dict.items())
        rcParams.update({'figure.autolayout': True})

        if self.top is not None:
            sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
            other_count = 0
            for i in range(self.top, len(sorted_items)):
                other_count = other_count + sorted_items[i][1]

            items = sorted_items[0:self.top]
            items.append(('other', other_count))

        separated_items = list(zip(*items))

        plt.bar(separated_items[0], separated_items[1])
        plt.xticks(rotation='vertical')
        plt.autoscale()
        plt.show()
