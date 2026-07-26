import os
import random
from datetime import datetime, timedelta

def generate_natural_history():
    start_date = datetime(2020, 2, 25)
    end_date = datetime(2024, 12, 30)
    current_date = start_date
    filename = "contribution_history.txt"

    while current_date <= end_date:
        year = current_date.year
        
        # Determine "intensity" based on the year
        if year <= 2021:
            # Sparse: 50% chance of a few commits, high chance of empty
            chance = 0.5
            num_commits = random.randint(0, 3)
        elif year == 2022:
            # Medium: More consistent, mix of light/dark green
            chance = 0.7
            num_commits = random.randint(1, 5)
        elif year == 2023:
            # Light/Sparse: Similar to 2020 but slightly more active
            chance = 0.6
            num_commits = random.randint(1, 3)
        else: # 2024
            # Dense: High activity leading to current date
            chance = 0.9
            num_commits = random.randint(3, 10)

        # Apply logic
        if random.random() < chance:
            for i in range(num_commits):
                hour = random.randint(9, 17)
                minute = random.randint(0, 59)
                date_str = current_date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:%S')

                with open(filename, "a") as f:
                    f.write(f"Commit on {date_str}\n")

                os.environ['GIT_AUTHOR_DATE'] = date_str
                os.environ['GIT_COMMITTER_DATE'] = date_str
                
                os.system(f'git add {filename}')
                os.system(f'git commit -m "update history {date_str}" --no-edit')

        current_date += timedelta(days=1)
        print(f"Processed: {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    generate_natural_history()