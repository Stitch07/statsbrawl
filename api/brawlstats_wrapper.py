import brawlstats
import numpy as np


class API:
    def __init__(self, token: str):
        self.client = brawlstats.Client(token, is_async=True)

    async def brawler_stats(self, limit=50, _type='mean', cb=lambda: None):
        brawlers = {}
        all_brawlers = [
            'shelly', 'nita', 'colt', 'bull', 'jessie',  # league reward 0-500
            'brock', 'dynamike', 'bo',                   # league reward 1000+
            'el primo', 'barley', 'poco', 'rosa',        # rare
            'penny', 'darryl', 'carl',                   # super rare
            'frank', 'pam', 'piper',                     # epic
            'mortis', 'tara', 'gene',                    # mythic
            'spike', 'crow', 'leon'                      # legendary
        ]
        for brawler in all_brawlers:
            lb = await self.client.get_leaderboard(brawler, count=limit)
            trophies = list(map(lambda b: b.trophies, lb))
            val = np.mean(trophies) if _type == 'mean' else np.max(trophies)
            brawlers[brawler] = val
            cb()
        return brawlers

    async def top_brawlers(self, limit=50, cb=lambda: None):
        brawlers = {}
        top_players = await self.client.get_leaderboard('players', count=limit)
        for player in top_players:
            try:
                full_profile = await self.client.get_profile(player.tag)
                cb()
                for brawler in full_profile.brawlers:
                    if brawler.name in brawlers:
                        brawlers[brawler.name] += brawler.trophies
                    else:
                        brawlers[brawler.name] = brawler.trophies
            except TimeoutError:
                continue
        return brawlers
