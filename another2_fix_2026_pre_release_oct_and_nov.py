import subprocess
import os

def fast_purge():
    print("Nadiifinta unstaged files...")
    os.system("git stash")

    # 1. Helaan commit ID-gii ugu dambeeyay ee ka horreeyay Aug 2026 (Ka hor Oct/Nov)
    cmd = 'git log --before="2026-08-01" -n 1 --format="%H"'
    try:
        clean_commit = subprocess.check_output(cmd, shell=True).decode().strip()
    except Exception as e:
        print("Cilad ayaa dhacday:", e)
        return

    if clean_commit:
        print(f"Commit-ka saxda ah ee bisha July: {clean_commit}")
        
        # 2. Cut-gareey history-ga oo ku ekee commit-kaas
        print("Dib u habaynta history-ga...")
        os.system(f"git reset --hard {clean_commit}")
        
        print("\nSidoo kale u push-gareey GitHub:")
        print("git push origin main --force")
    else:
        print("Lama helin commit taariikhdaas ku habboon.")

if __name__ == "__main__":
    fast_purge()