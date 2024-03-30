def list_ret(*args):
    return args

a=[23,23,23]
b=[45,76]
# print(list_ret(*a,b))
def return_dict(**jinjo):
    return jinjo

slov={"name":"tom","id":1}
print(return_dict(**slov))

