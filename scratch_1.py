import os, time, datetime
import PySimpleGUI as sg

l = list()
t = list()


layout = [
    [sg.Text('File Explorer')], [sg.Text("Enter a Path"), sg.InputText(" ", key='d')],
    [sg.Text("Enter a Filter Expression (extension)                     "),
     sg.Checkbox("Display Directories", key='c')],
    [sg.InputText(" ", key='e'), sg.Button("Find")], [sg.Text("List of Files and Directories: ")],
    [sg.Listbox(" ", size=(100, 20), key="l")]

]
window = sg.Window('File Explorer v0.1', layout)


def fo():
    fs = 0
    for root, dirs, files in os.walk(values['d']):
        dirs.clear()
        for f in files:
            if ext in f:
                path = os.path.join(root, f)
                c = time.ctime(os.path.getmtime(path))
                l.append(os.path.join(f) + "  <<" + c + ">>")
                fs=fs+1
    return fs


while True:
    event, values = window.Read()
    if event == "Find":
        os.chdir(values['d'])
        ext = values["e"]

        if values['c'] == True:
            l += [x for x in os.listdir(os.curdir) if os.path.isdir(x)]

        elif values['c'] == False:
            l += ['DIR' for x in os.listdir(os.curdir) if os.path.isdir(x)]

        print(fo())
        print(len(l))
        window.FindElement("l").Update(l)
        l.clear()
