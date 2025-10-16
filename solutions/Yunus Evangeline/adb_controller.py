# solutions/Yunus Evangeline/adb_controller.py

import subprocess

def run_adb(command):
    full_cmd = f"adb {command}"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def tap(x, y):
    return run_adb(f"shell input tap {x} {y}")

def input_text(text):
    safe_text = text.replace(" ", "%s")
    return run_adb(f"shell input text {safe_text}")

def swipe(x1, y1, x2, y2, duration=300):
    return run_adb(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
