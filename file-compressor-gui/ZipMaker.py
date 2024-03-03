import pathlib
import zipfile

def make_zipfile(filepaths, destination_dir):
    destination_dir = pathlib.Path(destination_dir, 'compressed.zip')
    with zipfile.ZipFile(destination_dir, 'w') as zipf:
        for filepath in filepaths:
            zipf.write(filepath)

if __name__ == '__main__':
    make_zipfile('compressed.zip', 'C:/Users/JohnDoe/Desktop/Files')