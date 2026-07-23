# CPGit

CPGit is a Git-inspired command-line version control system built specifically for **Competitive Programming**. It enables users to maintain multiple versions of solutions for the same programming problem while providing an intuitive command-line interface similar to Git.

Unlike traditional version control systems, CPGit is tailored for competitive programmers. It stores multiple versions of a solution, tracks metadata, allows algorithm-based tagging, integrates with LeetCode for problem details, and provides AI-powered code review to help identify logical and implementation mistakes.

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/CPGit.git
cd CPGit
```

## 2. Install Apache Cassandra

Download and install Apache Cassandra.

Start the Cassandra server before using the application.

---

## 3. Create the database

Execute the schema file to create the required tables.
Use index file to create indexes on database.

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install the CLI package

Install the project locally.

```bash
pip install -e .
```

After installation, the `cpg` command will be available globally.

---

## 6. Configure Environment Variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

# Available Commands

| Command | Description |
|---------|-------------|
| `cpg help` | Display all available commands |
| `cpg <file> enable` | Enable versioning for a file |
| `cpg <file> disable` | Disable versioning for a file |
| `cpg <file> save` | Save the current file as a new version (only if content has changed) |
| `cpg <file> check` | Check whether versioning is enabled |
| `cpg <file> track` | Display the latest saved version |
| `cpg <file> <version> info` | Show metadata of a specific version |
| `cpg <file> <version> show` | Open a specific version in VS Code |
| `cpg <file> <version> checkout` | Replace the current file with the selected version |
| `cpg <file> <version> add_tags <tag1> <tag2> ...` | Add one or more tags to a version |
| `cpg <file> <version> display` | Display all tags associated with a version |
| `cpg <file> <version> remove <tag1> <tag2> ...` | Remove tags from a version |
| `cpg <file> details` | Fetch problem details from LeetCode (if available) |
| `cpg <file> <version> assist` | Analyze the selected version using an LLM and report possible mistakes |

---
