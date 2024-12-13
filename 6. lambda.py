message = lambda: print("Привіт козак : ")
message()

add = lambda a,b: print(f"a+b = {a+b}")
add(2,4)
print(add)

a=35
print(str(a))

res=12
def summa(a, b):
    global res
    res=a+b
    print(f"result = {res}")

summa(23,45)
print(f"result = {res}")