import json


class WritePlayer:
    def __init__(self, singleton_mtg_sim):
        self.data = singleton_mtg_sim.data
        self.saveDataObserver = singleton_mtg_sim.saveDataObserver

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
        self.saveDataObserver.notify('players.json')

    def remove_player(self, player_name):
        self.saveDataObserver.notify('players.json')
        pass

    def update_player(self, player_name, *args):
        self.saveDataObserver.notify('players.json')
        pass
