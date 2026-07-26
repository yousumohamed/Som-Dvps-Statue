import os
import random
from datetime import datetime, timedelta

def create_pro_commits():
    # Range for the year 2025
    start_date = datetime(2021, 1, 19)
    end_date = datetime(2024, 12, 31)
    
    current_date = start_date

    while current_date <= end_date:
        # current_date.weekday() returns 0 for Monday and 6 for Sunday
        # We only want Monday (0) through Friday (4)
        if current_date.weekday() < 5:
            # 15% chance of taking a "day off" even on a weekday
            if random.random() > 0.15:
                num_commits = random.randint(3, 8)
            else:
                num_commits = 0
        else:
            # 95% chance of no commits on weekends
            # (leaving 5% for the occasional "overtime" look)
            num_commits = random.randint(0, 1) if random.random() > 0.95 else 0

        for _ in range(num_commits):
            # Strict 9-to-5 window (9 AM to 5 PM)
            hour = random.randint(9, 16) 
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%dT%H:%M:%S')

            os.environ['GIT_AUTHOR_DATE'] = date_str
            os.environ['GIT_COMMITTER_DATE'] = date_str

            # Random commit messages to look more realistic
            messages = ["Update documentation", "Fix bug in controller", "Refactor API logic", "Add unit tests", "Minor tweaks"]
            msg = random.choice(messages)

            os.system(f'git commit --allow-empty -m "{msg}" --no-edit')

        current_date += timedelta(days=1)

    print("Professional 2025 history generated!")

if __name__ == "__main__":
    create_pro_commits()