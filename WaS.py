import os
import time
import subprocess
import argparse
import sys

## TEST2 WaS, Trying 12

def parse_args():
    parser = argparse.ArgumentParser(
        description="Monitor a folder and trigger a script on new or modified files."
    )
    parser.add_argument("watched_dir", type=str, help="Directory to monitor.")
    parser.add_argument("trigger_script", type=str, help="Python script to run on changes.")
    parser.add_argument(
        "--interval", type=int, default=10,
        help="Polling interval in seconds (default: 10)."
    )
    parser.add_argument(
        "--trigger-on-startup", action="store_true",
        help="If set, runs the target script immediately on startup."
    )
    return parser.parse_args()

def get_file_timestamps(path):
    """Return a mapping from filename to last modification time."""
    return {
        f: os.path.getmtime(os.path.join(path, f))
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    }

def run_trigger_script(script_path):
    try:
        print(f"\n▶ Executing: {script_path}")
        subprocess.run(["python", script_path], check=True)
        print("✅ Execution completed.\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during script execution: {e}")

def main():
    args = parse_args()

    if not os.path.isdir(args.watched_dir):
        print(f"Error: '{args.watched_dir}' is not a valid directory.")
        sys.exit(1)

    if not os.path.isfile(args.trigger_script):
        print(f"Error: Script '{args.trigger_script}' not found.")
        sys.exit(1)

    print(f"📂 Monitoring: '{args.watched_dir}' every {args.interval} seconds.")
    if args.trigger_on_startup:
        print("⚡ Triggering script immediately on startup.")
        run_trigger_script(args.trigger_script)

    seen_files = get_file_timestamps(args.watched_dir)

    while True:
        try:
            current_files = get_file_timestamps(args.watched_dir)
            changed_files = {
                f for f in current_files
                if f not in seen_files or current_files[f] != seen_files[f]
            }

            if changed_files:
                print(f"📥 Detected new/modified files: {changed_files}")
                run_trigger_script(args.trigger_script)
                seen_files = current_files  # Update tracking

            time.sleep(args.interval)

        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            time.sleep(args.interval)

if __name__ == "__main__":
    main()



