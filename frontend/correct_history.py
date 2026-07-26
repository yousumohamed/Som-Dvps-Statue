import os
import random
from datetime import datetime, timedelta

def generate_natural_history():
    # Target range: 25 Feb 2020 to 30 Dec 2024
    start_date = datetime(2020, 2, 25)
    end_date = datetime(2024, 12, 30)
    
    current_date = start_date
    filename = "correct_activity.txt"

    while current_date <= end_date:
        year = current_date.year
        
        # 1. Custom Year Rules for spacing and colors
        if year in [2020, 2021]:
            # More empty spaces (45% chance of committing) and light green (1-3 commits)
            chance = 0.45
            num_commits = random.randint(1, 3)
        elif year == 2022:
            # Medium consistency
            chance = 0.70
            num_commits = random.randint(2, 6)
        elif year == 2023:
            # Little green, light green, and small spaces (60% chance, 1-3 commits)
            chance = 0.60
            num_commits = random.randint(1, 3)
        else: # 2024
            # Highly active, dense dark green
            chance = 0.85
            num_commits = random.randint(5, 12)

        # 2. Execute commits if the probability matches
        if random.random() < chance:
            for i in range(num_commits):
                hour = random.randint(9, 17)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                # Format exactly as Git requires: YYYY-MM-DD HH:MM:SS
                date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')

                # Write text to ensure code additions register
                with open(filename, "a") as f:
                    f.write(f"Contribution log entry {date_str} - task {i}\n")

                # Stage the file changes
                os.system(f'git add {filename}')
                
                # FIX: Pass the environment variables directly into the command string line so Git registers them
                commit_command = (
                    f'git -c "user.name=yousumohamed" -c "user.email=yousufmoha255@gmail.com" '
                    f'commit --date="{date_str}" '
                    f'-m "feat: update contribution log {current_date.strftime("%Y-%m-%d")}" --no-edit'
                )
                os.system(commit_command)

        current_date += timedelta(days=1)
        print(f"Generated commits for {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    generate_natural_history()