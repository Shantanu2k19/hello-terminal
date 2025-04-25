import os
import sys

def get_shell_rc_file():
    shell = os.environ.get("SHELL", "")
    home = os.path.expanduser("~")
    if "zsh" in shell:
        return os.path.join(home, ".zshrc")
    else:
        return os.path.join(home, ".bashrc")

def remove_hello_from_rc():
    rc_file = get_shell_rc_file()
    try:
        with open(rc_file, "r") as f:
            lines = f.readlines()
        with open(rc_file, "w") as f:
            for line in lines:
                if "Hello World" not in line and "# Added by hello-terminal" not in line:
                    f.write(line)
        print(f"'Hello World' line removed from {rc_file}")
    except Exception as e:
        print(f"Failed to update {rc_file}: {e}", file=sys.stderr)
