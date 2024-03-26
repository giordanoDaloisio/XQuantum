import pandas as pd
import ollama
import os


def parseAlgorithmCharacteristics(algo):
    data = pd.ExcelFile("../Dataset/Characteristics.xlsx")
    df = pd.read_excel(data)
    filtered_df = df[df["File"].str.contains(algo)]
    algorithmName = filtered_df["Algorithm"].values[0]
    cubits = filtered_df["Number of Qubits"].values[0]
    desc = filtered_df["One line description"].values[0]
    return str(algorithmName), str(cubits), str(desc)


def runPrompt(complexPrompt, base_model):
    ollama.pull(base_model)
    # for i in range(2):
    for filename in os.listdir("../Dataset/Code"):
        if filename.endswith(".qasm"):
            print("Processing file: " + filename)
            inFile = open(
                os.path.join("../Dataset/Code", filename), "r", encoding="utf-8"
            )
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
            os.makedirs(os.getcwd() + f"/../Output/{base_model}_{2}", exist_ok=True)
            out = open(
                os.getcwd()
                + f"/../Output/{base_model}_{2}/"
                + filename
                + "_"
                + str(complexPrompt),
                "w",
                encoding="utf-8",
            )
            out.write(content)
            print(content)
