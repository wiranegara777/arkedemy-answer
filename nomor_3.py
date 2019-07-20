from itertools import permutations

def substring(lst,string):
    for i in range(len(lst),0,-1):
        for x in permutations(lst, i):
            if ''.join(x) == string:
                for j in range (len(x)):
                    if j == len(x)-1:
                        print(x[j])
                    else:
                        print(x[j]+", ",end="")
                    

lst = ['pro', 'gram', 'merit', 'program', 'it', 'programmer']
string = str(input())
substring(lst,string)