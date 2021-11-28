from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.garden.mapview import MapView, MapMarker
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color, Line
import update_cont
import get_pos

if get_pos.state is not 1:
    print("not connected to db")
else:
    update_cont.connect_to_db()

class Logo(Screen):
    pass

class SecondWindow(Screen):
    name = ObjectProperty(None)
    
    def btn_states(self,n , m, a):
        print("przycisk:", self.name)
        if get_pos.state == 1:
            update_cont.update_states(n, m, a)

class ThirdWindow(Screen):

    def slider_release(self, r, s):
        print(" | puszczono")
        print(" | rudder ang. :", r )
        print(" | boom ang. : ", s )
        print("----------------------")
        if get_pos.state == 1:
            update_cont.update_sliders(r, s)

class Measurments(Screen):
    def __init__(self, **kw):
        super(Measurments, self).__init__(**kw)

        with self.canvas:
            #Color(.534, .345, .678, .8)

            self.rect = Rectangle(pos = self.center,
                size= (200, 200))

            self.lin = Line()

            self.bind(pos = self.update_rect,
            size = self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        #self.rect.size = self.size

class Map(Screen):
    
    #test A1
    def __init__(self, **kw):
        super().__init__(**kw)
        self.register_event_type("on_frame")
        Clock.schedule_interval(self._on_frame, 0)
        Clock.schedule_interval(self.lift_off, 2)
    #----

    def lift_off(self, *args):  
        
        if get_pos.state == 1:
            pos = get_pos.get_pos()
            #boat_lat = self.ids.boat_loc.lat
            #boat_lon = self.ids.boat_loc.lon
            print(self.ids.boat_loc.lat)
            print(pos[1])
            self.ids.boat_loc.lat = pos[1]
            self.ids.boat_loc.lon = pos[2]

        if get_pos.state == 0:
            print("not connected to db")

        print("working..")


    #test A1
    
    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass
    #-------  
    
    
    pass  
 

class Attribb(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("screen.kv")


class TestApp(App):

    #map = Map()
    #Clock.schedule_once(map.lift_off, 0.5)

    def build(self):
        map = Map()
        Clock.schedule_interval(map.lift_off, 0.5)
        #Clock.schedule_interval(self.update, 1)
        return kv

    #def update(self, *args):
    #    print("update")
    #    map = Map()
    #    Clock.schedule_once(map.lift_off, 0.5)
    #    Clock.schedule_once(self.build, 0.5)
        

if __name__ == "__main__":
    print("App created by Pawel Galusza")
    TestApp().run()

print("koniec..")
if get_pos.state == 1:
    update_cont.exit()