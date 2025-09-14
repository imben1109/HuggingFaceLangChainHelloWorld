from langchain_huggingface import HuggingFaceEndpoint

def main():
    # Connect to a Hugging Face hosted model (replace with any available model repo id)
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B",
        task="text-generation",
        max_new_tokens=100
    )

    # Generate response
    output = llm.invoke("Write a short poem about Hong Kong")
    print(output)

if __name__ == "__main__":
    main()