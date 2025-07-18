import subprocess
import os
import shutil

# Config
BUILD_DIR = "public"
DEPLOY_BRANCH = "gh-pages"
COMMIT_MSG = "Deploying site"

def run(cmd, check=True):
    print(f"→ {' '.join(cmd)}")
    subprocess.run(cmd, check=check)

# 1. Build site
run(["hugo", "--cleanDestinationDir"])

# 2. Save current branch name
current_branch = subprocess.check_output(["git", "branch", "--show-current"], text=True).strip()

# 3. Switch to deploy branch
run(["git", "checkout", DEPLOY_BRANCH])

# 4. Copy built files to root
print("→ Copying built site from public/ to repo root...")
for item in os.listdir(BUILD_DIR):
    s = os.path.join(BUILD_DIR, item)
    d = os.path.join(".", item)
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s, d)
    else:
        shutil.copy2(s, d)

# 5. Stage changes
run(["git", "add", "-A"])

# 6. Commit if there are changes
result = subprocess.run(["git", "diff", "--cached", "--quiet"])
if result.returncode == 0:
    print("✔ No changes to commit. Skipping commit.")
else:
    run(["git", "commit", "-m", COMMIT_MSG])

# 7. Push to gh-pages
run(["git", "push", "origin", DEPLOY_BRANCH])

# 8. Switch back to main
run(["git", "checkout", current_branch])
