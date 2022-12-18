import os 
diretorio = os.getcwd()

folder_list=[i for i in os.listdir(diretorio) if os.path.isdir(i)]
for folder in folder_list:
    path=os.path.join(diretorio, folder)
    files= os.listdir(path)
    for file in files:
        from_path= os.path.join(path,file)
        to_path=os.path.join(diretorio, file)
        os.replace(from_path. to_path)
    os.rdmir(path)    
