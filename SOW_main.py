import kivy
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass

class AddPlayerPopup(Popup):
    PlayerName = StringProperty("")
    PlayerIncome = NumericProperty(0.0)
    PlayerCash = NumericProperty(0.0)

    def SavePlayerInfo(self):
        self.PlayerName = self.ids.name_input.text
        print("player name is", self.PlayerName)
        try:
            self.PlayerIncome = float(self.ids.income_input.text)
            print("player income is", self.PlayerIncome)
        except ValueError:
            print("Invalid player income! put a valid number")
            self.ids.income_input.text = ""
            return
        try:
            self.PlayerCash = float(self.ids.cash_input.text)
            print("player cash is", self.PlayerCash)
        except ValueError:
            print("Invalid player cash! put a valid number")
            return
        self.dismiss()



class SOWapp(App):

    def ShowAddPlayerPopup(self):
        popup = Factory.AddPlayerPopup()
        popup.open()



if __name__ == '__main__':
    SOWapp().run()