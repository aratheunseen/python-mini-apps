import zipfile

def extract_zipfile(filepath, destination_dir):
    with zipfile.ZipFile(filepath, 'r') as zipf:
        zipf.extractall(destination_dir)

if __name__ == '__main__':
    extract_zipfile('test.zip', 'test')