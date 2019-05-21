import json

import matplotlib.pyplot as plt
from docopt import docopt
from progress.bar import ChargingBar

import api
import datavis
import util

doc = """
Usage:
  statsbrawl.py topbrawlers --count=<count> [--out=<file>]
  statsbrawl.py brawlerstats --count=<count> [--out=<file>] --type=<type>
  
statsbrawl is a data visualization CLI tool for Brawl Stars. Statsbrawl has 2 subcommands:
  1) topbrawlers - Generates a bar graph of cumulative trophies of the top <count> players, sorted by brawlers.
  2) brawlerstats - Generates a line graph of the average/max trophies of every brawler, using the brawler's individual leaderboard.
  
The --out flag can be used to write the resultant bar chart to a PNG file.
"""

with open('auth.json', 'r') as f:
    config = json.load(f)
    token = config.get('token')


@util.run_async
async def main():
    args = docopt(doc)
    bs = api.API(token)
    limit = int(args.get('--count'))

    if args.get('topbrawlers') is True:
        bar = ChargingBar(f'Fetching {limit} profiles...', max=limit,  suffix='%(percent).1f%% - %(eta)ds')
        top_brawlers = util.sort_dict(await bs.top_brawlers(limit=limit, cb=lambda: bar.next()))
        datavis.bar_graph(top_brawlers, ylabel='OK', title='Top brawlers in the leaderboard')
        if args.get('--out') is not None:
            plt.savefig(args.get('--out'))
        else:
            plt.show()

    elif args.get('brawlerstats') is True:
        num_brawlers = 24  # TODO: change this when Bibi is added ;)
        _type = args.get('--type')
        if _type not in ['mode', 'mean']:
            print('--type must be either "mode" or "mean"')
            exit(0)
        bar = ChargingBar(f'Getting stats for {num_brawlers} brawlers.',
                          max=num_brawlers, suffix='%(percent).1f%% - %(eta)ds')
        dataset = util.sort_dict(await bs.brawler_stats(limit=limit, cb=lambda: bar.next(), _type=_type))
        datavis.line_graph(dataset)
        plt.show()

    await bs.client.close()
