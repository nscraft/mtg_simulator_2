class GameState:
    def __init__(self, game_kind: str, players: dict):
        """
        :param game_kind: 'commander' or 'standard'
        :param players:
        {
        'player_1': {'name': 'John Doe', 'deck': 'Boros Aggro'},
        'player_2': {'name': 'Jane Doe', 'deck': 'Simic Ramp'}
         }
        """
        self.kind = game_kind
        self.players = players
        self.num_players = len(players)
        assert self.num_players > -1, 'Not enough players'
        self.turn_structure = {
            'Untap Step': 'Beginning Phase',
            'Upkeep Step': 'Beginning Phase',
            'Draw Step': 'Beginning Phase',
            'Pre-combat Main Phase': 'Main Phase',
            'Beginning of Combat Step': 'Combat Phase',
            'Declare Attackers Step': 'Combat Phase',
            'Declare Blockers Step': 'Combat Phase',
            'Combat Damage Step': 'Combat Phase',
            'End of Combat Step': 'Combat Phase',
            'Post-combat Main Phase': 'Main Phase',
            'End Step': 'Ending Phase',
            'Cleanup Step': 'Ending Phase',
        }
        self.phase = str
        self.step = str

    def players_playing(self):
        print(f"{self.num_players} players in game")
        if self.num_players == 0:
            return False
        else:
            return True

    def remove_player_from_game(self, player):
        self.players.pop(player)
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
        step_index = list(self.turn_structure.keys()).index(current_step)
        # set self.step to the next step in the turn_structure
        if current_step == 'Cleanup Step':
            self.step = 'Untap Step'
            self.phase = self.turn_structure[self.step]
        else:
            self.step = list(self.turn_structure.keys())[step_index + 1]
            self.phase = self.turn_structure[self.step]
