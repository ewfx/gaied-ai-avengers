## Imports

from llama_cpp import Llama

## Download the GGUF model

## Instantiate model from downloaded file
llm = Llama(
    model_path='D:\installations\python-llm\gguf\models\DeepSeek-R1-Distill-Qwen-14B-Q5_K_S.gguf',
    n_ctx=16000,  # Context length to use
    n_threads=32,            # Number of CPU threads to use
    n_gpu_layers=0        # Number of model layers to offload to GPU
)

## Generation kwargs
generation_kwargs = {
    "max_tokens":20000,
    "stop":["</s>"],
    "echo":False, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

## Run inference
prompt = "what is the capital of india ? "
res = llm(prompt, **generation_kwargs) # Res is a dictionary

## Unpack and the generated text from the LLM response dictionary and print it
print(res["choices"][0]["text"])
# res is short for result


