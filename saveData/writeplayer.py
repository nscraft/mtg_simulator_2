import json
from saveData.observer import saveDataObserver


class WritePlayer:
    def __init__(self, data):
        self.data = data

    def add_player(self, player_name: str):
        max_player_id = self.data['players'][-1]['id']
        new_player = {
            'id': max_player_id + 1,
            'name': player_name,
            'decks': [],
            'score': 0
        }
        self.data['players'].append(new_player)
        player_file_content = {
            'players': self.data['players']
        }
        with open('data/players.json', 'w') as f:
            json.dump(player_file_content, f, indent=4)
        saveDataObserver('players.json').notify()

    def remove_player(self, player_name):
        saveDataObserver('players.json').notify()
        pass

    def update_player(self, player_name, *args):
        saveDataObserver('players.json').notify()
        pass
