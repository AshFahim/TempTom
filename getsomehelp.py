#install PySimpleGUI and run this 
#just a loop to that stops the program from closing unless you're a stupid
import PySimpleGUI as sg

x=0
while x==0:
    layout = [
    [sg.Text('Are you stupid?')],
    [sg.Button('Yes'), sg.Button('No')]
]
    window = sg.Window("Demo Window", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        x = 0
    elif event == "Yes":
        x=1
        break
Window.close()  
