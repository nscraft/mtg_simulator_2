import json


class WritePlayer:
    def __init__(self, singleton_mtg_sim):
        self.data = singleton_mtg_sim.data
        self.observers = singleton_mtg_sim.observers

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
        for each in self.observers:
            each.notify('players.json')

    def remove_player(self, player_name):
        for each in self.observers:
            each.notify('players.json')
        pass

    def update_player(self, player_name, *args):
        for each in self.observers:
            each.notify('players.json')
        pass
