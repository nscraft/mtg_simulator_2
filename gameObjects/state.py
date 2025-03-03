class GameState:
    def __init__(self, kind: str, players: list):
        self.kind = kind  # 'commander' or 'standard'
        self.players = []
        self.num_players = len(self.players)
        assert self.num_players > 0, 'Not enough players'
        self.turn_structure = {
            'Untap Step': 'Beginning Phase',
            'Upkeep Step': 'Beginning Phase',
            'Draw Step': 'Beginning Phase',
            'Main Phase': ['Pre-combat Main Phase', 'Post-combat Main Phase'],
            'Beginning of Combat Step': 'Combat Phase',
            'Declare Attackers Step': 'Combat Phase',
            'Declare Blockers Step': 'Combat Phase',
            'Combat Damage Step': 'Combat Phase',
            'End of Combat Step': 'Combat Phase',
            'End Step': 'Ending Phase',
            'Cleanup Step': 'Ending Phase',
        }
        self.phase = str
        self.step = str

    def players_playing(self):
        if self.num_players == 0:
            print("0 players in game")
            return False
        else:
            return True

    def remove_player(self, player):
        self.players.remove(player)
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
        else:
            self.step = list(self.turn_structure.keys())[step_index + 1]
        # set self.phase to the value of the self.step key in the turn_structure
        # if the step is 'Main Phase', set self.phase to the next value in the list
        if self.step == 'Main Phase':
            self.phase = self.turn_structure[self.step][+1]
        else:
            self.phase = self.turn_structure[self.step]

