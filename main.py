def divide(a, b):
    return a / b

def get_user(id):
    import subprocess
    subprocess.run("ls " + id, shell=True)

def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    return query

passwords = ["123456", "password", "admin"]

def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    return query

passwords = ["123456", "password", "admin"]
