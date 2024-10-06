# update_readme.py
import os
from github import Github

# Fetch GitHub credentials from environment variables
ACCESS_TOKEN = os.environ['INPUT_ACCESS_TOKEN']
REPO_NAME = os.environ['INPUT_REPO_NAME']

# Initialize GitHub instance
g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)

# Fetch contributors
contributors = repo.get_contributors()
contributor_list = []

for contributor in contributors:
    contributor_list.append(f"- [{contributor.login}](https://github.com/{contributor.login})")

# Update README.md
readme_path = "README.md"  # Adjust this if the file is in a subdirectory
with open(readme_path, "r") as file:
    content = file.readlines()

# Find the line to update
for index, line in enumerate(content):
    if "## Contributors" in line:  # Make sure this matches your README section
        start_index = index + 1
        break

# Replace old contributors with the new list
content[start_index:] = [f"{line}\n" for line in contributor_list]

# Write back to README.md
with open(readme_path, "w") as file:
    file.writelines(content)
