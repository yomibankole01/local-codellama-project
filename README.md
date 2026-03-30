# Local CodeLlama Assistant

This project demonstrates how to run a **local Large Language Model (LLM)** using `llama-cpp-python` with GPU acceleration on Apple Silicon.

The project loads a **CodeLlama 13B model in GGUF format** and allows users to interact with it through Python to generate code and answer questions.

---

## Features

* Run **CodeLlama locally**
* GPU acceleration using Apple **Metal**
* Interactive prompt for asking questions or generating code
* Configurable inference parameters (temperature, top_p, repeat penalty, etc.)
* Lightweight setup using `llama-cpp-python`
* No external API calls required

---

## Project Structure

```
local-codellama-project
│
├── scripts
 └── run_llama.py          # Main script to run the model
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

* **Python 3.10+**
* **Apple Silicon Mac** (M1, M2, M3 or newer recommended)
  * Intel Macs are supported but will not benefit from Metal GPU acceleration
  * Intel Macs will have significantly slower inference speeds
* **32GB+ RAM** recommended for 13B models (16GB minimum)
* `llama-cpp-python` with Metal support

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yomibankole01/local-codellama-project.git
cd local-codellama-project
```

### 2. Create a virtual environment

```bash
python3 -m venv llm-env
source llm-env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### Key Dependencies

The main dependencies are:

* **llama-cpp-python==0.3.19** - Core library for running GGUF models
* **numpy==2.4.3** - Numerical computing
* **requests==2.33.0** - For downloading models
* Additional Jupyter/IPython utilities for interactive development

---

## Download the Model

Download a **CodeLlama GGUF model** compatible with `llama.cpp` and place it inside the `models/` folder.

### Recommended Sources

1. **Hugging Face** (Recommended)
   - Visit: https://huggingface.co/TheBloke/CodeLlama-13B-GGUF
   - Download: `CodeLlama-13B.Q5_K_M.gguf` (~8.6 GB)
   - Paste into `models/` folder

2. **Ollama**
   - Install Ollama: https://ollama.ai
   - Run: `ollama pull codellama:13b`
   - Location: `~/.ollama/models/`

3. **Quantized Models on Hugging Face**
   - Search for "CodeLlama GGUF" on https://huggingface.co
   - Use Q5_K_M quantization for good quality/speed balance

### File Placement

```
models/
└── codellama-13b.Q5_K_M.gguf
```

**Note:** Model files are **not included in the repository** because they are large (typically 8-13 GB).

---

## Running the Model

Run the script:

```bash
python script.py
```

You will be prompted to enter a question or coding request.

### Example Session

**Input:**
```
Enter your prompt: write a python function to reverse a list
```

**Output:**
```
def reverse_list(lst):
    """Reverse a list using slicing."""
    return lst[::-1]

# Alternative methods:
# Using reversed(): list(reversed(lst))
# Using sort(): lst.sort(reverse=True)
```

**Full interaction example:**
```
Enter your prompt: how do I read a file in python?

Here's how to read a file in Python:

1. Using context manager (recommended):
   with open('file.txt', 'r') as file:
       content = file.read()

2. Reading line by line:
   with open('file.txt', 'r') as file:
       for line in file:
           print(line.strip())

3. Reading all lines into a list:
   with open('file.txt', 'r') as file:
       lines = file.readlines()
```

---

## Model Configuration

The model is initialized with the following parameters:

```python
temperature=0.2      # Lower = more deterministic (good for code)
top_p=0.9            # Nucleus sampling threshold
top_k=40             # Top-k sampling
repeat_penalty=1.2   # Discourage repetitive output
n_ctx=4096           # Context window (max input+output tokens)
```

These parameters help produce stable, high-quality responses for coding tasks.

---

## Performance Expectations

### Apple Silicon (M1/M2/M3)
- **Generation speed:** 10-20 tokens/second (with Metal acceleration)
- **First token latency:** 1-3 seconds
- **Response time for typical prompt:** 5-30 seconds

### Intel Mac
- **Generation speed:** 2-5 tokens/second (CPU only)
- **First token latency:** 3-8 seconds
- **Response time for typical prompt:** 30-120+ seconds

### Memory Usage
- **Model size:** ~13 GB (Q5_K_M quantization)
- **RAM during inference:** 16-20 GB
- **VRAM (if available):** Automatically offloaded via Metal

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'llama_cpp'"

**Solution:**
```bash
pip install --upgrade llama-cpp-python
```

If issues persist, rebuild with Metal support:
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install --upgrade --force-reinstall llama-cpp-python
```

### Issue: "Metal acceleration not detected" or slow inference

**Solution:**
- Verify Metal is available: `python -c "import llama_cpp; print(llama_cpp.METAL)"`
- Rebuild llama-cpp-python with Metal:
  ```bash
  CMAKE_ARGS="-DLLAMA_METAL=on" pip install --upgrade --force-reinstall llama-cpp-python
  ```
- Restart the terminal and Python process

### Issue: "CUDA out of memory" or "killed" during inference

**Solution:**
- Reduce context size: Change `n_ctx=4096` to `n_ctx=2048`
- Use a smaller model (e.g., 7B instead of 13B)
- Close other applications to free RAM
- Check available memory: `free -h` (Linux/Mac)

### Issue: Model file not found

**Solution:**
- Verify the model file is in the `models/` folder
- Check the exact filename matches in `script.py`
- Ensure it's a valid GGUF format file

### Issue: Slow first inference (5+ seconds)

**Solution:**
- This is normal! The model loads into memory on first use
- Subsequent inferences will be faster
- Disable MLLock to speed up: `export LLAMA_NUM_THREADS=4`

### Issue: Responses are repetitive or low quality

**Solution:**
- Lower `temperature` (currently 0.2) for more deterministic output
- Reduce `repeat_penalty` if too aggressive
- Try a larger model (CodeLlama 34B) if available
- Make your prompt more specific

---

## Notes

* The model runs **entirely locally** — no internet required after setup
* No external API calls are made
* Performance depends on your system hardware (especially RAM and CPU)
* Metal acceleration significantly improves performance on Apple Silicon
* The first run will be slower as the model loads into memory

---

## Future Improvements

* Add a web UI (Flask/FastAPI)
* Support chat history and multi-turn conversations
* Add streaming responses for better UX
* Integrate additional models (Mistral, Llama 2, etc.)
* Add batch processing for multiple prompts
* Implement prompt templates for specific tasks

---

## License

MIT License

---

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

## Resources

* [llama-cpp-python GitHub](https://github.com/abetlen/llama-cpp-python)
* [CodeLlama Models on Hugging Face](https://huggingface.co/meta-llama)
* [GGUF Format Documentation](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
