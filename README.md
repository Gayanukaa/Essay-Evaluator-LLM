# Essay Evaluator LLM

This project is an essay evaluation application built using a Large Language Model (LLM). It allows users to input essays and receive detailed feedback on various aspects, including grammar, structure, and content relevance.

## Overview

<p>
 <img src="https://img.shields.io/github/license/Gayanukaa/Essay-Evaluator-LLM?style=flat&color=0080ff" alt="license">
 <img src="https://img.shields.io/github/last-commit/Gayanukaa/Essay-Evaluator-LLM?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
 <img src="https://img.shields.io/github/languages/top/Gayanukaa/Essay-Evaluator-LLM?style=flat&color=0080ff" alt="repo-top-language">
 <img src="https://img.shields.io/github/languages/count/Gayanukaa/Essay-Evaluator-LLM?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p>
  <em>Developed with the software and tools below.</em>
</p>
<p>
 <img src="https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white" alt="Python">
 <img src="https://img.shields.io/badge/DSPy-000000.svg?style=flat&logoColor=white" alt="DSPy">
 <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
 <img src="https://img.shields.io/badge/Ollama-00A896.svg?style=flat&logoColor=white" alt="Ollama">
 <img src="https://img.shields.io/badge/wsl-0a97f4.svg?style=flat&logo=ubuntu&logoColor=white" alt="WSL">
</p>

## Installation

1. Clone the repository: `git clone https://github.com/Gayanukaa/Essay-Evaluator-LLM.git`
2. Navigate to the project directory: `cd Essay-Evaluator-LLM`
3. Set up the environment with dependencies: `conda env create -f environment.yml -n dspy-dev`
4. Activate the environment required for the application: `conda activate lmql-dev`
5. Run the application: `streamlit run app.py`


## Prerequisites

Before running this application, make sure you have the following tools installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Ollama](https://ollama.com)

Download local model required. eg. [llama2 7B](https://ollama.com/library/llama2)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama2
```


## Usage

- Open your web browser and navigate to `http://localhost:8501` to access the Streamlit interface.
- Submit essays through the application to receive feedback and analysis.

## Comprehensive Guide

For a detailed guide on how to run your project on local models, check out my [Medium article](https://medium.com/@gayanukaamarasuriya/dspy-guide-running-your-project-on-local-models-part-1-d4dc22453620).

<p align="center">
<img src="Medium Cover Images.png" alt="Medium Article Cover Image">
</p>


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Contact

If you have any questions or suggestions, please feel free to reach out to us at [gayanukaamarasuriya@gmail.com](mailto:gayanukaamarasuriya@gmail.com).