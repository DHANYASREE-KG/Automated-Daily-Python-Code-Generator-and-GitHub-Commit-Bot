# 🚀 Automated Daily Python Code Generator and GitHub Commit Bot

An automated, beginner-friendly system that generates clean, educational Python programs every day and commits them to your GitHub repository automatically using **GitHub Actions**.

Runs every day at **9:00 AM Indian Standard Time (IST)** with zero manual intervention, complete duplicate prevention, syntax verification, and dual-mode AI/template generation.

---

## 🌟 Key Features

- **⏰ Automated Daily Execution**: Runs on a scheduled GitHub Actions cron job every morning at **9:00 AM IST** (`30 3 * * *` UTC).
- **🎯 7 Core Topic Categories**:
  - `basics`: Variables, conditions, loops, prime checkers, number patterns.
  - `strings`: Palindromes, anagrams, Caesar ciphers, tokenizers.
  - `lists`: Deduplication, two-sum, matrix rotation, sliding windows.
  - `functions`: Decorators, recursion, memoization, lambda pipelines.
  - `oop`: Classes, encapsulation, polymorphism, inheritance hierarchies.
  - `dsa`: Binary search, merge sort, stacks, queues, linked lists, BST, graphs.
  - `utilities`: Text analyzers, CSV aggregators, password generators, loggers.
- **🤖 Dual-Engine Architecture (AI + Curated Catalog)**:
  - **AI Mode**: Integrates with Google Gemini API (free tier) or OpenAI to generate completely fresh exercises.
  - **Offline Mode**: Includes an offline library of **70 production-ready templates** that automatically takes over if no API key is configured or if network calls time out.
- **🛡️ Duplicate & Safety Guards**:
  - SHA-256 content hashing and filename/title tracking inside `manifest.json`.
  - Static AST inspection ensures no dangerous functions (`eval`, `exec`, `os.system`) are written.
  - Safe path resolution prevents directory traversal.
- **🧪 Built-In Test Suite**: Runs automated syntax checks (`ast.parse`) and unit tests on every run.
- **✨ Safe Commit Automation**: Configured with the official GitHub Actions bot identity, avoids empty commits, and uses `[skip ci]` to prevent infinite workflow loops.

---

## 📂 Repository Structure

```text
daily-python-programs/
├── .github/
│   └── workflows/
│       └── daily_commit.yml          # GitHub Actions workflow (9:00 AM IST daily)
├── generator/
│   ├── __init__.py
│   ├── generate_program.py           # Main CLI orchestrator
│   ├── ai_generator.py               # Gemini/OpenAI API generator with safety filter
│   ├── fallback_templates.py         # Curated catalog of 70+ programs across 7 topics
│   └── manifest_manager.py           # Duplicate detection, SHA-256 hashing & metadata
├── programs/
│   ├── basics/                       # Python fundamentals & mathematical patterns
│   ├── strings/                      # String manipulation & text processing
│   ├── lists/                        # Arrays, matrices & sequence algorithms
│   ├── functions/                    # Decorators, recursion & functional programming
│   ├── oop/                          # Classes, inheritance & design patterns
│   ├── dsa/                          # Data structures & classical algorithms
│   └── utilities/                    # Real-world CLI scripts & data helpers
├── tests/
│   ├── __init__.py
│   └── test_generator.py             # 17 automated unit and integration tests
├── manifest.json                     # JSON registry of generated programs & hashes
├── requirements.txt                  # Python dependencies (requests, pytest)
├── .gitignore                        # Standard Python Git ignore rules
└── README.md                         # Complete project documentation
```

---

## 🛠️ Requirements

- **Python 3.10+** (Python 3.11 or 3.12 recommended)
- **Git** installed on your computer
- A free **GitHub** account

---

## 🚀 Quick Start Guide (Step-by-Step for Windows & VS Code)

### Step 1: Clone or Open the Project in VS Code

1. Open **VS Code**.
2. Open this folder:
   - Click **File** > **Open Folder...**
   - Select the folder containing these files (`python code` or your repository folder).
3. Open a terminal inside VS Code by pressing ``Ctrl + ` `` (Control + Backtick) or selecting **Terminal** > **New Terminal**.

### Step 2: Test the Generator Locally

Run a test run without creating files:

```powershell
python generator/generate_program.py --dry-run
```

Generate your first program locally:

```powershell
python generator/generate_program.py --force
```

Run the built-in test suite (zero third-party dependencies required):

```powershell
python -m unittest discover tests
```

---

## 🐙 Publishing to GitHub

### Step 1: Initialize Git and Commit Your Code

If you haven't initialized a Git repository in this folder yet, run:

```powershell
git init
git add .
git commit -m "feat: initial commit for automated python commit bot"
```

### Step 2: Create a New GitHub Repository

1. Go to [github.com/new](https://github.com/new).
2. Set **Repository name** to `daily-python-programs` (or any name you prefer).
3. Keep it **Public** (or **Private**).
4. **Do NOT** check "Add a README file" or ".gitignore" (we already have them!).
5. Click **Create repository**.

### Step 3: Link Your Local Folder to GitHub and Push

Copy the commands shown on GitHub under "push an existing repository from the command line":

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/daily-python-programs.git
git push -u origin main
```

*(Replace `YOUR_USERNAME` with your actual GitHub username).*

---

## ⚙️ Essential GitHub Actions Configuration

### 1. Enable Workflow Read & Write Permissions (CRITICAL)

By default, GitHub Actions workflows only have read access. You **must** enable write access so the bot can commit new files to your repository:

1. Open your repository on GitHub.
2. Click **Settings** (tab at the top right).
3. In the left sidebar, click **Actions** > **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Check the box **"Allow GitHub Actions to create and approve pull requests"**.
7. Click **Save**.

![GitHub Actions Permissions](https://docs.github.com/assets/cb-32943/mw-1440/images/help/settings/actions-workflow-permissions-read-and-write.webp)

### 2. No API Keys Needed!

This bot is configured to run **100% offline and free** using its curated catalog of 70+ Python practice programs.
- **No API keys or credit cards required**.
- **No secrets to configure in GitHub**.
- The bot handles everything automatically out of the box!

---

## 🧪 How to Trigger the Bot Manually

You don't have to wait until 9:00 AM to test it!

1. Go to your repository on GitHub.
2. Click on the **Actions** tab.
3. In the left sidebar, click **Automated Daily Python Code Generator**.
4. Click the **Run workflow** dropdown button on the right.
5. Select a topic (or leave as `auto`), check `Force new program generation`, and click **Run workflow**.
6. Refresh the page after 30 seconds to see the green checkmark and view the newly committed program!

---

## ⏰ Cron Schedule Details

- **Cron Expression**: `30 3 * * *`
- **Schedule Time**: 03:30 AM UTC
- **IST Time**: 03:30 AM UTC + 5:30 hours = **9:00 AM Indian Standard Time (IST)**

> [!NOTE]
> GitHub Actions schedules run on shared infrastructure. GitHub notes that scheduled workflows may experience slight delays (typically 5 to 15 minutes) during high server load. This is normal GitHub behavior.

---

## 🛠️ CLI Generator Commands

You can run the generator locally at any time:

```powershell
# Automatically picks the next topic in rotation
python generator/generate_program.py

# Generate a specific topic (basics, strings, lists, functions, oop, dsa, utilities)
python generator/generate_program.py --category dsa

# Preview what will be created without modifying files
python generator/generate_program.py --dry-run

# Force creation of a program even if one was already made today
python generator/generate_program.py --force

# Force curated template mode (ignoring AI)
python generator/generate_program.py --source template
```

---

## ❓ Troubleshooting & FAQs

### 1. Error: `Permission to <repo> denied to github-actions[bot]`
- **Cause**: Workflow permissions on GitHub are set to "Read repository contents" only.
- **Solution**: Go to **Settings** > **Actions** > **General** > **Workflow permissions** and select **Read and write permissions**.

### 2. The bot didn't commit anything today
- **Cause**: The bot checks `manifest.json`. If a program was already committed today, it skips committing to prevent accidental spam.
- **Solution**: To generate another program on the same day, trigger manually via **Run workflow** and check `Force new program generation`.

### 3. Will this cost money?
- **No**. GitHub Actions is **free** for public repositories (and includes 2,000 free minutes/month for private repos, of which this bot uses less than 15 minutes per month).
- Google Gemini API has a **free tier** that does not require entering a credit card.
- Even without any API key, the bot uses the built-in library of 70 programs completely free of charge.

---

## 📄 License

This project is licensed under the MIT License - open for study, practice, and personal customization.
