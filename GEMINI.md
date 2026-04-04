# GEMINI.md

## Ownership & Roles
*   **Primary Editor:** The Human (Xing Yang a.k.a. Bill)

## General Instructions

-When running commands in the terminal, (since I use bash (git bash) as my preferred tool when working) always wrap the command as `bash -c "[the actual command]"` when using the `run_shell_command` tool. This ensures consistent execution in the preferred environment and helps identify issues earlier.

-Keep the documentation up to date. Use ".md" files for documentation. Keep the README.md's updated `website/backend` folder and `website/frontend` folder up to date. ALL .md files in this repository are managed by AI and AI alone; the user does not touch them.

-Keep the AGENT_KNOWLEDGE.md file up to date.

## Specific to running commands

-Do not use `&&` to chain commands. Instead, just run the commands one line after the other.

- **Important Bash Syntax Quoting Rules in PowerShell:** The `run_shell_command` tool executes commands via `powershell.exe -NoProfile -Command <command>`. When wrapping commands in `bash -c`, using double quotes (e.g., `bash -c "cat file.txt"`) can cause PowerShell to strip the quotes before passing the argument to Bash. This leads to issues like:
  - Aliases being triggered (e.g., `cat` resolving to `Get-Content` or `rm` resolving to `Remove-Item` with wrong parameter parsing).
  - Variable assignments (e.g., `PYTHONPATH=.`) being misinterpreted as cmdlets.
  - **Solution:** Always use single quotes for the inner bash command string. For example, use `bash -c 'PYTHONPATH=. python script.py'` or `bash -c 'rm file1'` instead of double quotes around the inner command to prevent PowerShell from intercepting the syntax.
  - **File Operations:** When using `rm` or other file operations, prefer using **separate tool calls** for each file to avoid positional parameter errors caused by PowerShell's interpretation of the command string. For example, instead of `bash -c 'rm file1 file2'`, use two separate `run_shell_command` calls.


## Specific to This Workspace

### Run the application 

-I will be running the application using:

```Bash
bash -c 'PYTHONPATH=. ./venv/Scripts/uvicorn.exe website.backend.app:app --host 127.0.0.1 --port 8000'
```

### My Preferences

-Keep the frontend code as simple as possible. Forward all calculations, data, and logic to the backend as post requests.

-When referrencing the links in documentation intended for me to read, always use "http://localhost:..." instead of "http://127.0.0.1:..."

-Keep your own documentation and keep your documentation files updated.

-I'll rerun the application after your code changes (using `bash -c 'PYTHONPATH=. ./venv/Scripts/uvicorn.exe website.backend.app:app --host 127.0.0.1 --port 8000'`), so that within the same session updates can be reflected on the playwright browser tool.

-@Gemini please remember to delete files temporarily created i.e. Playwright screenshots you generated, etc. when they are no longer needed. (-Bill)







