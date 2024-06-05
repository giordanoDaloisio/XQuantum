# LLM explanation generation for quantum algorithms

This folder contains the code for generating quantum code explanations using LLMs.

To run the code, follow these steps:

1. Install all the required libraries reported in the main README.
2. Run the following command to generate the explanations:

```bash
python <llm_name>.py <--complex> <--improve>
```

where `<llm_name>` could be `gpt`, `llama`, or `tinyllama`. The `--complex` flag is used to generate explanations using _context aware_ prompts, and the `--improve` flag is used to improve existing explanations.
