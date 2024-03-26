import pandas as pd
import os
import shutil

file_folders = ["gpt", "tinyllama", "llama"]

data = pd.read_excel("Characteristics.xlsx")

for folders in file_folders:
    for run in os.listdir(folders):
        for file in os.listdir(os.path.join(folders, run)):
            file_name = file.split("_")
            alg_name = data[data["File"] == file_name[0]]["Algorithm"].values[0]
            if file_name[1] == "True":
                prompt_style = "complex_prompt"
            else:
                prompt_style = "simple_prompt"
            shutil.copy(
                os.path.join(folders, run, file),
                os.path.join(
                    alg_name, run, prompt_style, file + "_" + folders + ".txt"
                ),
            )
