# LLM Prompt Exploration for The Automatic Generation of Quantum Algorithm Explanations

This repository contains the replication package for the experiments conducted in the paper "LLM Prompt Exploration for The Automatic Generation of Quantum Algorithm Explanations".

## Requirements

- Install `ollama` from the following [link](https://ollama.com/download)
- Obtain a GPT-3 API key from OpenAI by following the instructions [here](https://openai.com/blog/openai-api)
- Install the following Python libraries:
  - `openai`
  - `ollama`
  - `pandas`
  - `seaborn`

## Project Structure

- `explanation_generation/`: Contains the code for generating quantum code explanations using LLMs.
- `explanation_human/` and `explanation_human_anonym/`: Contains the explanations from human-written prompts.
- `explanation_iterative/` and `explanation_iterative_anonym/`: Contains the explanations from iterative generated prompts.
- `figures/`: Contains the figures used in the paper.
- `forms/`: Contains the forms used for the evaluation of explanations.
- `quantum_code/`: Contains the quantum algorithms used to obtain the explanations.
- `analysis.ipynb`: Jupyter notebook for the analysis of the evaluation results and to generate the figures in the paper.
- `anonym_data.ipynb`: Jupyter notebook for anonymizing the explanations before the evaluation.
- `results.csv`: The evaluation results for RQ1, RQ2, and RQ3.
- `results_iterative.csv`: The evaluation results for RQ4.
