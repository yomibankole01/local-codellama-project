# Local CodeLlama Assistant

This project demonstrates how to run a **local Large Language Model (LLM)** using `llama-cpp-python` with GPU acceleration on Apple Silicon.

The project loads a **CodeLlama 13B model in GGUF format** and allows users to interact with it through Python to generate code and answer questions.

---

## Features

* Run **CodeLlama locally**
* GPU acceleration using Apple **Metal**
* Interactive prompt for asking questions or generating code
* Configurable inference parameters (temperature, top_p, repeat penalty, etc.)
* Lightweight setup using `llama-cpp-python.`

---

## Project Structure

```
local-codellama-project
│
├── script.py              # Main script to run the model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files
│
├── models/                # Local model files (not committed)
│   └── codellama-13b.Q5_K_M.gguf
│
└── llm-env/               # Python virtual environment (ignored)
```

---

## Requirements

* Python 3.10+
* Apple Silicon Mac (recommended)
* 32GB+ RAM recommended for 13B models
* `llama-cpp-python`

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yomibankole01/local-codellama-project.git
cd local-codellama-project
```

### 2. Create a virtual environment

```
python3 -m venv llm-env
source llm-env/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Download the Model

Download a **CodeLlama GGUF model** compatible with `llama.cpp` and place it inside the `models/` folder.

Example:

```
models/codellama-13b.Q5_K_M.gguf
```

Note: Model files are **not included in the repository** because they are large.

---

## Running the Model

Run the script:

```
python script.py
```

You will be prompted to enter a question or coding request.

Example:

```
Enter your prompt: write a python function to reverse a list
```

Example output:

```python
def reverse_list(lst):
    return lst[::-1]
```

---

## Model Configuration

The model is initialized with the following parameters:

```
temperature=0.2
top_p=0.9
top_k=40
repeat_penalty=1.2
n_ctx=4096
```

These parameters help produce stable responses for coding tasks.

---

## Notes

* The model runs **entirely locally**
* No external API calls are required
* Performance depends on your system hardware

---

## Future Improvements

* Add a web UI
* Support chat history
* Add streaming responses
* Integrate additional models

---

## License

MIT License
