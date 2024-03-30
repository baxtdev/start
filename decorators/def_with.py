def check(input_func):    
    def output_func(*args):     
        input_func(*args)
        print(input_func.__name__)
    return output_func     

@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
 
a=print_person("name",98)