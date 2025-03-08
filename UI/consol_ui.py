from events import game
from saveData.writePlayer import WritePlayer
from autoBattler import AutoBattle


class ConsoleUI:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConsoleUI, cls).__new__(cls)
        return cls._instance

    def __init__(self, singleton_mtg_sim):
        if not hasattr(self, 'initialized'):  # Ensure __init__ is only called once
            self.singleton_mtg_sim = singleton_mtg_sim
            self.data = singleton_mtg_sim.data
            self.saved_player_names = self.get_saved_player_names()
            self.user_choice = None
            self.initialized = True

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
                print("...why do we even have that lever?")
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
        game_type: 'Auto Battle' | 'Goldfish'
        game_type: 'Commander' | 'Standard'
        num_players: int (number of players)
        players: dict {
            'player_1': str (player name),
            'player_2': str (player name),
            ...
        }
        """
        settings = {
            'game_mode': None,
            'game_type': None,
            'num_players': None,
            'players': {},
        }
        # choose game mode
        while True:
            print("\nGame Mode:"
                  "\n1. Auto Battle",
                  "\n2. Goldfish",
                  )
            game_mode = input("Enter your choice (1-2):")
            if game_mode == '1':
                game_mode = 'Auto Battle'
                settings.update({'game_mode': game_mode})
            elif game_mode == '2':
                game_mode = 'Goldfish'
                settings.update({'game_mode': game_mode})
            else:
                print("Invalid choice. Please choose again.")
                continue
            break
        # Auto Battle settings
        if settings['game_mode'] == 'Auto Battle':
            while True:
                num_battles = input("Enter the number of battles:")
                if num_battles.isnumeric() and int(num_battles) > 0:
                    num_battles = int(num_battles)
                    settings.update({'num_battles': num_battles})
                else:
                    print("Invalid input. Please enter a number grater than zero.")
                    continue
                break
            while True:
                turn_limit = input("Enter the turn limit:")
                if turn_limit.isnumeric() and int(turn_limit) > 0:
                    turn_limit = int(turn_limit)
                    settings.update({'turn_limit': turn_limit})
                else:
                    print("Invalid input. Please enter a number grater than zero.")
                    continue
                break
        # choose game type
        while True:
            print("\nGame Type:"
                  "\n1. Commander",
                  "\n2. Standard",
                  )
            game_type = input("Enter your choice (1-2):")
            if game_type == '1':
                game_type = 'Commander'
                settings.update({'game_type': game_type})
            elif game_type == '2':
                game_type = 'Standard'
                settings.update({'game_type': game_type})
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
                    deck_list = self.data['players'][self.saved_player_names.index(player)].get('decks', [])
                    if len(deck_list) > 0:
                        settings['players'].update({f'player_{i + 1}': player})
                    else:
                        print("No decks available for this player.")
                        continue
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
              f"\nGame Type: {settings['game_type']}"
              f"\nNumber of Players: {settings['num_players']}"
              f"\nPlayers: {settings['players']}")
        if settings['game_mode'] == 'Auto Battle':
            print(
                f"\nNumber of Battles: {settings['num_battles']}"
                f"\nTurn Limit: {settings['turn_limit']}"
            )
        self.user_choice = input("Start game? (y/n):")
        if self.user_choice.lower() == 'y':
            print("Starting game...")
            self.run_game(settings)
        else:
            print("Game cancelled.")
            self.main_console_menu()

    def run_game(self, settings: dict):
        if settings['game_mode'] == 'Auto Battle':
            auto = AutoBattle(
                singleton_mtg_sim=self.singleton_mtg_sim,
                turn_limit=settings['turn_limit'],
                number_of_games=settings['num_battles'],
                game_kind=settings['game_type'],
                players=settings['players'],
            )
            if len(settings['players']) == 1:
                print("Running single player game...")
                auto.run_singlePlayer_game_logic()
            else:
                print("Running multi player game...")
                auto.run_multiPlayer_game_logic()
        elif settings['game_mode'] == 'Goldfish':
            game.GameEvent(
                singleton_mtg_sim=self.singleton_mtg_sim,
                game_kind=settings['game_type'],
                selected_players=settings['players'],
                           )
