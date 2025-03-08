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
            game.set_player_battlefields()
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # single player game logic
                self.singlePlayer_game_logic(game)

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
            game.set_player_battlefields()
            while self.turn_limit > 0:
                self.turn_limit -= 1
                # multi player game logic

    def singlePlayer_game_logic(self, game: GameEvent):
        player_on_turn = next(player for player in game.players if player.player_num == game.player_with_priority.strip('player_'))
        player_on_turn.start_turn()
        print(f'{player_on_turn.name} is on turn {player_on_turn.turn_num}')
        if game.phase == 'Beginning Phase' and game.step == 'Untap Step':
            pass
        elif game.phase == 'Beginning Phase' and game.step == 'Upkeep Step':
            pass
        elif game.phase == 'Beginning Phase' and game.step == 'Draw Step':
            pass
        elif game.phase == 'Main Phase' and game.step == 'Pre-combat Main Phase':
            pass
        elif game.phase == 'Combat Phase' and game.step == 'Beginning of Combat Step':
            pass
        elif game.phase == 'Combat Phase' and game.step == 'Declare Attackers Step':
            pass
        elif game.phase == 'Combat Phase' and game.step == 'Declare Blockers Step':
            pass
        elif game.phase == 'Combat Phase' and game.step == 'Combat Damage Step':
            pass
        elif game.phase == 'Combat Phase' and game.step == 'End of Combat Step':
            pass
        elif game.phase == 'Main Phase' and game.step == 'Post-combat Main Phase':
            pass
        elif game.phase == 'Ending Phase' and game.step == 'End Step':
            pass
        elif game.phase == 'Ending Phase' and game.step == 'Cleanup Step':
            pass
        else:
            raise ValueError('Invalid phase or step')