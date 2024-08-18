# Essay-Evaluator-LLM
Build and compare performance of essay evaluator in DSPy


## Configuration

Download local model. I have used [llama2 7B](https://ollama.com/library/llama2)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama2
```

Activate environment with dependencies 
```bash
conda env create -f environment.yml -n dspy-dev
```
Activate conda environment
```bash
conda activate lmql-dev
```

## Execution

To execute and test locally run ```main.py```

To execute the interface using streamlit run  ```streamlit run evaluator.py```