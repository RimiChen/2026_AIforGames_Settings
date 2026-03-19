# 2026_AIforGames_Settings

# 📦 AI for Games — Environment Setup (Assignment 1)

This guide will help you set up the Python environment required for Assignment 1.

---

## 🧰 Requirements

* Install **Anaconda** or **Miniconda**
* A code editor (recommended: VS Code or PyCharm)

---

## 🐍 Check Your Python Version

Open a terminal (Anaconda Prompt on Windows) and run:

```bash
python --version
```

You should use **Python 3.11** for this course.

---

## ⚙️ Step 1 — Create the Environment

Run the following command:

```bash
conda create -p D:\CondaEnv\AI_for_Games-py311 python=3.11 -y
```

📌 **Important:**

* You can replace `D:\CondaEnv\AI_for_Games-py311` with your own preferred path
* Example:

  ```bash
  conda create -p C:\Users\YourName\envs\ai-games python=3.11 -y
  ```

---

## ▶️ Step 2 — Activate the Environment

```bash
conda activate D:\CondaEnv\AI_for_Games-py311
```

📌 Again, replace the path if you used a different one.

---

## 📦 Step 3 — Install pygame

Try this first:

```bash
conda install -c conda-forge pygame -y
```

If that does not work, use:

```bash
pip install pygame
```

---

## ✅ Step 4 — Test Your Setup

Run:

```bash
python EnvTest.py
```

If a game window opens, your setup is successful.

---

## ⚠️ Notes on Warnings

You may see messages like:

* AVX2 warnings
* `pkg_resources` deprecation warnings

👉 These are **normal and safe to ignore**.
They do **not affect your assignment**.

---

## 🧪 Troubleshooting

### ❌ `conda` not recognized

* Make sure you are using **Anaconda Prompt**
* Or reinstall Anaconda/Miniconda

---

### ❌ Environment not activated

Make sure your prompt shows something like:

```bash
(D:\CondaEnv\AI_for_Games-py311)
```

---

### ❌ pygame window does not open

* Ensure installation succeeded
* Try reinstalling:

```bash
pip install pygame --upgrade
```

---

## 📌 Policy

* You are encouraged to use this environment to avoid compatibility issues
* You may use your own setup, but **you are responsible for ensuring your code runs correctly**

---

## 🚀 Next Step

Once your environment is ready:

👉 Proceed to run the provided starter code for Assignment 1.

---

## 👍 Instructor Note (Optional)

If you encounter setup issues, please first check this document carefully and search online.
Implementation/debugging issues are expected to be handled independently for this course.
