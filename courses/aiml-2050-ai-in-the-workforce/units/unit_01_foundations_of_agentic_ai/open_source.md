# Unit 01: Open-Source Guide — Setting Up Python & Environment Verification

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: Python 3.10+, pip, virtual environments (`venv`), Git  
> **Cost**: $0.00 (Zero-cost local infrastructure)

---

## 1. Prerequisites & System Requirements
- **OS**: Windows 10/11, macOS, or Linux.
- **RAM**: Minimum 8 GB (16 GB recommended).
- **Disk Space**: At least 5 GB free.

---

## 2. Step-by-Step Installation Commands

### Windows (PowerShell)
```powershell
# 1. Verify Python installation (Must be 3.10 or higher)
python --version

# 2. Upgrade pip to the latest release
python -m pip install --upgrade pip

# 3. Create an isolated course virtual environment
python -m venv aiml_env

# 4. Activate the virtual environment
.\aiml_env\Scripts\Activate.ps1

# 5. Install foundational data & notebook packages
pip install jupyterlab requests pydantic python-dotenv
```

### macOS / Linux (Bash)
```bash
python3 --version
python3 -m venv aiml_env
source aiml_env/bin/activate
pip install --upgrade pip
pip install jupyterlab requests pydantic python-dotenv
```

---

## 3. 60-Second Smoke Test Verification

Create a file named `test_env.py` and run it:
```python
import sys
import pydantic
import requests

print("=" * 50)
print(f"Python Version:   {sys.version.split()[0]}")
print(f"Pydantic Version: {pydantic.__version__}")
print(f"Requests Version: {requests.__version__}")
print("STATUS: Environment is ready for AIML 2050!")
print("=" * 50)
```

Run:
```powershell
python test_env.py
```
**Expected Output**: Clean output printing package versions and `STATUS: Environment is ready for AIML 2050!`.

---

## 4. Troubleshooting FAQ
1. **Execution Policy Error in PowerShell**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
2. **`python` not recognized**: Ensure you checked *"Add Python to PATH"* during Windows installer setup.
3. **Port collision on Jupyter**: Run `jupyter lab --port 8890`.
