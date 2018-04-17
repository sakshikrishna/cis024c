import helper
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int, help="number 1")
parser.add_argument("num2", type=int, help="number 2")
args = parser.parse_args()
print helper.add2(args.num1, args.num2), "is the sum from main.py"