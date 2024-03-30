def open_file(file_name:str):
    with open(file_name,"r") as file:
        text=file.read()
        return text

# print(open_file("text.txt"))     

def open_file_for_add(file_name:str):
    with open(file_name,"w+") as file:
        text_pr=input("Goo text")
        file.write(text_pr)
        return text_pr
    
# print(open_file_for_add("/home/xushu/study_plan_python/start/files/task_second/text.txt"))    

def open_file_for_append(file_name:str):
    with open(file_name,"a") as file:
        text_prompt=input("Goo text: ")
        file.write(" "+text_prompt+" ")

        return text_prompt

# print(open_file_for_append("/home/xushu/study_plan_python/start/text.txt"))
file=open("text.txt","a")
# print("line",file=file,end='str')
