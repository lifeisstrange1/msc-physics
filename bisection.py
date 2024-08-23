# first part of code

def f(x):
    return x**2 - 3


def bisection(a,b,n):
    i = 1
    condition = True
    while condition:
        x = (a+b)/2
        if f(x)<0:
           a=x
        else:
           b=x

        print("iteration = ", i, "and x = ", x, "for f(x) = ", f(x))
        if i==n:
           condition= False
        else:
           condition= True
           i = i + 1
    print("required root is = ", x)

a = float(input("First approximation root : "))
b = float(input("Second approximation root : "))
n = int(input("No. of iterations : "))

if f(a)*f(b) > 0:
   print("Given approximate roots do not bracket the root")
   print("Try again with different values")

else:
   bisection(a,b,n)


# second part of code

def f(x):
    return x**2 - 3


def bisection(a,b,e):
    i = 1
    x = 0
    condition = True
    while condition:
        g = f(x)
        x = (a+b)/2
        if f(x)<0:
           a=x
        else:
           b=x

        print("iteration = ", i, "and x = ", x, "for f(x) = ", f(x))

        i = i + 1
        condition = abs(f(x)-g)>e
    print("required root is = ", x)

a = float(input("First approximation root : "))
b = float(input("Second approximation root : "))
e = float(input("Permissible error : "))

if f(a)*f(b) > 0:
   print("Given approximate roots do not bracket the root")
   print("Try again with different values")

else:
   bisection(a,b,e)

