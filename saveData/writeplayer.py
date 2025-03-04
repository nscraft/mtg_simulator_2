import json


class WritePlayer:
    def __init__(self, data):
        self.data = data

    def add_player(self, player_name: str):
        # todo: add option to set multiple values for player
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

    def remove_player(self, player_name):
        for player in self.data['players']:
            if player['name'] == player_name:
                self.data['players'].remove(player)
                player_file_content = {
                    'players': self.data['players']
                }
                with open('data/players.json', 'w') as f:
                    json.dump(player_file_content, f, indent=4)
                return
        print("Player not found.")
        return

    def update_player(self, player_name, new_name):
        pass
