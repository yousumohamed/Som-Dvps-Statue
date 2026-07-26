import os
import random
from datetime import datetime, timedelta

def fill_gap_2022():
    # Muddada banaan ee 2022: Janaayo 15 ilaa Luulyo 31
    start_date = datetime(2022, 1, 15)
    end_date = datetime(2022, 7, 31)
    
    current_date = start_date
    filename = "2022_activity_2022.txt"

    while current_date <= end_date:
        # Fursad 40% ah si ay u dhalato meelo banaan oo dabiici ah
        if random.random() < 0.40:
            # 1 ilaa 4 commits si uu u bixiyo light green iyo cagaar dhex-dhexaad ah
            num_commits = random.randint(1, 4)
            
            for i in range(num_commits):
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                # Habaynta taariikhda Git u baahan yahay
                date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')

                # Ku qorista file-ka si ay code additions u xisaabsoonto
                with open(filename, "a") as f:
                    f.write(f"Patching 2022 gap: {date_str} - entry {i}\n")

                os.system(f'git add {filename}')
                
                # MUHIIM: Halkaan ku bedel "email-kaaga@github.com" kanaga saxda ah
                commit_command = (
                    f'git -c "user.name=Yousuf Mohamed" -c "user.email=yousufmoha255@gmail.com" '
                    f'commit --date="{date_str}" '
                    f'-m "style: update core configuration {current_date.strftime("%Y-%m-%d")}" --no-edit'
                )
                os.system(commit_command)

        current_date += timedelta(days=1)
        print(f"Processed date: {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    fill_gap_2022()