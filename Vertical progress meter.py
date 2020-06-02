import PySimpleGUI as sg

for i in range(10000):
        sg.OneLineProgressMeter('One Line Meter Example', i+1, 10000, 'key')

