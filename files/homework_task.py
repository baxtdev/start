def to_add(filename:str,data:list):
    with open(filename,"w") as file:
        if type(data) is list:
            for i in data:    
                file.write(i)
            print("Запись закончено")
        else:
            print("Этот обьект не является списком")


def to_read(filenames:list):
    data_files=[]
    if type(filenames) is list:
        for i in filenames:
            with open(i) as files:
                data_files.append(files.read()+"\n")
        print("Все файлы прочитаны")
        return data_files        
    
    else:
        print("Этот обьект не является списком")
