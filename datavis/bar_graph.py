import matplotlib.pyplot as plt
import numpy as np

plt.gcf().subplots_adjust(bottom=0.2)


def bar_graph(dataset: dict, ylabel=None, title=None):
    y_pos = np.arange(len(dataset.keys()))
    plt.bar(y_pos, dataset.values(), align='center', alpha=0.5)
    plt.xticks(y_pos, dataset.keys(), rotation='vertical')
    plt.ylabel(ylabel)
    plt.title(title)
