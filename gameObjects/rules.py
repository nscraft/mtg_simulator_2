class GeneralRules:
    def __init__(self):
        self.rules = {
            "starting_life": 20,
            "max_hand_size": 7,
            "deck_size": 60,
            "max_copies": 4,
            "starting_hand_size": 7,
            "starting_hand_draws": 1,
        }


class CommanderRules(GeneralRules):
    def __init__(self):
        super().__init__()
        self.rules["starting_life"] = 40
        self.rules["max_hand_size"] = 7
        self.rules["deck_size"] = 100
        self.rules["max_copies"] = 1
        self.rules["starting_hand_size"] = 7
        self.rules["starting_hand_draws"] = 1
