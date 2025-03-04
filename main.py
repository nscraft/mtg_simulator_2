import os
from get_data import get_data
from saveData.observer import saveDataObserver
from UI import consol_ui


class MTGSim:
    def __init__(self):
        self.data = {}
        self.saveDataObserver = saveDataObserver()
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

    def start_ui(self):
        ui = consol_ui.consoleNave(self)
        ui.main_console_menu()


if __name__ == "__main__":
    mtg_sim = MTGSim()
    mtg_sim.set_data()
    mtg_sim.start_ui()
