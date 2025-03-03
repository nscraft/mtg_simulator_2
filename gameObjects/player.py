
class Player:
    def __init__(self, player_num: int, name: str, life_total: int, max_hand_size: int, deck: list):
        self.turn_num = 0
        self.player_num = player_num
        self.name = name
        self.life_total = life_total
        self.max_hand_size = max_hand_size
        self.board = {  # a dictionary of zones. Each zone is a list of cards.
            'command': [],
            'library': [],
            'hand': [],
            'battlefield': [],
            'graveyard': [],
            'exile': [],
            'stack': []
        }
        self.deck = deck  # a list of cards

    def start_turn(self):
        self.turn_num += 1
