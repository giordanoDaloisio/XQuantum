import openai
import open_ai_key
import pandas as pd
import os

from utils import getImprovePrompt


openai.api_key = open_ai_key.api_key
model_name = "gpt-3.5-turbo-16k"
temperature = 0.8


def parseAlgorithmCharacteristics(algo):
    data = pd.ExcelFile("../Dataset/Characteristics.xlsx")
    df = pd.read_excel(data)
    filtered_df = df[df["File"].str.contains(algo)]
    algorithmName = filtered_df["Algorithm"].values[0]
    cubits = filtered_df["Number of Qubits"].values[0]
    desc = filtered_df["One line description"].values[0]
    return str(algorithmName), str(cubits), str(desc)


def runPrompt(complexPrompt, improve):
    for root, dirs, files in os.walk(os.getcwd() + "/quantum_code/Code"):
        for filename in files:
            inFile = open(os.path.join(root, filename), "r", encoding="utf-8")
            code = inFile.read()
            prompt = "Can you give a high-level explanation of this code?" + code
            if complexPrompt:
                algorithmName, cubits, desc = parseAlgorithmCharacteristics(filename)
                prompt += "The name of the algorithm is: " + algorithmName + "\n"
                prompt += "The code includes " + cubits + " cubits" + "\n"

            if improve:
                prompt = getImprovePrompt(filename, code)

            messages = [{"role": "user", "content": prompt}]

            response = openai.ChatCompletion.create(
                model=model_name, messages=messages, temperature=temperature
            )

            content = response.choices[0].message.content

            if not improve:
                out = open(
                    os.getcwd()
                    + "/../Output/gpt/"
                    + filename
                    + "_"
                    + str(complexPrompt),
                    "w",
                )
                out.write(content)
            else:
                os.makedirs("explanation_improved/gpt", exist_ok=True)
                out = open(os.getcwd() + f"explanation_improved/gpt/{filename}", "w")
                out.write(content)
            print(content)


# Prompt 1: Basic
# runPrompt(False)

# Prompt 2: Include algorithm name and number of cubits
runPrompt(False, True)
