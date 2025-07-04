import PySimpleGUI as fsg
from zipcreator import make_archive


label1 = fsg.Text("Select files you want to compress: ")
input1 = fsg.Input()
button1 = fsg.FileBrowse("Choose", key = "files")

label2 = fsg.Text("Select folder where you want to save: ")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose", key = "folder")

button3 = fsg.Button("Compress")

output_text = fsg.Text(key = "output", text_color="black")

window = fsg.Window("File Compressor", [[label1, input1, button1],
                                        [label2, input2, button2],
                                        [button3, output_text]])

 
while True:
    event, values = window.read()
    print (event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive (filepaths, folder)
    window["output"].update(value="compression complete!")


window.close()
