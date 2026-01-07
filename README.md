# TODOne

Automatically creates GitHub Issues from TODO comments in your code.

## Quick Installation

Run this command in your project terminal to set up the bot instantly:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/kplunkett05/TODOne/main/install.sh)"
```

Alternatively:

## Manual Installation

Create a file at `.github/workflows/todone.yml` and paste in the following:

```yml
name: TODOne

on:
  push:
    branches: ["main"]

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
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Supported Languages

Support for:
* Python
* JavaScript / TypeScript
* Java
* C
* C++
* C#
* Rust
* Ruby
* Go