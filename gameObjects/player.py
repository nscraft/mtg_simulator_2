import random


class Player:
    def __init__(self, player_num: int, name: str, life_total: int, max_hand_size: int, deck):
        self.turn_num = 0
        self.player_num = player_num
        self.name = name
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
        self.deck = deck  # a Deck object
        if hasattr(self.deck, 'commander'):
            self.commander = self.deck.commander
        # game setup actions
        self.life_total = life_total
        self.mana_pool = {
            'white': 0,
            'blue': 0,
            'black': 0,
            'red': 0,
            'green': 0,
            'colorless': 0
        }

    def start_turn(self):
        self.turn_num += 1

    def set_commander_to_command_zone(self):
        assert hasattr(self, 'commander'), 'Player does not have a commander'
        self.board['command'].append(self.commander)

    def set_deck_to_library(self):
        card_list = self.deck.cards
        if hasattr(self, 'commander'):
            card_list.remove(self.commander)
        self.board['library'] = card_list

    def shuffle_library(self):
        random.shuffle(self.board['library'])

    def update_card_zone(self, card_name: str, from_zone: str, to_zone: str):
        card = self.board[from_zone].pop(self.board[from_zone].index(card_name))
        self.board[to_zone].append(card)

    def draw_starting_hand(self):
        for _ in range(self.max_hand_size):
            self.update_card_zone(self.board['library'][0], 'library', 'hand')


