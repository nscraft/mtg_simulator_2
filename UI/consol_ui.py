from events import game
from saveData.writeplayer import WritePlayer


class consoleNave:
    def __init__(self, singleton_mtg_sim):
        self.singleton_mtg_sim = singleton_mtg_sim
        self.data = singleton_mtg_sim.data
        self.saved_player_names = self.get_saved_player_names()
        user_choice = None

    def get_saved_player_names(self) -> list:
        data = self.data.get('players', [])
        return [player['name'] for player in data]

    def main_console_menu(self):
        while True:
            print("\nMain Menu:"
                  "\n1. Create Player",  # todo: develop modify player option
                  "\n2. Load Deck",  # todo: develop edit deck option
                  "\n3. Print Report for Deck",
                  "\n4. Run Game",
                  "\n5. Exit")
            choice = input("Enter your choice (1-5):")
            if choice == '1':
                self.create_player_menu()
            elif choice == '2':
                self.load_deck_menu()
            elif choice == '3':
                self.print_report_menu()
            elif choice == '4':
                self.game_setup_menu()
            elif choice == '5':
                print("Goodbye")
                exit()
            else:
                print("Invalid choice. Please choose again.")
            break

    def create_player_menu(self):
        print("\nSaved Players:"
              f"\n{self.saved_player_names}")
        print("\nEnter your new player's name:")
        player_name = input()
        if player_name in self.saved_player_names:
            print("Player already exists. Please enter a new name.")
        else:
            WritePlayer(self.singleton_mtg_sim).add_player(player_name)
            self.saved_player_names = self.get_saved_player_names()
            print("\nSaved Players:"
                  f"\n{self.saved_player_names}")
            self.main_console_menu()

    def load_deck_menu(self):
        pass

    def print_report_menu(self):
        pass

    def game_setup_menu(self):
        """
        Prompts the user to select game settings and starts the game.
        game_mode: 'Commander' | 'Standard'
        num_players: int (number of players)
        players: dict {
            'player_1': str (player name),
            'player_2': str (player name),
            ...
        }
        """
        settings = {
            'game_mode': None,
            'num_players': None,
            'players': {},
        }
        # choose game mode
        while True:
            print("\nGame Mode:"
                  "\n1. Commander",
                  "\n2. Standard",
                  )
            game_mode = input("Enter your choice (1-2):")
            if game_mode == '1':
                game_mode = 'Commander'
                settings.update({'game_mode': game_mode})
            elif game_mode == '2':
                game_mode = 'Standard'
                settings.update({'game_mode': game_mode})
            else:
                print("Invalid choice. Please choose again.")
                continue
            break
        # choose number of players
        while True:
            num_players = input("Enter the number of players:")
            if num_players.isnumeric():
                num_players = int(num_players)
                settings.update({'num_players': num_players})
            else:
                print("Invalid input. Please enter a number.")
                continue
            break
        # choose players
        print("\nSaved Players:"
              f"\n{self.saved_player_names}")
        for i in range(settings['num_players']):
            while True:
                player = input(f"Enter player {i + 1} name:")
                if player in self.saved_player_names:
                    settings['players'].update({f'player_{i + 1}': player})
                else:
                    print("Player does not exist.")
                    continue
                break
        # choose decks
        for player_key, player_name in settings['players'].items():
            player_data = next((player for player in self.data['players'] if player['name'] == player_name), None)
            if player_data:
                available_decks = player_data.get('decks', [])
                print(f"\nAvailable decks for {player_name}:"
                      f"\n{available_decks}")
                print(f"\nChoose a deck for {player_name}:")
                while True:
                    deck = input()
                    if deck in available_decks:
                        settings['players'][player_key] = {'name': player_name, 'deck': deck}
                    else:
                        print("Deck not found.")
                        continue
                    break
        print("\nGame settings:"
              f"\nGame Mode: {settings['game_mode']}"
              f"\nNumber of Players: {settings['num_players']}"
              f"\nPlayers: {settings['players']}")
        print("Starting game...")

        game.GameEvent(settings['game_mode'], settings['players'], self.data)
