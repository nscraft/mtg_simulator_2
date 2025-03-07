import unittest
from gameObjects.state import GameState


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.mock_players = {
            'player_1': {'name': 'John Doe', 'deck': 'Boros Aggro'},
            'player_2': {'name': 'Jane Doe', 'deck': 'Simic Ramp'},
        }
        self.game_state = GameState('standard', self.mock_players)

    def test_players_playing(self):
        self.assertTrue(self.game_state.players_playing())
        self.game_state.num_players = 0
        self.assertFalse(self.game_state.players_playing())

    def test_remove_player(self):
        self.game_state.remove_player_from_game('player_1')
        self.assertEqual(self.game_state.num_players, 1)
        self.assertEqual(self.game_state.players, {'player_2': {'name': 'Jane Doe', 'deck': 'Simic Ramp'}})

        self.game_state.remove_player_from_game('player_2')
        self.assertEqual(self.game_state.num_players, 0)
        self.assertEqual(self.game_state.players, {})

    def test_advance_turn(self):
        self.game_state.phase = 'Beginning Phase'
        self.game_state.step = 'Untap Step'
        self.game_state.advance_turn()
        self.assertEqual(self.game_state.step, 'Upkeep Step')
        self.assertEqual(self.game_state.phase, 'Beginning Phase')

        self.game_state.step = 'Draw Step'
        self.game_state.advance_turn()
        self.assertEqual(self.game_state.step, 'Pre-combat Main Phase')
        self.assertEqual(self.game_state.phase, 'Main Phase')
        self.game_state.advance_turn()
        self.assertEqual(self.game_state.step, 'Beginning of Combat Step')
        self.assertEqual(self.game_state.phase, 'Combat Phase')

        self.game_state.phase = 'Combat Phase'
        self.game_state.step = 'End of Combat Step'
        self.game_state.advance_turn()
        self.assertEqual(self.game_state.step, 'Post-combat Main Phase')
        self.assertEqual(self.game_state.phase, 'Main Phase')
