def divide(a, b):
    return a / b

def get_user(id):
    import subprocess
    subprocess.run("ls " + id, shell=True)
