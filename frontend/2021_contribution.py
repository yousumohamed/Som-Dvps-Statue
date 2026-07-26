import os
import random
from datetime import datetime, timedelta

def fill_rest_of_2021():
    # Waxaan ka bilaabaynaa halkii sawirkaaga ku ekaa (Febraayo 20, 2021) ilaa dhammaadka sanadka
    start_date = datetime(2021, 2, 20)
    end_date = datetime(2021, 12, 31)
    
    current_date = start_date
    filename = "activity_2021.txt"

    while current_date <= end_date:
        # Fursad 35% ah si ay u dhalato meelo banaan (empty spaces) oo dabiici ah
        if random.random() < 0.35:
            # 1 ilaa 4 commits maalinkii si ay u noqoto cagaar khafiif ah (light green) iyo mid dhex-dhexaad ah
            num_commits = random.randint(1, 4)
            
            for i in range(num_commits):
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                # Habaynta taariikhda Git
                date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')

                # Ku qorista file-ka si ay line additions u xisaabsoonto
                with open(filename, "a") as f:
                    f.write(f"Filling 2021 gap: {date_str} - entry {i}\n")

                os.system(f'git add {filename}')
                
                # MUHIIM: Ku bedel email-kaaga rasmiga ah ee GitHub halkaan
                commit_command = (
                    f'git -c "user.name=Yousuf Mohamed" -c "user.email=yousufmoha255@gmail.com" '
                    f'commit --date="{date_str}" '
                    f'-m "style: patch contribution updates {current_date.strftime("%Y-%m-%d")}" --no-edit'
                )
                os.system(commit_command)

        current_date += timedelta(days=1)
        print(f"Processed date: {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    fill_rest_of_2021()