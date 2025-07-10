import subprocess
import sys

def run(cmd, cwd=None):
    print(f"→ {cmd}")
    result = subprocess.run(cmd, cwd=cwd, shell=True)
    if result.returncode != 0:
        print("❌ Command failed. Aborting.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python deploy.py 'Your commit message here'")
        sys.exit(1)

    commit_message = sys.argv[1]

    # Step 1: Build site
    run("hugo --cleanDestinationDir")

    # Step 2: Commit and push public/
    run("git add -A", cwd="public")
    run(f"git commit -m \"{commit_message}\"", cwd="public")
    run("git push -f origin gh-pages", cwd="public")

    print("\n✅ Site deployed to GitHub Pages!")

if __name__ == "__main__":
    main()