def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x = 20
    inner_function()
    print(x)

outer_function()
 

