# uses logic to simulate play for a game
from events.game import GameEvent


class AutoBattle:

    def __init__(self, turn_limit: int | None, number_of_games: int,
                 game_kind: str, players: dict, data: dict
                 ):
        self.turn_limit = turn_limit
        self.number_of_games = number_of_games
        assert self.number_of_games > 0, 'Not enough games'
        self.game_kind = game_kind
        self.players = players
        self.data = data

    def run_singlePlayer_game_logic(self):
        while self.number_of_games > 0:
            self.number_of_games -= 1
            game = GameEvent(
                game_kind=self.game_kind,
                players=self.players,
                data=self.data
            )
            assert game.num_players == 1, 'Not a single player game'
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # single player game logic

    def run_multiPlayer_game_logic(self):
        while self.number_of_games > 0:
            self.number_of_games -= 1
            game = GameEvent(
                game_kind=self.game_kind,
                players=self.players,
                data=self.data
            )
            assert game.num_players > 1, 'Not a multi player game'
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # single player game logic
