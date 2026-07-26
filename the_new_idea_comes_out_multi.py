import os
import random
from datetime import datetime, timedelta

def generate_independent_repos():
    # Taariikhda 2021 ee la rabo in la patch-gareeyo
    start_date = datetime(2021, 2, 20)
    end_date = datetime(2021, 12, 31)
    
    # 1. Ku bedel halkaan akoonkaaga GitHub (Username-kaaga)
    github_username = "yousumohamed"
    
    # 2. Ku bedel halkaan Email-kaaga rasmiga ah ee GitHub
    github_email = "yousufmoha255@gmail.com"

    # Mashaariicda iyo meelaha ay ku xirmayaan GitHub (Magacyada mashaariicda runta ah)
    projects = {
        "real-state-management-system": {
            "file": "src/App.js",
            "messages": ["feat: add user authentication layout", "fix: dashboard chart rendering issue"]
        },
        "fitness-tracker": {
            "file": "src/routes/Cart.svelte",
            "messages": ["feat: implement shopping cart logic", "chore: update svelte dependencies"]
        },
        "portfolio": {
            "file": "lib/main.dart",
            "messages": ["feat: integrate pedometer sensor API", "ui: redesign workout tracking screen"]
        }
    }

    # Sameynta isbeddelada mid kasta oo ka mid ah mashaariicda
    for repo_name, config in projects.items():
        print(f"\n--- Bilaabidda dhalinta Mashruuca: {repo_name} ---")
        
        # Ka bax galka repo-ga hadda oo banaanka ka samee folder madax-bannaan
        # Tani waxay hubineysaa in mashaariicdu aysan isku dhex jirin
        parent_dir = os.path.dirname(os.getcwd())
        project_path = os.path.join(parent_dir, repo_name)
        
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            
        # Gal folder-ka cusub gudihiisa
        os.chdir(project_path)
        
        # Ka dhig galkaan Git Repository cusub oo madax-bannaan
        os.system("git init")
        os.system("git branch -M main")
        
        # Ku xir Repo-ga u gaarka ah ee aad GitHub ka furatay
        os.system(f"git remote remove origin")
        os.system(f"git remote add origin https://github.com/{github_username}/{repo_name}.git")

        current_date = start_date
        while current_date <= end_date:
            # 35% fursad dabiici ah si ay meelo banaan u reebto
            if random.random() < 0.35:
                num_commits = random.randint(1, 3)
                for i in range(num_commits):
                    hour = random.randint(9, 18)
                    minute = random.randint(0, 59)
                    second = random.randint(0, 59)
                    
                    date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')
                    
                    full_file_path = config["file"]
                    os.makedirs(os.path.dirname(full_path := os.path.join(project_path, full_file_path)), exist_ok=True)
                    
                    with open(full_path, "a") as f:
                        f.write(f"// Professional 2021 contribution update: {date_str}\n")

                    commit_msg = random.choice(config["messages"])

                    # Git status, add iyo commit madax-bannaan
                    os.system(f'git add "{full_file_path}"')
                    
                    commit_command = (
                        f'git -c "user.name=Yousuf Mohamed" -c "user.email={github_email}" '
                        f'commit --date="{date_str}" -m "{commit_msg}" --no-edit'
                    )
                    os.system(commit_command)

            current_date += timedelta(days=1)
        
        # U push-gareey mashruucan u gaarka ah GitHub
        print(f"U raridda {repo_name} dhanka GitHub...")
        os.system("git push -u origin main --force")

if __name__ == "__main__":
    generate_independent_repos()