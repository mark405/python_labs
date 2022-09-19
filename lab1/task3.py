import argparse

parser = argparse.ArgumentParser()

parser.add_argument("formula", type=str, nargs="*")

args = parser.parse_args()

status = True
for i in range(0, len(args.formula[0])):
    if args.formula[0][i] == "+" or args.formula[0][i] == "-":
        if args.formula[0][i + 1] == "+" or args.formula[0][i + 1] == "-":
            status = False
            break

if status:
    try:
        print(True, eval(" ".join(args.formula)))
    except:
        print(False, None)
else:
    print(False, None)

