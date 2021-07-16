from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Logo(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("screen.kv")


class TestApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    TestApp().run()