from kivy.app import App

from kivy.uix.button import Button

class ButtonApp(App):
  def build(self):
    def on_press_button(self):
      print("você apertou um botão!")

if __name__ == "__main__":
  app = ButtonApp(App)
  app.run()