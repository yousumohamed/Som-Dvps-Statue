import os
import random
from datetime import datetime, timedelta

def generate_2026_activity():
    # Define the range
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 7, 3)
    
    current_date = start_date
    filename = "2020_creation_activity.txt"

    while current_date <= end_date:
        # Generate 5-12 commits per day for "Top Contributor" status
        num_commits = random.randint(5, 12)

        for i in range(num_commits):
            # Random time for each commit
            hour = random.randint(9, 17)
            minute = random.randint(0, 59)
            date_str = current_date.replace(hour=hour, minute=minute).strftime('%Y-%m-%dT%H:%M:%S')

            # Write to a file to ensure "Additions" are registered
            with open(filename, "a") as f:
                f.write(f"Contribution entry {current_date} - {i}\n")

            # Set dates
            os.environ['GIT_AUTHOR_DATE'] = date_str
            os.environ['GIT_COMMITTER_DATE'] = date_str

            # Commit
            os.system(f'git add {filename}')
            os.system(f'git commit -m "feat: update contribution log {current_date.strftime("%Y-%m-%d")}" --no-edit')

        current_date += timedelta(days=1)
        print(f"Generated commits for {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    generate_2026_activity()