#!/bin/bash

WORKFLOW_DIR=".github/workflows"
FILE_NAME="$WORKFLOW_DIR/todone.yml"

cat <<EOF > /tmp/todone_temp.yml
name: TODOne

on:
  push:
    branches: ["main", "master"]

permissions:
  contents: read
  issues: write 

jobs:
  todone:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Run TODOne
        uses: kplunkett05/TODOne@v1.0
        env:
          GITHUB_TOKEN: \${{ secrets.GITHUB_TOKEN }}
EOF

if [ ! -d "$WORKFLOW_DIR" ]; then
    echo "Creating directory $WORKFLOW_DIR..."
    mkdir -p "$WORKFLOW_DIR"
fi

mv /tmp/todone_temp.yml "$FILE_NAME"

echo "Successfully installed TODOne to $FILE_NAME"
echo "Commit and push this file to activate the bot"