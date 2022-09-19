import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("operation", type=str)
parser.add_argument("x", type=float)
parser.add_argument("y", type=float)

args = parser.parse_args()

if args.operation == "add":
    product = operator.add(args.x, args.y)
elif args.operation == "sub":
    product = operator.sub(args.x, args.y)
elif args.operation == "mult":
    product = operator.mul(args.x, args.y)
elif args.operation == "truediv":
    product = operator.truediv(args.x, args.y)
elif args.operation == "floordiv":
    product = operator.floordiv(args.x, args.y)
elif args.operation == "mod":
    product = operator.mod(args.x, args.y)
elif args.operation == "pow":
    product = operator.pow(args.x, args.y)
elif args.operation == "sin":
    product = [math.sin(args.x), math.sin(args.y)]
elif args.operation == "cos":
    product = [math.cos(args.x), math.cos(args.y)]
elif args.operation == "log":
    product = [math.log(args.x), math.log(args.y)]
elif args.operation == "sqrt":
    product = [math.sqrt(args.x), math.sqrt(args.y)]
elif args.operation == "exp":
    product = [math.exp(args.x), math.exp(args.y)]
else:
    product = "invalid argument"

print(product)
