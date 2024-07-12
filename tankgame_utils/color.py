"""
\e[0;31m	Red
\e[0;32m	Green
\e[0;33m	Yellow
\e[0;34m	Blue
\e[0;35m	Purple
\e[0;36m	Cyan
\e[0;37m	White
"""
def manual_reset():
    print(f"\e[0m")
def tgprint(text, color="white", bold=False, autoreset=True):
    is_bold = int(bold)
    if color == "red":
        print(f"\e[{is_bold};31m{text}")
    elif color == "green":
        print(f"\e[{is_bold};32m{text}")
    elif color == "yellow":
        print(f"\e[{is_bold};33m{text}")
    elif color == "blue":
        print(f"\e[{is_bold};34m{text}")
    elif color == "purple":
        print(f"\e[{is_bold};35m{text}")
    elif color == "cyan":
        print(f"\e[{is_bold};36m{text}")
    elif color == "white":
        print(f"\e[{is_bold};37m{text}")
    if autoreset:
        print("\e[0m")
def print_title():
    fcontent = ""
    with open("title.txt", "r") as f:
        fcontent = f.read()
        f.close()
    print(fcontent)
