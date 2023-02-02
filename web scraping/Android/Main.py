from cgitb import text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Page2(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.hello=Label(text="hi")
        self.window.add_widget(self.hello)
        self.button=Button(text="click me")
        self.window.add_widget(self.button)
        return self.window
class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.hello=Label(text="hi")
        self.window.add_widget(self.hello)
        self.button=Button(text="click me")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self,instance):
        Page2().run()


if __name__ == "__main__":
    SayHello().run()