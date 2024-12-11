from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.uix.label import Label

<CreateAccountWindow>:
name: "create"

namee: namee
email: email
password: passw

FloatLayout:
cols:1

FloatLayout:
size: root.width, root.height/2

Label:
text: "Create an Account"
size_hint: 0.8, 0.2
pos_hint: {"x":0.1, "top":1}
font_size: (root.width**2 + root.height**2) / 14**4

Label:
size_hint: 0.5,0.12
pos_hint: {"x":0, "top":0.8}
text: "Name: "
font_size: (root.width**2 + root.height**2) / 14**4

TextInput:
pos_hint: {"x":0.5, "top":0.8}
size_hint: 0.4, 0.12
id: namee

_____________________________________________________________________________
Arquivo: my.kv
multiline: False
font_size: (root.width**2 + root.height**2) / 14**4

Label:
size_hint: 0.5,0.12
pos_hint: {"x":0, "top":0.8-0.13}
text: "Email: "
font_size: (root.width**2 + root.height**2) / 14**4

TextInput:
pos_hint: {"x":0.5, "top":0.8-0.13}
size_hint: 0.4, 0.12
id: email
multiline: False
font_size: (root.width**2 + root.height**2) / 14**4

Label:
size_hint: 0.5,0.12
pos_hint: {"x":0, "top":0.8-0.13*2}
text: "Password: "
font_size: (root.width**2 + root.height**2) / 14**4

TextInput:
pos_hint: {"x":0.5, "top":0.8-0.13*2}
size_hint: 0.4, 0.12
id: passw
multiline: False
password: True
font_size: (root.width**2 + root.height**2) / 14**4

_____________________________________________________________________________
Arquivo: my.kv

Button:
pos_hint:{"x":0.3,"y":0.25}
size_hint: 0.4, 0.1
font_size: (root.width**2 + root.height**2) / 17**4
text: "Already have an Account? Log In"
on_release:
root.manager.transition.direction = "left"
root.login()

Button:
pos_hint:{"x":0.2,"y":0.05}
size_hint: 0.6, 0.15
text: "Submit"
font_size: (root.width**2 + root.height**2) / 14**4
on_release:
root.manager.transition.direction = "left"
root.submit()

<LoginWindow>:
name: "login"

email: email
password: password

FloatLayout:

Label:

_____________________________________________________________________________
Arquivo: my.kv
text:"Email: "
font_size: (root.width**2 + root.height**2) / 13**4
pos_hint: {"x":0.1, "top":0.9}
size_hint: 0.35, 0.15

TextInput:
id: email
font_size: (root.width**2 + root.height**2) / 13**4
multiline: False
pos_hint: {"x": 0.45 , "top":0.9}
size_hint: 0.4, 0.15

Label:
text:"Password: "
font_size: (root.width**2 + root.height**2) / 13**4
pos_hint: {"x":0.1, "top":0.7}
size_hint: 0.35, 0.15

TextInput:
id: password
font_size: (root.width**2 + root.height**2) / 13**4
multiline: False
password: True
pos_hint: {"x": 0.45, "top":0.7}
size_hint: 0.4, 0.15

Button:
pos_hint:{"x":0.2,"y":0.05}
size_hint: 0.6, 0.2

_____________________________________________________________________________
Arquivo: my.kv
font_size: (root.width**2 + root.height**2) / 13**4
text: "Login"
on_release:
root.manager.transition.direction = "up"
root.loginBtn()

Button:
pos_hint:{"x":0.3,"y":0.3}
size_hint: 0.4, 0.1
font_size: (root.width**2 + root.height**2) / 17**4
text: "Não tem uma conta? Bora criar!"
on_release:
root.manager.transition.direction = "right"
root.createBtn()

<MainWindow>:
n: n
email: email
created:created

FloatLayout:
Label:
id: n
pos_hint:{"x": 0.1, "top":0.9}
size_hint:0.8, 0.2
text: "Account Name: "

Label:

_____________________________________________________________________________
Arquivo: my.kv
id: email
pos_hint:{"x": 0.1, "top":0.7}
size_hint:0.8, 0.2
text: "Email: "

Label:
id: created
pos_hint:{"x": 0.1, "top":0.5}
size_hint:0.8, 0.2
text: "Created: "

Button:
pos_hint:{"x":0.2, "y": 0.1}
size_hint:0.6,0.2
text: "Sair"
on_release:
app.root.current = "login"
root.manager.transition.direction = "down"
