from PySimpleGUI import Text, CBox, Input, Button, Window



layout =  [[Text(f'{i}. '), Input()] for i in range(1,6)]
layout += [[Button('Save'), Button('Exit')]]

window = Window('To Do List Example', layout)
event, values = window.read()

print(values)
