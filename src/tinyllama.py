import ollama
import pandas as pd
import os
from utils import parseAlgorithmCharacteristics

base_model = "tinyllama"

ollama.pull(base_model)


def runPrompt(complexPrompt):
    for root, dirs, files in os.walk("../Dataset/Code"):
        for filename in files:
            print("Processing file: " + filename)
            inFile = open(os.path.join(root, filename), "r", encoding="utf-8")
            code = inFile.read()
            prompt = "Can you give a high-level explanation of this code?" + code
            if complexPrompt:
                algorithmName, cubits, desc = parseAlgorithmCharacteristics(filename)
                prompt += "The name of the algorithm is: " + algorithmName + "\n"
                prompt += "The code includes " + cubits + " cubits" + "\n"
            messages = [{"role": "user", "content": prompt}]

            response = ollama.chat(
                model=base_model,
                messages=messages,
            )["message"]

            content = response["content"]
            os.makedirs(os.getcwd() + f"/../Output/{base_model}", exist_ok=True)
            out = open(
                os.getcwd()
                + f"/../Output/{base_model}/"
                + filename
                + "_"
                + str(complexPrompt),
                "w",
                encoding="utf-8",
            )
            out.write(content)
            print(content)


if __name__ == "__main__":
    runPrompt(True)
    runPrompt(False)
