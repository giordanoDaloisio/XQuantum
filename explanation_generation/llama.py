from utils import runPrompt
from argparse import ArgumentParser
import argparse

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--complex", action="store_true")
    parser.add_argument("--iterative", action="store_true")
    args = parser.parse_args()

    base_model = "llama2"
    if args.complex:
        print("Use complex prompt")
    else:
        print("Use simple prompt")

    # runPrompt(args.complex, args.iterative, 3, base_model)
    runPrompt(args.complex, args.iterative, 10, base_model)
