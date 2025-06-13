try:
    with open("file.txt", "r", encoding="utf-8") as file:
        print("Successful opened the file")
        content = file.read()
        print(content)  
except FileNotFoundError:
    print("File Not Found Error: No such file or directory")
except PermissionError:
    print("Permission Denied Error: Access is denied")