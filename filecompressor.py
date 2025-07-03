import PySimpleGUI as fsg

label1 = fsg.Text("Select files you want to compress: ")
input1 = fsg.Input()
button1 = fsg.FileBrowse("Choose")

label2 = fsg.Text("Select folder where you want to save: ")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose")

button3 = fsg.Button("Compress")
window = fsg.Window("File Compressor", [[label1, input1, button1],
                                        [label2, input2, button2],
                                        [button3]])

window.read()   
window.close()
