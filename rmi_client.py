import Pyro4
uri=input("Enter server uri")
calculator=Pyro4.Proxy(uri)
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Sum:",calculator.add_numbers(a,b))
print("Multiplication:",calculator.multipy_numbers(a,b))
