
class GameState:
    def __init__(self, kind: str, players: list):
        self.kind = kind  # 'commander' or 'standard'
        self.players = []
        self.num_players = len(self.players)
        assert self.num_players > 0, 'Not enough players'
        self.turn_structure = {
            'Phase': ['Beginning Phase',
                      'Main Phase',
                      'Combat Phase',
                      'Ending Phase'],
            'Step': ['Untap Step',
                     'Upkeep Step',
                     'Draw Step',
                     'Beginning of Combat Step',
                     'Declare Attackers Step',
                     'Declare Blockers Step',
                     'Combat Damage Step',
                     'End of Combat Step'
                     'End Step',
                     'Cleanup Step'],
            'Beginning Phase': ['Untap Step',
                                'Upkeep Step',
                                'Draw Step'],
            'Main Phase': [],
            'Combat Phase': ['Beginning of Combat Step',
                             'Declare Attackers Step',
                             'Declare Blockers Step',
                             'Combat Damage Step',
                             'End of Combat Step'],
            'Ending Phase': ['End Step',
                             'Cleanup Step'],
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
        current_phase = self.phase
        current_step = self.step
        steps_in_phase = self.turn_structure[current_phase]
        assert current_step in steps_in_phase, 'Invalid step'
        step_index = steps_in_phase.index(current_step)
        if step_index == len(steps_in_phase) - 1:
            phase_index = list(self.turn_structure.keys()).index(current_phase)
            next_phase = list(self.turn_structure.keys())[phase_index + 1]
            self.phase = next_phase
            self.step = self.turn_structure[next_phase][0]
        else:
            self.step = steps_in_phase[step_index + 1]
