import pandas as pd
import ollama
import os


def parseAlgorithmCharacteristics(algo):
    data = pd.ExcelFile(os.getcwd() + "/quantum_code/Characteristics.xlsx")
    df = pd.read_excel(data)
    filtered_df = df[df["File"].str.contains(algo)]
    algorithmName = filtered_df["Algorithm"].values[0]
    cubits = filtered_df["Number of Qubits"].values[0]
    desc = filtered_df["One line description"].values[0]
    return str(algorithmName), str(cubits), str(desc)


def genPrompt(previousPrompt, previousExplanation):
    # ollama.pull("llama2")

    prompt = (
        "I gave llama2 the following prompt to generate an explanation for code:\n"
        + previousPrompt
    )
    prompt += "and it gave me the following explanation:\n" + previousExplanation
    prompt += "Give me one prompt that would be able to generate a better explanation describing:\n"
    prompt += "A general description of what’s happening\n A high-level description of each step\n A relation between these high-level steps and the relevant code line\n and put it in double quotations."

    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": prompt}],
    )["message"]

    optimizedPrompt = response["content"]
    print(optimizedPrompt)
    return optimizedPrompt.split('"')[1]


def runPrompt(complexPrompt, iterative, iterations, base_model):
    ollama.pull(base_model)

    for filename in os.listdir(os.getcwd() + "/quantum_code/Code"):
        if filename.endswith(".qasm"):
            print("Processing file: " + filename)
            for i in range(0, iterations):
                print("Iteration " + str(i))
                inFile = open(
                    os.path.join(os.getcwd() + "/quantum_code/Code", filename),
                    "r",
                    encoding="utf-8",
                )
                code = inFile.read()
                prompt = "Can you give a high-level explanation of this code?" + code
                if complexPrompt:
                    algorithmName, cubits, desc = parseAlgorithmCharacteristics(
                        filename
                    )
                    prompt += "The name of the algorithm is: " + algorithmName + "\n"
                    prompt += "The code includes " + cubits + " cubits" + "\n"
                messages = [{"role": "user", "content": prompt}]

                if iterative and i > 0:
                    prompt = genPrompt(previousPrompt, previousExplanation) + code
                    print("Optimized prompt is: " + prompt)

                response = ollama.chat(
                    model=base_model,
                    messages=messages,
                )["message"]

                content = response["content"]
                path = (
                    os.getcwd()
                    + f"/explanation/{base_model}_{2}/"
                    + filename
                    + "_"
                    + str(complexPrompt)
                )
                if iterative:
                    os.makedirs("explanation_iterative_new", exist_ok=True)
                    os.makedirs(
                        "explanation_iterative_new/" + str(iterations) + "_iterations",
                        exist_ok=True,
                    )
                    path = (
                        os.getcwd()
                        + f"/explanation_iterative_new/"
                        + str(iterations)
                        + "_iterations/"
                        + filename
                        + "_"
                        + str(i)
                    )
                    prompt_out = open(path + "_prompt", "w", encoding="utf-8")
                    prompt_out.write(prompt)

                os.makedirs(
                    os.getcwd() + f"/explanation/{base_model}_{2}", exist_ok=True
                )
                out = open(
                    path,
                    "w",
                    encoding="utf-8",
                )
                out.write(content)
                # print(content)
                previousExplanation = content
                previousPrompt = prompt
