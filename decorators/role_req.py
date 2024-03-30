
users={
    "Tillo":{
        "role":"admin"
    },
    "Baibolot":{
        "role":"user"
    },
    "Alisa":{
        "role":"child"
    },
    "Aleksey":{
        "role":"manager"
    }
}
def role_required(required_role):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            user = users.get(username)
            if user and user.get("role") == required_role:
                return func(username, *args, **kwargs)
            else:
                return "Access denied. Insufficient privileges."

        return wrapper
    return decorator


@role_required("admin")
def admin_function(username):
    return f"Hello {username}, you have admin privileges."

@role_required("manager")
def regular_function(username):
    return f"Hello {username}, you have manager user privileges."


print(admin_function("Tillo"))  
print(admin_function("Baibolot"))  

print(regular_function("Alisa"))  
print(regular_function("Aleksey"))  
