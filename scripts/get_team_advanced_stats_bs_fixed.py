import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment
import os

def fetch_player_advanced_stats(start_year=2010, end_year=2023, save_path='data/raw/player_advanced_2010_2023.csv'):
    all_data = []
    for year in range(start_year, end_year + 1):
        print(f"📥 Fetching player advanced stats for season ending {year}...")
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        # The player advanced stats table is usually directly on the page (no comments)
        table = soup.find('table', id='advanced_stats')
        if not table:
            # Sometimes the table is inside comments
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            for comment in comments:
                if 'id="advanced_stats"' in comment:
                    table = BeautifulSoup(comment, 'lxml').find('table', id='advanced_stats')
                    break
        
        if table is None:
            print(f"❌ No player advanced stats table for {year}")
            continue
        
        df = pd.read_html(str(table))[0]

        # Drop repeated header rows that appear inside the table
        df = df[df['Player'] != 'Player']

        # Remove rows where player is missing (if any)
        df = df.dropna(subset=['Player'])

        df['Season'] = f"{year-1}-{str(year)[-2:]}"
        all_data.append(df)

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        combined.to_csv(save_path, index=False)
        print(f"✅ Saved player advanced stats to {save_path}")
    else:
        print("⚠️ No player data fetched.")

if __name__ == "__main__":
    fetch_player_advanced_stats()

