import json


class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, player_name):
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
