# launcher.py
import os
import sys
import subprocess
import platform
import shutil

# Path to your main script (can contain spaces)
script_path = os.path.abspath("main.py")  # ensures full absolute path

# Terminal size settings
term_cols = 120  # width in characters (approximate)
term_rows = 30   # height in characters (approximate)

def run_in_terminal():
    current_platform = platform.system()

    if current_platform == "Windows":
        # Wrap path in quotes to handle spaces
        cmd = f'start cmd /k "mode con: cols={term_cols} lines={term_rows} & python "{script_path}""'
        os.system(cmd)

    elif current_platform == "Darwin":  # macOS
        # Use AppleScript to open Terminal and run the script
        apple_script = f'''
        tell application "Terminal"
            do script "python3 \\"{script_path}\\""
            set bounds of front window to {{100, 100, {100 + term_cols*8}, {100 + term_rows*20}}}
            activate
        end tell
        '''
        subprocess.run(["osascript", "-e", apple_script])

    elif current_platform == "Linux":
        # Prefer gnome-terminal, fallback to xterm
        if shutil.which("gnome-terminal"):
            cmd = f'gnome-terminal -- bash -c "python3 \\"{script_path}\\"; exec bash"'
        elif shutil.which("xterm"):
            cmd = f'xterm -geometry {term_cols}x{term_rows} -e "python3 \\"{script_path}\\""' 
        else:
            print("No supported terminal emulator found. Run the script manually:")
            print(f'python3 "{script_path}"')
            return
        subprocess.Popen(cmd, shell=True)

    else:
        print(f"Unsupported platform: {current_platform}")

if __name__ == "__main__":
    run_in_terminal()
