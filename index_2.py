# x=10
# def show():
#     global x
#     x+=20
#     print(x)
# show()
# print(x
# def outer():
#     x = "outter"
#     def inner():
#         nonlocal x
#         x = "inner"
         
#     inner() 
#     print("x after inner", x)
# outer()
# x="global"
# def outter():
#     x="enclosing"
#     def inner():    
#         x="local" 
#         print("inner x:",x)
#     inner()
#     print("outer x:",x)
# outter()
# print("global x:",x)
# y=1
# def countdown(n):
    
#     print(n)
#     if n > 0:
#         countdown(n-1)
# countdown(5)
x="global" 
def outer():
    x="enclosing"
    def inner():
        global x
        x="local"
        print("inner x:",x)
    inner()
    print("outer x:",x)
outer()
print("global x:",x)