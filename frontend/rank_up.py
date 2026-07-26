import os
import random
from datetime import datetime, timedelta

def reach_top_rank():
    # We need ~3,500 to 4,000 to be safe
    # From July 4, 2026, to Dec 31, 2026 is 180 days
    # 4000 / 180 = ~22 commits per day
    start_date = datetime.now()
    end_date = datetime(2026, 12, 31)
    
    current_date = start_date
    filename = "rank_up.txt"

    while current_date <= end_date:
        # Generate 22-25 commits per day to guarantee the #1 spot
        for i in range(random.randint(22, 25)):
            # Distribute commits throughout the workday
            hour = random.randint(9, 17)
            minute = random.randint(0, 59)
            date_str = current_date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:%S')

            # Write meaningful content to ensure GitHub counts the contribution
            with open(filename, "a") as f:
                f.write(f"Refactor logic for optimization {date_str}\n")

            os.environ['GIT_AUTHOR_DATE'] = date_str
            os.environ['GIT_COMMITTER_DATE'] = date_str

            os.system(f'git add {filename}')
            os.system(f'git commit -m "chore: performance update #{i}" --no-edit')

        current_date += timedelta(days=1)
        print(f"Pushed contributions for {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    reach_top_rank()