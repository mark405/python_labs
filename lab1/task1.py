import argparse

parser = argparse.ArgumentParser()

parser.add_argument("x", type=int)
parser.add_argument("operation")
parser.add_argument("y", type=int)

args = parser.parse_args()

if args.operation == "+":
    product = args.x + args.y
elif args.operation == "-":
    product = args.x - args.y
elif args.operation == "*":
    print(args.x * args.y)
elif args.operation == "/":
    if args.y == 0:
        product = "invalid argument"
    else:
        product = args.x / args.y
else:
    product = "invalid argument"

print(product)
