import ollama
import pandas as pd
import os
from utils import parseAlgorithmCharacteristics

ollama.pull("llama2")


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
                model="llama2",
                messages=messages,
            )["message"]

            content = response["content"]
            os.makedirs(os.getcwd() + "/../Output/llama2/", exist_ok=True)
            out = open(
                os.getcwd()
                + "/../Output/llama2/"
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
