print(''' 
          .-------------------------.
          |                         |
          |       __________        |
          |     ||Calculator||      |
          |       ==========        |
          |                         |
          '-------------------------'
      ''')

def Add(x, y):
    print(f"Sum of you values:{x + y}")

def Sub(x, y):
    print(f"Sub of you values:{x - y}")

def Mul(x, y):
    print(f"Multiple of you values:{x * y}")

def Div(x, y):
    print(f"Divide of you values:{x / y}")

while True:

    Choice = input(f"Enter 'Add' or 'Sub' or 'Mul' or 'Div' for product of your values: ")

    x = int(input("Enter the value: "))
    y = int(input("Enter the value: "))

    if Choice == "Add":
        Add(x, y)
    elif Choice == "Sub":
        Sub(x, y)
    elif Choice == "Mul":
        Mul(x, y)
    elif Choice == "Div":
        Div(x, y)
    else:
        print("User input is invalid")

    Choice1 = input(" If you want to continue (Yes | No): ")
    if Choice1 == "Yes":
       continue
    
    else:
        print("Thanks for reaching our calculator.")
        break
