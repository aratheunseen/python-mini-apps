import PySimpleGUI as sg
import ZipMaker

select_file_label = sg.Text('Select Files to Compress:')
select_filepaths = sg.InputText(key='files')
file_browse_button = sg.FilesBrowse('Choose')

dest_folder_label = sg.Text('Select Destination Folder:')
destination_folderpath = sg.InputText(key="destination")
folder_browse_button = sg.FolderBrowse('Choose')

output_label = sg.Text(key='output', size=(50,1))

compress_button = sg.Button('Compress', size=(55,2), button_color=('white', 'green'), key='Compress')
exit_button = sg.Button('Exit', size=(10,2), button_color=('white', 'red'), key='Exit')

layout = [
    [select_file_label, select_filepaths, file_browse_button],
    [dest_folder_label, destination_folderpath, folder_browse_button],
    [compress_button, exit_button],
    [output_label]
]

window = sg.Window('Files Compressor', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'Compress':
        filepaths = values['files'].split(';')
        destination = values['destination']
        ZipMaker.make_zipfile(filepaths, destination)
        output_label.update('Files Compressed!')

window.close()