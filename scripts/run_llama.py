from llama_cpp import Llama
import os

model_path = os.path.join("models", "codellama-13b.Q5_K_M.gguf")

llm = Llama(
    model_path=model_path,
    n_gpu_layers=-1,  
    n_ctx=4096,
    verbose=False,
    temperature=0.2,
    top_p=0.9,
    repeat_penalty=1.2,
    top_k=40,
    mirostat_mode=2
)

print("Model loaded successfully. Type 'exit' to quit.\n")

while True:
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "exit":
        break

    output = llm(
    prompt=prompt,
    max_tokens=200,
    temperature=0.2,
    top_p=0.9,
    top_k=40,
    repeat_penalty=1.2,
    stop=["[INST]", "\n\n\n", "User:", "Q:"]
)
    answer = output["choices"][0]["text"]
    print(f"Model response: {answer}\n")