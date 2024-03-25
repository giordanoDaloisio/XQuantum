import pandas as pd


def parseAlgorithmCharacteristics(algo):
    data = pd.ExcelFile("../Dataset/Characteristics.xlsx")
    df = pd.read_excel(data)
    filtered_df = df[df["File"].str.contains(algo)]
    algorithmName = filtered_df["Algorithm"].values[0]
    cubits = filtered_df["Number of Qubits"].values[0]
    desc = filtered_df["One line description"].values[0]
    return str(algorithmName), str(cubits), str(desc)
