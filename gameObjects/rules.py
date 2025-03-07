class GeneralRules:
    def __init__(self):
        self.rules = {
            "starting_life": 20,
            "max_hand_size": 7,
            "deck_size": 60,
            "max_copies": 4,
            "starting_hand_size": 7,
            "starting_hand_draws": 1,
            "turn_structure": {
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
            },
        }


class CommanderRules(GeneralRules):
    def __init__(self):
        super().__init__()
        self.rules["starting_life"] = 40
        self.rules["deck_size"] = 100
        self.rules["max_copies"] = 1
