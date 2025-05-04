# 🔍 Folder Watcher and Script Trigger

A lightweight Python utility that monitors a specified directory for new files. When new files are detected, it automatically triggers a user-defined Python script. This is ideal for automating data pipelines, batch processing, or handling dropped files in real time.

---

## 📦 Features

- Monitors a directory for newly added files
- Executes a custom Python script on change detection
- Configurable polling interval
- Simple command-line interface
- Cross-platform (Linux, macOS, Windows)

---

## 🛠️ Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

---

## 🚀 Usage

### 1. Clone or copy the script

Save the script as `watch_folder.py`.

### 2. Run the watcher

```bash
python watch_folder.py <watched_dir> <trigger_script> [--interval SECONDS]
