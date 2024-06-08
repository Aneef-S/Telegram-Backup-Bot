from zipfile import ZipFile
from pathlib import Path

#Folder/file to zip
folder_to_zip = './Dummy-Folder'
#Path to unzipped files
loc_to_unzip = './UnzippedFiles'
#Folder to unzip
folder_to_unzip = './ZippedFiles/Web.zip'
#Path to zip file that is to be unzipped
loc_of_zip = './ZippedFiles/Web.zip'


folder_path_to_zip = Path(folder_to_zip)




#For Compressing a File
def ZipTheFile(srcLocation, desLocation):
    print('\n\n\nSelecting file to compress...')
    print(f'Source file -  ${srcLocation}')
    print(f'Destination file - ${desLocation}')
    print('Compressing...')
    with ZipFile(desLocation,'w') as zip:
        for file in srcLocation.rglob('*'):
            zip.write(file,file.relative_to(srcLocation.parent))
        print(f"Compressing finished at ${desLocation}\n\n\n")


#For Decompressing a File
def UnzipTheFile(fromLocation, toLocation):
    print('\n\n\nSelecting file to decompress...')
    print(f'Source file -  ${fromLocation}')
    print(f'Destination file - ${toLocation}')
    print('DeCompressing...')
    
    with ZipFile(fromLocation,'r') as zip_ref:
        zip_ref.extractall(path=toLocation)
        print(f"DeCompressing finished at ${toLocation}\n\n\n")
   

def main():
    
    ZipTheFile(folder_path_to_zip,loc_of_zip)
    UnzipTheFile(loc_of_zip,loc_to_unzip)
    

if __name__ == '__main__':
    main()