import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class UI(GridLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.cols = 1

        self.grid = GridLayout()
        self.grid.cols = 2

        self.grid.add_widget(Label(text='First Name: '))
        self.first_name = TextInput(multiline=False)
        self.grid.add_widget(self.first_name)

        self.grid.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.grid.add_widget(self.last_name)

        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.prank)

        self.add_widget(Label(text='Registration'))
        self.add_widget(self.grid)
        self.add_widget(self.submit)

    def prank(self,instance):
        first = self.first_name.text
        last = self.last_name.text
        return self.add_widget(Label(text=f'u suck {first} {last} xDDDDDDD XDDDDDDDDDDD'))




class MyGame(App):
    def build(self):
        return UI()

if __name__ == '__main__':
    MyGame().run()
