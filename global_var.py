x = 5 #variable global

def myfunc():
    global x 
    x = 10 #variable local
    print(x)

myfunc()
print(x)
