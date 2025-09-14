```
pip install langchain langchain-huggingface
```

```
HUGGINGFACEHUB_API_TOKEN="your_huggingface_token_here"
```

```
from langchain_huggingface import HuggingFaceEndpoint

# Connect to a Hugging Face hosted model (replace with any available model repo id)
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-Nemo-Instruct-2407",  # example model
    task="text-generation",
    max_new_tokens=100
)

# Generate response
output = llm.predict("Write a short poem about Hong Kong")
print(output)
```
