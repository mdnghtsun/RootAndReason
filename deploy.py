#!/usr/bin/env python3
import os
import subprocess
import sys

def run(cmd, check=True):
    print(f"→ {' '.join(cmd)}")
    subprocess.run(cmd, check=check)

if len(sys.argv) != 2:
    print("Usage: python3 deploy.py 'commit message'")
    sys.exit(1)

commit_msg = sys.argv[1]

# Step 1: Build the site
run(["hugo", "--cleanDestinationDir"])

# Step 2: Move into the public directory
os.chdir("public")

# Step 3: Initialize git if not already a repo
if not os.path.exists(".git"):
    run(["git", "init"])
    run(["git", "checkout", "-b", "gh-pages"])
    run(["git", "remote", "add", "origin", "git@github.com:mdnghtsun/RootAndReason.git"])
else:
    # Step 4: Make sure we're on gh-pages branch
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode()
    if branch != "gh-pages":
        branches = subprocess.check_output(["git", "branch"], text=True)
        if "gh-pages" in branches:
            run(["git", "checkout", "gh-pages"])
        else:
            run(["git", "checkout", "-b", "gh-pages"])

# Step 5: Commit and push
run(["git", "add", "-A"])
run(["git", "commit", "-m", commit_msg])
run(["git", "push", "-f", "origin", "gh-pages"])
