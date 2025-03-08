import gameObjects.rules as rules
from gameObjects.player import Player
from gameObjects.deck import Deck


class GameEvent:
    def __init__(self, singleton_mtg_sim, game_kind: str, selected_players: dict):
        """
        :param game_kind:
        :param selected_players: example
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
        self.singleton_mtg_sim = singleton_mtg_sim
        self.data = singleton_mtg_sim.data
        self.game_kind = game_kind
        self.rules = self._get_rules()
        self.selected_players = selected_players
        assert all(
            player['name'] in [player_data['name'] for player_data in self.data['players']] for player in selected_players.values())
        self.players = self._get_players()
        self.num_players = len(selected_players)
        assert self.num_players > -1, 'Not enough players to play'
        # pre-first turn setup
        self._set_player_battlefields()
        self.step = list(self.rules['turn_structure'].keys())[0]  # get the first step (key) in the turn_structure dict
        self.phase = self.rules['turn_structure'][self.step]  # accesses the value (phase) for the key (step)
        self.player_with_priority = 'player_1'

    def _get_rules(self) -> dict:
        if self.game_kind == 'commander':
            return rules.CommanderRules().rules
        elif self.game_kind == 'standard':
            return rules.GeneralRules().rules
        elif self.game_kind == 'gold_fish':
            return rules.GeneralRules().rules
        else:
            return rules.GeneralRules().rules

    def _get_players(self) -> list:
        # create a player object for each player in self.players
        player_object_list = []
        for player_num in self.selected_players:
            deck_name = self.selected_players[player_num]['deck']
            deck_data = self.data['decks'][next(
                i for i, deck in enumerate(self.data['decks']) if deck['name'] == deck_name)]
            player_object_list.append(Player(
                player_num=player_num.strip('player_'),
                name=self.selected_players[player_num]['name'],
                life_total=self.rules['starting_life'],
                max_hand_size=self.rules['max_hand_size'],
                deck=Deck(
                    deck_name=deck_name,
                    kind=deck_data['kind'],
                    cards=deck_data['cards'],
                    commander=deck_data.get('commander', None),
                ),
            ))
        return player_object_list

    def _set_player_battlefields(self):
        """
        This is a pre-game setup step that must be called before the first turn begins.
        """
        for player in self.players:
            assert player.turn_num == 0, 'Player has already started their first turn'
            if hasattr(player, 'commander'):
                player.set_commander_to_command_zone()
            player.set_deck_to_library()
            player.shuffle_library()
            player.draw_starting_hand()

    def players_playing(self):
        print(f"{self.num_players} players in game")
        if self.num_players == 0:
            return False
        else:
            return True

    def remove_player_from_game(self, player):
        """
        self.selected_players is a dictionary with keys 'player_1', 'player_2', etc.
            each key in self.selected_players is a dictionary with keys 'name' and 'deck'
        self.players is a list of Player objects
            each Player object has a name attribute
        This method removes the Player object from self.players where player.name == self.selected_players[player]['name']
        self.selected_players is unchanged.
        self.num_players is then updated before calling self.players_playing()
        :param player: a key in self.selected_players
        """
        self.players.remove(
            next(player_obj for player_obj in self.players if player_obj.name == self.selected_players[player]['name'])
        )
        self.num_players = len(self.players)
        self.players_playing()

    def advance_turn(self):
        """
        Step through the turn structure by one step or phase.
        Starting a new turn is a method belonging to the player class.
        When Player.start_turn() called, the player's turn_num attribute is incremented by 1 and GamesState.phase is
         set to 'Beginning Phase'.
        """
        current_phase = self.phase  # example 'Combat Phase'
        current_step = self.step  # example 'Draw Step' (treats 'Main Phase' as a step)

        # find the index of the current step in the turn_structure
        step_index = list(self.rules['turn_structure'].keys()).index(current_step)
        # set self.step to the next step in the turn_structure
        if current_step == 'Cleanup Step':
            self.step = 'Untap Step'
            self.phase = self.rules['turn_structure'][self.step]
        else:
            self.step = list(self.rules['turn_structure'].keys())[step_index + 1]
            self.phase = self.rules['turn_structure'][self.step]

    def pass_priority(self):
        # todo: wip
        # set it to the next player in the players dict
        current_priority_player = self.player_with_priority
        player_list = list(self.players.keys())
        current_index = player_list.index(current_priority_player)
        if current_index == len(player_list) - 1:
            self.player_with_priority = player_list[0]
        else:
            self.player_with_priority = player_list[current_index + 1]
