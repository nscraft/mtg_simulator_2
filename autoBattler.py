# uses logic to simulate play for a game
from events.game import GameEvent


class AutoBattle:

    def __init__(self, singleton_mtg_sim, turn_limit: int | None, number_of_games: int,
                 game_kind: str, players: dict,
                 ):
        self.singleton_mtg_sim = singleton_mtg_sim
        self.data = singleton_mtg_sim.data
        self.turn_limit = turn_limit
        self.number_of_games = number_of_games
        assert self.number_of_games > 0, 'Not enough games'
        self.game_kind = game_kind
        self.players = players

    def run_singlePlayer_game_logic(self):
        game_num = 1
        while game_num <= self.number_of_games:
            print(f'Running game {game_num} of {self.number_of_games}')
            game_num += 1
            game = GameEvent(
                singleton_mtg_sim=self.singleton_mtg_sim,
                game_kind=self.game_kind,
                selected_players=self.players,
            )
            assert game.num_players == 1, 'Not a single player game'
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # single player game logic

    def run_multiPlayer_game_logic(self):
        game_num = 1
        while game_num <= self.number_of_games:
            print(f'Running game {game_num} of {self.number_of_games}')
            game_num += 1
            game = GameEvent(
                singleton_mtg_sim=self.singleton_mtg_sim,
                game_kind=self.game_kind,
                selected_players=self.players,
            )
            assert game.num_players > 1, 'Not a multi player game'
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # single player game logic
