import os
import json
from get_data import get_data


class MTGSim:
    def __init__(self):
        self.data = {}
        self.saved_player_names = []
        print("~~Welcome to MTG_Sim!~~")

    def set_data(self):
        # find all json files in the data directory
        data_files = [file for file in os.listdir('data') if file.endswith('.json')]
        if not data_files:
            print("No data files found.")
        else:
            # for each file, update self.configuration with the contents of the file
            for file in data_files:
                self.data.update(get_data(file.split('.')[0]))
            self.saved_player_names = self.get_saved_player_names()

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
                self.run_game_menu()
            elif choice == '5':
                print("Goodbye")
                exit()
            else:
                print("Invalid choice. Please choose again.")

    def create_player_menu(self):
        print("\nSaved Players:"
              f"\n{self.saved_player_names}")
        print("\nEnter your new player's name:")
        player_name = input()
        if player_name in self.saved_player_names:
            print("Player already exists. Please enter a new name.")
        else:
            self.create_player(player_name)
            self.set_data()
            print("\nSaved Players:"
                  f"\n{self.saved_player_names}")
            self.main_console_menu()

    def load_deck_menu(self):
        pass

    def print_report_menu(self):
        pass

    def run_game_menu(self):
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
        while True:
            print("\nGame Mode:"
                  "\n1. Commander",
                  "\n2. Standard",
                  )
            game_mode = input("Enter your choice (1-2):")
            if game_mode == '1':
                game_mode = 'Commander'
            elif game_mode == '2':
                game_mode = 'Standard'
            else:
                print("Invalid choice. Please choose again.")
                continue
            settings.update({'game_mode': game_mode})

            num_players = input("Enter the number of players:")
            if num_players.isnumeric():
                num_players = int(num_players)
                settings.update({'num_players': num_players})
            else:
                print("Invalid input. Please enter a number.")
                continue
            while True:
                print("\nSaved Players:"
                      f"\n{self.saved_player_names}")
                for i in range(settings['num_players']):
                    player = input(f"Enter player {i + 1} name:")
                    if player in self.saved_player_names:
                        settings['players'].update({f'player_{i + 1}': player})
                    else:
                        print("Player does not exist.")
                        continue
                break
            break
        self.start_game(
            settings['game_mode'],
            settings['players'],
        )

    def create_player(self, player_name):
        max_player_id = self.data['players'][-1]['id']
        new_player = {
            'id': max_player_id + 1,
            'name': player_name,
            'decks': [],
            'score': 0
        }
        self.data['players'].append(new_player)
        player_file_content = {
            'players': self.data['players']
        }
        with open('data/players.json', 'w') as f:
            json.dump(player_file_content, f, indent=4)

    def load_deck(self):
        pass

    def print_report(self):
        pass

    def start_game(self, game_mode: str, players: dict):
        pass


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.set_data()
    mtg_sim.get_saved_player_names()
    mtg_sim.main_console_menu()
