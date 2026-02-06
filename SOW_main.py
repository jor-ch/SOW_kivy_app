import kivy
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class Asset:
    def __init__(self, asset_name, asset_value, asset_income_per_month):
        self.name = asset_name
        self.value = asset_value
        self.asset_income_per_month = asset_income_per_month

class Player:

    def __init__(self, input_name, input_income, input_cash): #to call this constructor after adding input parameters in popup to add new players
        self.name = input_name
        self.income = input_income
        self.cash = input_cash
        self.asset_value = 0
        self.liabilities = 0 #may not need debt variable, need to double check in future
        self.debt = 0
        self.expense_per_month = 0
        self.net_worth = self.cash

    def payday(self):
        self.cash += (self.income - self.expense_per_month)
        print("cash now is", self.cash)



class WindowManager(ScreenManager):
    pass

class AddPlayersScreen(Screen):
    pass

class PlayerButton(Button):
    PlayerName = StringProperty("")

class AddPlayerPopup(Popup):
    PlayerName = StringProperty("")
    PlayerIncome = NumericProperty(0.0)
    PlayerCash = NumericProperty(0.0)

    def ShowInvalidEntryPopup(self):
        popup = Factory.InvalidEntryPopup()
        popup.open()

    def SavePlayerInfo(self):
        self.PlayerName = self.ids.name_input.text
        print("player name is", self.PlayerName)
        try:
            self.PlayerIncome = float(self.ids.income_input.text)
            print("player income is", self.PlayerIncome)
        except ValueError:
            self.ShowInvalidEntryPopup()
            self.ids.income_input.text = ""
            return
        try:
            self.PlayerCash = float(self.ids.cash_input.text)
            print("player cash is", self.PlayerCash)
        except ValueError:
            self.ShowInvalidEntryPopup()
            return


        app = App.get_running_app()
        AddedPlayer = Player(self.PlayerName, self.PlayerIncome, self.PlayerCash)
        app.player_list[AddedPlayer.name] = AddedPlayer
        target_screen = app.root.get_screen("AddPlayers")
        player_list_container = target_screen.ids.player_list
        player_button = Factory.PlayerButton(text = AddedPlayer.name, PlayerName = AddedPlayer.name)
        player_list_container.add_widget(player_button)
        print ("name on the button is", player_button.PlayerName)

        self.dismiss()

class InvalidEntryPopup(Popup):
    pass


class SOWapp(App):
    App.player_list = dict()  # player_list takes name of player as key, and shows player class as value
    def ShowAddPlayerPopup(self):
        popup = Factory.AddPlayerPopup()
        popup.open()



if __name__ == '__main__':
    SOWapp().run()