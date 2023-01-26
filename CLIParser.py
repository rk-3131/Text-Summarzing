import argparse

parser = argparse.ArgumentParser()

parser.add_argument("Number1", help="Enter number1")
parser.add_argument("Number2", help="Enter number2")
parser.add_argument("Option", help="Enter option")


args = parser.parse_args()

number1 = int(args.Number1)
number2 = int(args.Number2)

if (args.Option == "+"):
    print(number1 + number2)

elif (args.Option == "-"):
    print(number1 - number2)

elif (args.Option == "*"):
    print(number1 * number2)

elif (args.Option == "/"):
    print(number1 / number2)

else:
    print("Enter valid options")

