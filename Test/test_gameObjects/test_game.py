import unittest
import unittest.mock
from events.game import GameEvent


class TestGameEvent(unittest.TestCase):
    def setUp(self):
        self.mock_singleton_mtg_sim = unittest.mock.MagicMock()
        self.mock_singleton_mtg_sim.data = {
            'players': [
                {'id': 1, 'name': 'Nick', 'decks': ['Boros Aggro', 'Dimir Control'], "score": 0},
                {'id': 2, 'name': 'Josh', 'decks': ['Simic Ramp', 'Gruul Aggro'], "score": 100}
            ],
            'decks': [
                {'name': 'Boros Aggro', 'kind': 'standard', 'cards': ['Card 1', 'Card 2', 'Card 3']},
                {'name': 'Kumena Merfolk', 'kind': 'commander', 'cards': ['Card 1', 'Card 2', 'Card 3'],
                 'commander': 'Kumena, Tyrant of Orazca'},
                {'name': 'Golgari Midrange', 'kind': 'standard', 'cards': ['Card 1', 'Card 2', 'Card 3']},
                {'name': 'Rith Tokens', 'kind': 'commander', 'cards': ['Card 1', 'Card 2', 'Card 3'],
                 'commander': 'Rith, the Awakener'},
            ]
        }

        self.mock_game_kind = 'commander'
        self.mock_selected_players = {
            'player_1': {'name': 'Nick', 'deck': 'Boros Aggro'},
            'player_2': {'name': 'Josh', 'deck': 'Kumena Merfolk'},
        }
        self.game_event = GameEvent(self.mock_singleton_mtg_sim,
                                    self.mock_game_kind,
                                    self.mock_selected_players)

    def test_players_playing(self):
        self.assertTrue(self.game_event.players_playing())
        self.game_event.num_players = 0
        self.assertFalse(self.game_event.players_playing())

    def test_remove_player(self):
        self.game_event.remove_player_from_game('player_1')
        self.assertEqual(self.game_event.num_players, 1)
        players_playing_names = [player.name for player in self.game_event.players]
        # assert player_2 still in the game
        self.assertIn('Josh', players_playing_names)
        self.game_event.remove_player_from_game('player_2')
        self.assertEqual(self.game_event.num_players, 0)
        self.assertEqual(self.game_event.players, [])

    def test_advance_turn(self):
        self.game_event.phase = 'Beginning Phase'
        self.game_event.step = 'Untap Step'
        self.game_event.advance_turn()
        self.assertEqual(self.game_event.step, 'Upkeep Step')
        self.assertEqual(self.game_event.phase, 'Beginning Phase')

        self.game_event.step = 'Draw Step'
        self.game_event.advance_turn()
        self.assertEqual(self.game_event.step, 'Pre-combat Main Phase')
        self.assertEqual(self.game_event.phase, 'Main Phase')
        self.game_event.advance_turn()
        self.assertEqual(self.game_event.step, 'Beginning of Combat Step')
        self.assertEqual(self.game_event.phase, 'Combat Phase')

        self.game_event.phase = 'Combat Phase'
        self.game_event.step = 'End of Combat Step'
        self.game_event.advance_turn()
        self.assertEqual(self.game_event.step, 'Post-combat Main Phase')
        self.assertEqual(self.game_event.phase, 'Main Phase')
