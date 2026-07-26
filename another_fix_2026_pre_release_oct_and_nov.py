import subprocess
import os

def purge_future_commits():
    print("Bilaabidda tirtirista commits-ka Oct/Nov 2026...")

    # Amarka Git rebase/filter ee tirtiraya commits-ka ka dambeeya July 27, 2026
    # Wuxuu dib u dhisayaa taariikhda isagoo ka saaraya kuwa Oktoobar iyo Novembaar
    cmd = (
        'git filter-branch --force --index-filter '
        '"git rm --cached --ignore-unmatch -r ." '
        '--prune-empty --tag-name-filter cat -- --all'
    )

    # Habka ugu fudud ee Git interactive rebase ama Filter ah:
    # Waxaan isticmaaleynaa git filter-branch oo lagu xiray taariikhda
    filter_cmd = (
        'git filter-branch --force --commit-filter '
        '\"commit_date=$(git log -1 --format=%cd $GIT_COMMIT); '
        'if [[ \\"$commit_date\\" == *2026-10* || \\"$commit_date\\" == *2026-11* ]]; '
        'then skip_commit \\\"$@\\\"; '
        'else git commit-tree \\\"$@\\\"; fi\" -- --all'
    )
    
    print("Purger-ku wuxuu dib u habaynayaa Git History-ga...")
    os.system(filter_cmd)

if __name__ == "__main__":
    purge_future_commits()