def cli():
    com_list = ["ls", "cd", "exit"]
    while True:
        line = input("VFS> ").split()
        if line[0] not in com_list:
            print("Error")
        elif line[0] == "ls":
            print(*line)
        elif line[0] == "cd":
            print(*line)
        elif line[0] == "exit":
            break
cli()