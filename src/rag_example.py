from langchain_huggingface import HuggingFaceEndpoint
from langchain.schema import Document
from langchain.retrievers import InMemoryRetriever
from langchain.chains import RetrievalQA

def main():
    # Sample documents for retrieval
    docs = [
        Document(page_content="Hong Kong is a vibrant city known for its skyline."),
        Document(page_content="Victoria Harbour is a famous attraction in Hong Kong."),
        Document(page_content="Dim sum is a popular cuisine in Hong Kong."),
    ]

    # Create an in-memory retriever
    retriever = InMemoryRetriever.from_documents(docs)

    # Connect to a Hugging Face hosted model
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B",
        task="text-generation",
        max_new_tokens=100
    )

    # Create a RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    # Ask a question
    result = qa_chain.invoke({"query": "What is a popular food in Hong Kong?"})
    print("Answer:", result["result"])
    print("Source docs:", [doc.page_content for doc in result["source_documents"]])

if __name__ == "__main__":
    main()