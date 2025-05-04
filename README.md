# 🔄 Watch & Trigger: Python Directory Monitor

A robust Python utility that monitors a directory for new or modified files and automatically triggers a specified Python script. Ideal for data pipelines, batch processors, or automated workflows.

---

## ✅ Features

- 🕵️‍♂️ Monitors a folder for file **additions** or **modifications**
- ⚡ Optional **immediate execution** at script startup
- 🕒 Configurable polling interval (default: 10 seconds)
- 🔒 Uses file timestamps for accurate change detection
- 🐍 Lightweight: no third-party dependencies

---

## 🛠 Requirements

- Python 3.6+
- Works on Linux, macOS, and Windows

---

## 🚀 Usage

### Basic command:

```bash
python WaS.py <watched_dir> <trigger_script> [--interval SECONDS] [--trigger-on-startup]
