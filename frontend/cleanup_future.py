import os
from datetime import datetime

def remove_future_commits():
    # Taariikhda maanta (July 26, 2026)
    today = datetime(2026, 7, 26)
    
    print("Bilaabidda baarista commits-ka khaldan...")
    
    # 1. Abuur repo cusub oo lagu sifeynayo taariikhda
    os.system('git filter-branch --force --env-filter "
        commit_date=\$(git log -1 --format=%cd \$GIT_COMMIT)
        if [ \$(date -d \"\$commit_date\" +%s) -gt \$(date -d \"2026-07-27\" +%s) ]; then
            skip_commit=1
        fi
    " --tag-name-filter cat -- --all')

if __name__ == "__main__":
    print("Script-ku wuxuu diyaarinayaa tirtirista kuwa Oktoobar iyo Novembaar...")