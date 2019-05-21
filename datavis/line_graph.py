import matplotlib.pyplot as plt

plt.gcf().subplots_adjust(bottom=0.2)


def line_graph(dataset: dict, xlabel=None, ylabel=None, title=None):
    brawlers = dataset.keys()
    trophies = dataset.values()
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)  # show brawler names vertically
    ax.plot(brawlers, trophies)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid()
    return fig
