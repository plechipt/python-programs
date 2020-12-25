import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class UI(GridLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.title = Label(text='Registration', font_size=15)
        self.add_widget(self.title)

        self.inside.add_widget(Label(text='First Name:  '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text='Submit', font_size=35)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        name = self.name.text
        last = self.last_name.text
        email = self.email.text

        print(f'Name: {name}, Last Name: {last}, Email: {email}')

class MyApp(App):
    def build(self):
        return UI()

if __name__ == '__main__':
    MyApp().run()
