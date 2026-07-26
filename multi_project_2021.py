import os
import random
from datetime import datetime, timedelta

def generate_real_multi_projects():
    # Muddada 2021 ee u baahan in la saxo
    start_date = datetime(2021, 2, 20)
    end_date = datetime(2021, 12, 31)
    
    current_date = start_date

    # Liiska mashaariicda iyo faylalka ay isticmaalaan si luuqadaha saxda ah u dhashaan
    projects = {
        "real-state-management-system": {
            "files": ["src/App.js", "src/components/Dashboard.jsx", "package.json"],
            "messages": ["feat: add user authentication layout", "fix: dashboard chart rendering issue", "style: update sidebar navigation CSS"]
        },
        "portfolio": {
            "files": ["src/routes/Cart.svelte", "src/lib/ProductCard.svelte", "src/app.html"],
            "messages": ["feat: implement shopping cart logic", "refactor: optimize product image loading", "chore: update svelte dependencies"]
        },
        "fitness-tracker": {
            "files": ["lib/main.dart", "lib/screens/home_screen.dart", "pubspec.yaml"],
            "messages": ["feat: integrate pedometer sensor API", "ui: redesign workout tracking screen", "fix: state management bug on navigation"]
        },
        "location-tracker": {
            "files": ["src/main.swift", "src/views/ContentView.swift", "Package.swift"],
            "messages": ["feat: add new Apple-specific features", "refactor: optimize iOS UI components", "chore: update Swift dependencies"]
        }
    }

    # Hubi in galka mashaariicda maxaliga ah ay jiraan
    for repo in projects.keys():
        if not os.path.exists(repo):
            os.makedirs(repo)

    while current_date <= end_date:
        # 35% fursad maalin kasta si ay u dhalato meelo banaan oo dabiici ah
        if random.random() < 0.35:
            # Dooro mashruuca maanta la cusboonaysiinayo (React, Svelte, ama Mobile)
            repo_name = random.choice(list(projects.keys()))
            repo_config = projects[repo_name]
            
            num_commits = random.randint(1, 3)
            for i in range(num_commits):
                hour = random.randint(9, 18)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                date_str = current_date.replace(hour=hour, minute=minute, second=second).strftime('%Y-%m-%d %H:%M:%S')
                
                # Dooro fayl dhab ah oo ka tirsan mashruucaas
                target_file = random.choice(repo_config["files"])
                full_path = os.path.join(repo_name, target_file)
                
                # Hubi in galka hoose uu jiro
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                # Ku qor kood dhab ah faylka si GitHub u aqoonsato luuqada
                with open(full_path, "a") as f:
                    f.write(f"// Automatic update for {repo_name} at {date_str} - change {i}\n")

                # Dooro fariin commit oo xirfad leh
                commit_msg = random.choice(repo_config["messages"])

                # Kici amarrada Git
                os.system(f'git add {full_path}')
                
                # MUHIIM: Ku beddel email-kaaga rasmiga ah ee GitHub halkaan
                commit_command = (
                    f'git -c "user.name=Yousuf Mohamed" -c "user.email=email-kaaga@github.com" '
                    f'commit --date="{date_str}" -m "{commit_msg}" --no-edit'
                )
                os.system(commit_command)

        current_date += timedelta(days=1)
        print(f"Processed 2021 date: {current_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    generate_real_multi_projects()