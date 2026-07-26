import subprocess
import os

def nuke_future():
    print("Nadiifinta kuwa Oct & Nov 2026...")
    
    # Amarka git rebase ama filter ah oo tirtiraya commits-ka Oct/Nov 2026
    # Sidoo kale wuxuu dib u dhisayaa commit hashes-ka si GitHub u ogaato in uu beddel dhacay
    cmd = (
        'git filter-branch --force --commit-filter '
        '"commit_date=$(git log -1 --format=%cd $GIT_COMMIT); '
        'if [[ \\"$commit_date\\" == *2026-10* || \\"$commit_date\\" == *2026-11* ]]; '
        'then skip_commit \\"$@\\"; '
        'else git commit-tree \\"$@\\"; fi" -- --all'
    )
    
    # Isagoo adeegsanaya ENV variable si looga fogaado warning-ka Windows
    env = os.environ.copy()
    env["FILTER_BRANCH_SQUELCH_WARNING"] = "1"
    
    subprocess.run(cmd, shell=True, env=env)
    print("\nDib u habayntii waa dhameystarantay!")

if __name__ == "__main__":
    nuke_future()