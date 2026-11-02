from kivy.app import App
from kivy.uix.label import Label

class EzanVaktiApp(App):
    def build(self):
        return Label(text='Bursa Ezan Vakti Uygulaması')

if __name__ == '__main__':
    EzanVaktiApp().run()
