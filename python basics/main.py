# print your name 
print("Trilok Thakar")


#  This is single line comment 

# define variabels for diffrent data types int, boolean, char, float, double and print on the console.

a = 5
print("Type of a:", type(a))
b = True
print("Type of b:", type(b))
c = 9.0
print("type of c:", type(c))
string = "Trilok"
print("type of string:", type(string))

#  Define the local and Global variables with the same name and print both variables and 
# understand the scope of the variables


a = 5
# Uses global because there is no local 'a'
def f():
    print("Inside f() : ", a)

# Variable 'a' is redefined as a local
def g():
    a = 2
    print("Inside g() : ", a)

# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4        # value of a modified
    print("Inside h() : ", a)

# Global scope

print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


