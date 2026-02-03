import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass

class SOWapp(App):
    pass


if __name__ == '__main__':
    SOWapp().run()