from BRScraper import nba
# All players stats per game regular season
print(nba.get_stats(2024, info='per_game', playoffs=False, rename=False)
