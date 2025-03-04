import gameObjects.rules as rules


class GameEvent:
    def __init__(self, game_kind: str, players: dict, data: dict):
        self.game_kind = game_kind
        self.players = players
        # assert all items in list players in data['players']['name']
        assert all(player in [player['name'] for player in data['players']] for player in self.players.values()), \
            'Player not found in data'
        # assert all players have data in data['decks']
        self.data = data
        self.rules = self.get_rules()
        self.gameState = self.init_gameState()

    def get_rules(self):
        if self.game_kind == 'commander':
            return rules.commanderRules().rules
        elif self.game_kind == 'standard':
            return rules.generalRules().rules
        elif self.game_kind == 'gold_fish':
            return rules.generalRules().rules
        else:
            return rules.generalRules().rules
