import os
import requests
import re

REPO = os.getenv("GITHUB_REPOSITORY")
TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = f"https://api.github.repos/{REPO}/issues"

headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def get_existing_issues():
    response = requests.get(API_URL, headers=headers, params={"state":"open"})
    
    return [issue["title"] for issue in response.json()]

def create_issue(title, body, filepath, line_num):
    print(f"Creating issue: {title}")
    data = {
        "title": title,
        "body": f"Found in `{filepath}` at line `{line_num}\n{body}",
        "labels": ["todone"]
    }
    
    requests.post(API_URL, headers=headers, json=data)

def scan_files():
    existing_titles = get_existing_issues()
    todo_pattern = re.compile(r'(#|//)\s*TODO:\s*(.*)')

    for root, dirs, files in os.walk("."):
        if ".git" in root or "node_modules" in root:
            continue
        
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".cs", ".java", ".cpp", ".c", ".rs", ".cpp", ".rb")):
                filepath = os.path.join(root, file)

                with open(filepath, "r", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        match = todo_pattern.search(line)
                        if match:
                            todo_message = match.group(2).strip()
                            title = f"[TD] {todo_message}"

                            if title not in existing_titles:
                                create_issue(title, todo_message, filepath, line_num)

if __name__ == "__main__":
    scan_files()