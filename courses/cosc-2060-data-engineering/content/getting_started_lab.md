# Getting Started with the Lab Environment

Welcome to the hands-on lab environment for **COSC 2060**. In this course, you do not need to install heavy database servers or machine learning libraries on your personal computer. Instead, you will use **GitHub Codespaces**—a free, browser-based cloud workstation pre-loaded with Python 3.11, DuckDB, Polars, OpenCV, FastAPI, and all course datasets.

Follow the steps below to create your personal sandbox repository and run your first script before starting Unit 1.

---

## 1. Creating Your Personal Sandbox Repository

Because you will be writing code and saving your progress throughout the semester, you will start by creating your own private copy of the course sandbox template on GitHub:

1. **Open the Course Template Repository:**
   Go to [**https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox**](https://github.com/tswarmLCCC/COSC-2060-Student-Sandbox) and make sure you are signed in to your free GitHub account.
2. **Use the Template:**
   Click the green **"Use this template"** button near the top-right corner of the page and select **"Create a new repository"**.
3. **Configure Your Repository:**
   - **Repository name:** Enter `COSC-2060-Student-Sandbox-yourname` (for example, `COSC-2060-Student-Sandbox-tswarm`).
   - **Visibility:** Select **Private** so your lab solutions remain private to you.
   - Click **"Create repository"**.
4. **Automatic Button Setup (Wait 5 Seconds):**
   As soon as your repository is created, a built-in GitHub workflow automatically updates the **"Open in GitHub Codespaces"** button on your README page so that it links directly to *your* personal repository. Refresh the page once after 5 seconds.

---

## 2. Launching Your Cloud Workstation in GitHub Codespaces

Once your repository is ready, you can open your cloud workstation directly in your web browser:

1. On your repository homepage, click the **"Open in GitHub Codespaces"** button (or click the green **`<> Code`** button &rarr; select the **Codespaces** tab &rarr; click **"Create codespace on main"**).
2. **First-Time Setup (Takes ~2 Minutes):**
   The first time you launch your Codespace, GitHub builds your Linux container, installs all Python libraries from `requirements.txt` (DuckDB, Polars, PyArrow, OpenCV, FastAPI, Pydantic, pytest), and runs `datasets/seed_all_datasets.py` to generate all course `.parquet` and `.csv` data files.
3. **Resuming Later:**
   Whenever you come back for future units, open your repository on GitHub, click **`<> Code` &rarr; Codespaces**, and click your existing Codespace to resume right where you left off in seconds.

---

## 3. Finding Your Files in the Workspace

When your Codespace finishes loading, you will see Visual Studio Code in your browser with the file Explorer on the left side:

```text
COSC-2060-Student-Sandbox/
├── datasets/                                      # Pre-built .parquet & .csv datasets for all 8 units
│   ├── seed_all_datasets.py                       # Script that generates the course data files
│   ├── unit01_drivers.parquet                     # Unit 1 driver roster
│   ├── unit01_routes.parquet                      # Unit 1 truck dispatch logs
│   ├── unit01_weather.parquet                     # Unit 1 hourly weather observations
│   └── fuel_transactions_1m.parquet               # Unit 2 1-million-row fuel stream
├── units/
│   ├── unit_01_relational_foundations/            # Unit 1 workspace folder
│   │   ├── study_guide.md                         # Reading notes & self-check questions
│   │   ├── ds_to_engine.ipynb                     # Interactive Jupyter Notebook walkthrough
│   │   ├── coding_clinic.py                       # Follow-along practice script (Part 0 to Part 3)
│   │   └── lab1_starter.py                        # Graded Lab 1 starter script
│   ├── unit_02_anomaly_detection_engines/         # Unit 2 workspace folder
│   ...
│   └── unit_08_capstone_defense_and_production/   # Unit 8 workspace folder
└── reset_sandbox.sh                               # Restores datasets if you ever want a fresh start
```

Every unit folder inside `units/` contains the exact same four file types so you always know where to look:

| File Name | What It Is Used For | Graded? |
| :--- | :--- | :---: |
| **`study_guide.md`** | Your unit reading guide, documentation links, and self-check practice questions with expandable answer keys. | Practice |
| **`ds_to_engine.ipynb`** | An interactive Jupyter Notebook that steps through the unit's concepts and code one cell at a time. | Practice |
| **`coding_clinic.py`** | A runnable Python script with warm-up exercises and guided challenges ("Part 0: Warm-Up" through "Part 3: You Do"). | Practice |
| **`labN_starter.py`** | The starter file for your graded lab assignment. You will complete the `TODO` sections in this file and submit it to Canvas. | **Graded (Lab)** |

---

## 4. Running Python Scripts and Jupyter Notebooks

You will use two main ways to run code inside your Codespace:

### A. Running `.py` Scripts in the Terminal
1. Open the integrated terminal at the bottom of VS Code (press `` Ctrl + ` `` or use the top menu: **Terminal &rarr; New Terminal**).
2. Run any script using the `python` command. For example, to run the Unit 1 Coding Clinic:
   ```bash
   python units/unit_01_relational_foundations/coding_clinic.py
   ```
3. To test your Unit 1 Lab Starter script as you work on it:
   ```bash
   python units/unit_01_relational_foundations/lab1_starter.py
   ```

### B. Running Interactive Cells in `ds_to_engine.ipynb`
1. Click `units/unit_01_relational_foundations/ds_to_engine.ipynb` in the left file Explorer.
2. Each notebook is pre-configured to use the **`Python 3.11 (COSC 2060 Sandbox)`** kernel.
3. Click the **Play (`▷`)** button next to any code cell (or press **`Shift + Enter`**) to execute that cell and inspect the output table right below it.

---

## 5. Submitting Your Lab and Resetting Your Sandbox

### How to Submit Your Completed Lab to Canvas
1. After you finish editing and testing `lab1_starter.py` (and confirm it runs with zero errors in the terminal), right-click `lab1_starter.py` in the left VS Code Explorer sidebar and click **"Download..."**.
2. Save the file to your computer and upload it to the **Unit Applied Lab Assignment** page in Canvas.
3. **Save a Backup to Your GitHub Repo:** In the terminal, run these three commands at the end of each work session so your work is safely backed up to your private GitHub repository:
   ```bash
   git add -A
   git commit -m "Save lab progress"
   git push
   ```

### How to Reset Your Datasets if Something Breaks
If you ever accidentally overwrite or delete a file in the `datasets/` folder, you can regenerate all original course datasets in 5 seconds by running this command in the terminal:
```bash
bash reset_sandbox.sh
```

