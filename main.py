import os
from get_data import get_data


class MTGSim:
    def __init__(self):
        self.data = {}
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

    def console_menu_loop(self):
        while True:
            print("\nMain Menu:"
                  "1. Create Player",  # todo: develop modify player option
                  "2. Load Deck",  # todo: develop edit deck option
                  "3. Print Report for Deck",
                  "4. Run Game",
                  "5. Exit")
            choice = input("Enter your choice (1-4):")

            if choice == '1':
                print("\nSaved Players:"
                      f"{self.data['players']}")
                print("\nEnter your new player's name:")
                player_name = input()
                # if player name already exists, ask for a new name
                if player_name in self.data['players']:
                    print("Player already exists. Please enter a new name.")
                else:
                    self.create_player(player_name)
                    print("\nSaved Players:"
                          f"{self.data['players']}")
                    break

            elif choice == '2':
                self.load_deck()

            elif choice == '3':
                self.print_report()

            elif choice == '4':
                settings = {
                    'game_mode': None,
                    'num_players': None,
                    'players': {},
                    'num_games': int,
                }
                while True:
                    print("\nGame Mode:"
                          "1. Commander",
                          "2. Standard",
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
                        int(num_players)
                        settings.update({'num_players': num_players})
                    else:
                        print("Invalid input. Please enter a number.")
                        continue
                    print("\nSaved Players:"
                          f"{self.data['players']}")
                    for i in range(settings['num_players']):
                        player = input(f"Enter player {i} name:")
                        if player in self.data['players']:
                            settings['players'].update({f'player_{i}': player})
                        else:
                            print("Player does not exist.")
                            continue
                    self.start_game(
                        settings['game_mode'],
                        settings['players'],
                        )

            elif choice == '4':
                print("Goodbye")
                break
            else:
                print("Invalid choice. Please choose again.")

    def create_player(self, player_name):
        max_player_id = self.data['players'][-1]['id']
        new_player = {
            'id': max_player_id + 1,
            'name': player_name,
            'decks': [],
            'score': 0
        }
        self.data['players'].append(new_player)

    def load_deck(self):
        pass

    def print_report(self):
        pass

    def start_game(self, game_mode: str, players: dict):
        pass


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.set_data()
    mtg_sim.console_menu_loop()
