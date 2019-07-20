def mrBrulee(command,N,lst):
    string = ""
    for i in range(1,N+1):
        string+=str(i)
    if command == "MUL":
        total = int(string[lst[0]-1])
        for j in range(1,len(lst)):
            total*=int(string[lst[j]-1])
    elif command == "DIV":
        total = int(string[lst[0]-1])
        for j in range(1,len(lst)):
            total/=int(string[lst[j]-1])
    elif command == "SUM":
        total = int(string[lst[0]-1])
        for j in range(1,len(lst)):
            total+=int(string[lst[j]-1])
    else:
        total = int(string[lst[0]-1])
        for j in range(1,len(lst)):
            total-=int(string[lst[j]-1])
    return(total)

print(mrBrulee("SUM",20,[11,13,15]))
print(mrBrulee("MUL",20,[12,15,17]))
