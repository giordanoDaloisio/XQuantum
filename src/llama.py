from utils import runPrompt
from argparse import ArgumentParser
import argparse

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--complex", action="store_true")
    args = parser.parse_args()

    base_model = "llama2"
    runPrompt(args.complex, base_model)
    # runPrompt(False)
