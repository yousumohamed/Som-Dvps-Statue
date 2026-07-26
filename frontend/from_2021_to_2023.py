import os
import random
from datetime import datetime, timedelta

def generate_natural_history():
    # Taariikhda aad codsatay: 19 Feb 2021 ilaa 30 Dec 2023
    start_date = datetime(2021, 2, 19)
    end_date = datetime(2023, 12, 30)
    
    current_date = start_date
    filename = "natural2_activity.txt"

    while current_date <= end_date:
        month = current_date.month
        
        # Sida sawirka ka muuqda: Janaayo ilaa Juun waa degan tahay (meelo badan banaan iyo light green)
        if 1 <= month <= 6:
            chance = 0.35  # 35% fursad in maalinkas commit la sameeyo (banaano badan)
            num_commits = random.randint(1, 3) # Commits yar (Light Green)
            
        # Luulyo ilaa Diseembar waa mashquul aad u cagaaran (Sida sawirka dambe)
        else:
            chance = 0.85  # 85% fursad maalin kasta (Aad u cagaaran)
            num_commits = random.randint(5, 12) # Commits badan (Dark Green)

        # Meelmarinta commits-ka haddii fursadu timaado
        if random.random() < chance:
            for i in range(num_commits):
                hour = random.randint(9, 17)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                # Qaabka Git u akhriyo taariikhda
                date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')

                # Ku qoritaan file-ka si ay line additions u noqoto
                with open(filename, "a") as f:
                    f.write(f"Natural contribution entry {date_str} - task {i}\n")

                os.system(f'git add {filename}')
                
                # MUHIIM: Halkaan ku bedel "email-kaaga@github.com" kanaga rasmiga ah
                commit_command = (
                    f'git -c "user.name=Yousuf Mohamed" -c "user.email=yousufmoha255@gmail.com" '
                    f'commit --date="{date_str}" '
                    f'-m "feat: update contribution log {current_date.strftime("%Y-%m-%d")}" --no-edit'
                )
                os.system(commit_command)

        current_date += timedelta(days=1)
        print(f"Generated commits for {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    generate_natural_history()