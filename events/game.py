import gameObjects.rules as rules


class GameEvent:
    def __init__(self, game_kind: str, players: dict, data: dict):
        """
        :param game_kind:
        :param players: example
        {
        'player_1': {'name': 'John Doe', 'deck': 'Boros Aggro'},
        'player_2': {'name': 'Jane Doe', 'deck': 'Simic Ramp'}
         }
        :param data: example
        {
        'players': [
            {'id': 1, 'name': 'John Doe', 'decks': ['Boros Aggro', 'Dimir Control'], "score": 0},
            {'id': 2, 'name': 'Jane Doe', 'decks': ['Simic Ramp', 'Gruul Aggro'], "score": 100}
        ],
        'decks': [
            {'name': 'Boros Aggro', 'cards': ['Card 1', 'Card 2', 'Card 3']},
            {'name': 'Dimir Control', 'cards': ['Card 1', 'Card 2', 'Card 3']},
            {'name': 'Simic Ramp', 'cards': ['Card 1', 'Card 2', 'Card 3']},
            {'name': 'Gruul Aggro', 'cards': ['Card 1', 'Card 2', 'Card 3']}
        ]
        """
        self.game_kind = game_kind
        self.players = players
        # assert all player names are in data['players']
        assert all(player['name'] in [player['name'] for player in data['players']] for player in players.values())
        # assert all decks are in data['decks']
        assert all(deck
                   in [deck['name'] for deck in data['decks']] for deck in [player['deck'] for player in players.values
        ()])
        self.data = data
        self.rules = self.get_rules()
        self.gameState = self.init_gameState()

    def get_rules(self):
        if self.game_kind == 'commander':
            return rules.CommanderRules().rules
        elif self.game_kind == 'standard':
            return rules.GeneralRules().rules
        elif self.game_kind == 'gold_fish':
            return rules.GeneralRules().rules
        else:
            return rules.GeneralRules().rules

    def init_gameState(self):
        pass
