from zipfile import ZipFile
from pathlib import Path

#Path of folder/file to zip
file_to_zip = './Web'
#Path to zip file that is to be unzipped
file_to_unzip = './UnzippedFiles'
file_of_zip = './ZippedFiles/Web.zip'


folder_path_to_zip = Path(file_to_zip)





def ZipTheFile(srcLocation, desLocation):
    print('\n\n\nSelecting file to compress...')
    print(f'Source file -  ${srcLocation}')
    print(f'Destination file - ${desLocation}')
    print('Compressing...')
    with ZipFile(desLocation,'w') as zip:
        for file in srcLocation.rglob('*'):
            zip.write(file,file.relative_to(srcLocation.parent))
        print(f"Compressing finished at ${desLocation}\n\n\n")

def UnzipTheFile(fromLocation, toLocation):
    print('\n\n\nSelecting file to decompress...')
    print(f'Source file -  ${fromLocation}')
    print(f'Destination file - ${toLocation}')
    print('DeCompressing...')
    with ZipFile(fromLocation,'r') as zip:
        zip.extractall(path=toLocation)
        print(f"DeCompressing finished at ${toLocation}\n\n\n")


def main():
    
    #ZipTheFile(folder_path_to_zip,file_of_zip)
    UnzipTheFile(file_to_unzip,file_to_unzip)
    

if __name__ == '__main__':
    main()