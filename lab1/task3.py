import argparse

parser = argparse.ArgumentParser()

parser.add_argument("formula", nargs="*")

args = parser.parse_args()


if args.formula:
    if args.formula[0].find("++") == 1 or args.formula[0].find("+-") == 1 or args.formula[0].find("-+") == 1 or args.formula[0].find("--") == 1:
        print("fd", None)
    else:
        try:
            print(True, eval(" ".join(args.formula)))
        except:
            print(False, None)
else:
    print(False, None)

