import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget

class LogParser(Widget):
    pass

class LogPartnerApp(App):

    def build(self):
        return LogParser()


if __name__ == '__main__':
    LogPartnerApp().run()
