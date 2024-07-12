import tankgame_utils as tg
from tankgame_utils.color import tgprint

class Tank:
    def __init__(self, name, description, moves, cost):
        self.name = name
        self.description = description
        self.moves = moves
        self.cost = cost


tg.color.manual_reset()
tg.print_title()
tgprint("Loading...", "green", True)

print(tg.load_tanks_from_json("data/tanks.json"))



 