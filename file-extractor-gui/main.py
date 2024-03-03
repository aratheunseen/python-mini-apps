import PySimpleGUI as sg
import ZipExtractor

select_file_label = sg.Text('Select ZIP File to Extract:')
select_filepath = sg.InputText(key='file')
files_browse_button = sg.FilesBrowse('Choose')

dest_folder_label = sg.Text('Select Destination Folder:')
destination_folderpath = sg.InputText(key="destination")
folder_browse_button = sg.FolderBrowse('Choose')

output_label = sg.Text(key='output', size=(50,1))

extract_button = sg.Button('Extract', size=(55,2), button_color=('white', 'green'), key='extract')
exit_button = sg.Button('Exit', size=(10,2), button_color=('white', 'red'), key='exit')

layout = [
    [select_file_label, select_filepath, files_browse_button],
    [dest_folder_label, destination_folderpath, folder_browse_button],
    [extract_button, exit_button],
    [output_label],
]

window = sg.Window('ZIP Extractor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'exit':
        break

    elif event == 'extract':
        filepath = values['file']
        destination = values['destination']
        ZipExtractor.extract_zipfile(filepath, destination)
        window['file'].update('')
        window['destination'].update('')
        output_label.update('File Extracted Successfully!')

window.close()