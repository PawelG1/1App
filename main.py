from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import update_cont


class Logo(Screen):
    pass

class SecondWindow(Screen):
    name = ObjectProperty(None)
    
    def btn_states(self,n , m, a):
        print("przycisk:", self.name)
        update_cont.update_states(n, m, a)

class ThirdWindow(Screen):

    def slider_release(self, r, s):
        print(" | puszczono")
        print(" | rudder ang. :", r )
        print(" | boom ang. : ", s )
        print("----------------------")
        update_cont.update_sliders(r, s)

class Measurments(Screen):
    pass

class Attribb(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("screen.kv")


class TestApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    print("App created by Paweł Gałusza")
    TestApp().run()

print("koniec..")
update_cont.exit()