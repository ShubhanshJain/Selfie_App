from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class selfie_app(App):
    def make(self):
        
        self.obj_camera = Camera()
        self.obj_camera.resolution = (810, 810)
        obj_button = Button(tect = "Click it!")
        obj.button.size.hint = (.6, .3)
        obj_button.pos_hint = {'x': .35,'y': .35 }
        obj_button.bind(on_press = self.selfie_take())
        obj_layout = BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
        return obj_layout
        
    def selfie_take(self, *args):
        print("Selfie has been taken successfully")
        self.obj_camera.export_to_png('./demo.png')
        
if  __name__ == '__main__':
    selfie_app().run()             