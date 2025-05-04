import os
import time
import subprocess
import argparse
import sys

# === Argument Parser ===
parser = argparse.ArgumentParser(description="Monitor a folder and trigger a script on new files.")
parser.add_argument("watched_dir", type=str, help="Path to the folder to monitor.")
parser.add_argument("trigger_script", type=str, help="Python script to run when new files are detected.")
parser.add_argument("--interval", type=int, default=10, help="Polling interval in seconds (default: 10).")
args = parser.parse_args()

WATCHED_DIR = args.watched_dir
TRIGGER_SCRIPT = args.trigger_script
SLEEP_INTERVAL = args.interval

# Validate paths
if not os.path.isdir(WATCHED_DIR):
    print(f"Error: '{WATCHED_DIR}' is not a valid directory.")
    sys.exit(1)

if not os.path.isfile(TRIGGER_SCRIPT):
    print(f"Error: Script '{TRIGGER_SCRIPT}' not found.")
    sys.exit(1)

# Track existing files
seen_files = set(os.listdir(WATCHED_DIR))

def run_trigger_script():
    try:
        print(f"New files detected. Executing: {TRIGGER_SCRIPT}")
        subprocess.run(["python", TRIGGER_SCRIPT], check=True)
        print("Execution completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during script execution: {e}")

def main():
    global seen_files
    print(f"Monitoring '{WATCHED_DIR}' for new files every {SLEEP_INTERVAL} seconds...")

    while True:
        try:
            current_files = set(os.listdir(WATCHED_DIR))
            new_files = current_files - seen_files

            if new_files:
                print(f"New files: {new_files}")
                run_trigger_script()
                seen_files = current_files  # Update file list

            time.sleep(SLEEP_INTERVAL)

        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    main()
