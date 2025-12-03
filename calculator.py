def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n2-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide
           }
#print(operations["+"](4,5))

def calculate():
    should_accumulate=True
    number1=float(input("type a  1stnum:\n"))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operations_symbol=input("type a operation?:")
        number2=float(input("type 2nd num:\n"))
        answer=operations[operations_symbol](number1,number2)
        print(f"{number1} {operations_symbol} {number2} = {answer}")

        choice=input(f"if you are continuewith pre numberber type 'y' with {answer},or type 'n' to stop")
        if choice=="y":
            number1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculate()
calculate()
