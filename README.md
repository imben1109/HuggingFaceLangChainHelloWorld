# Huggingface Langchain Hello World

# Hugging Face LangChain App

This project demonstrates how to use the LangChain library in conjunction with Hugging Face models for text generation.

## Installation

To get started, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

This will install the following packages:

- langchain
- langchain-huggingface

## Setup

Before running the application, make sure to set your Hugging Face API token. You can do this by setting the environment variable:

```
export HUGGINGFACEHUB_API_TOKEN="your_huggingface_token_here"
```

## Usage

To run the application, execute the main script:

```
python src/main.py
```

The script connects to a specified Hugging Face model and generates text based on a given prompt.

## Hello World Example

In the `src/main.py` file, you can find an example of how to connect to a Hugging Face hosted model and generate a response. The current example generates a short poem about Hong Kong.

## Template Prompt Example

You can also use prompt templates for more flexible text generation.  
Run the template prompt example script:

```
python src/template_prompt_example.py
```

This script demonstrates how to use LangChain's `PromptTemplate` to dynamically create prompts for Hugging Face models.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!