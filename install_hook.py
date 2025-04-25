import os
import sys

def get_shell_rc_file():
    shell = os.environ.get("SHELL", "")
    home = os.path.expanduser("~")
    if "zsh" in shell:
        return os.path.join(home, ".zshrc")
    else:
        return os.path.join(home, ".bashrc")

def add_hello_to_rc():
    rc_file = get_shell_rc_file()
    line = 'echo "Hello World"\n'

    try:
        with open(rc_file, "r") as f:
            contents = f.readlines()

        if line in contents:
            print(f"'Hello World' already in {rc_file}")
            return

        with open(rc_file, "a") as f:
            f.write("\n# Added by hello-terminal\n")
            f.write(line)

        print(f"'Hello World' added to {rc_file}")

    except Exception as e:
        print(f"Failed to update {rc_file}: {e}", file=sys.stderr)
