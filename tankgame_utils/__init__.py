import json
def print_title():
    fcontent = ""
    with open("tankgame_utils/title.txt", "r") as f:
        fcontent = f.read()
        f.close()
    print(fcontent)
def load_tanks_from_json(filename):
    try:
        content = {}
        with open(filename, "r") as f:
            content = json.load(f)
            f.close()
        return content
    except:
        print("ERROR Loading JSON file")