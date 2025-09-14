from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

def main():
    # Create a prompt template
    prompt = PromptTemplate.from_template("Write a short {genre} about {topic}")

    # Format the prompt with variables
    formatted_prompt = prompt.format(genre="poem", topic="Hong Kong")

    # Connect to a Hugging Face hosted model
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B",
        task="text-generation",
        max_new_tokens=100
    )

    # Generate response
    output = llm.invoke(formatted_prompt)
    print(output)

if __name__ == "__main__":
    main()