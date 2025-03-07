# uses logic to simulate play for a game
from events.game import GameEvent


class AutoBattle:

    def __init__(self, player_count: int, turn_limit: int | None, number_of_games: int):
        self.player_count = player_count
        assert self.player_count > 0, 'Not enough players'
        self.turn_limit = turn_limit
        self.number_of_games = number_of_games
        assert self.number_of_games > 0, 'Not enough games'

    def run_singlePlayer_game_logic(self):
        while self.number_of_games > 0:
            self.number_of_games -= 1
            GameEvent(
                game_kind=self.game_kind,
                players=self.players,
                data=self.data
            )
            while self.turn_limit > 0:
                self.turn_limit -= 1
                self.advance_turn()

    def run_multiPlayer_game_logic(self):
        pass

