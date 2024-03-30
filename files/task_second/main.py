word="My love is your,sister \nand you.Janydan"
word=word.replace(",","").replace("."," ")
word=word.replace("\n","")
word=word.split()

def count_word(word:str,data:list):
    count=0
    index=0
    for i in data:
        if i==word:
            count+=1
            index=i
    return {"кол":count,"слово":index}   

def count_words_in_file(data:list):
    len_count=0
    len_countet=0
    for i in data:
        len_count+=len(i)
        len_countet+=1
    return {"кол_слов":len(data),"ср_дл_слов":len_count/len_countet}


def count_sentences_in_file(data:list):
    return len(data)    

# print(word)
# print(count_sentences_in_file(word))



def count_senten(text):
    if text[-1]==".":
        text_sentecnce=text.split(".")
        return len(text_sentecnce)-1
    return len(text.split("."))


def count_word(text:str):
    text=text.replace(","," ").replace("."," ")
    return len(text.split())

def open_files(files):
    datas={}
    for i in files:
        with open(i,"r") as file:
            datas[i]=file.read()
    return datas


def add_to_file(data:dict):
    with open("outputt.txt","w+") as file:
        for i in data:
            file.write("Файл-"+i+":"+f"{count_word(open_files([i])[i])}"+" слов."+f"{count_senten((open_files([i])[i]))} предложении\n")

add_to_file((open_files(["text.txt","output.txt","request.txt"])))
print(count_word(open_files(["text.txt"])["text.txt"]))        