# State Mutability Classification for Unverified Contract ABI

Welcome to the State Mutability Classification repository for unverified smart contract ABIs! This toolkit equips you with powerful tools to analyze the state mutability of unverified smart contracts, aiding the community in comprehending their behavior and potential risks. At its core, this repository houses a BERT-based model, leveraging GPT-4 to succinctly summarize information about unknown contracts based on their ABI.

## Model Information

The state mutability classification model can be accessed at the following location: [IKenLeI/bert-state-mutability](https://huggingface.co/IKenLeI/bert-state-mutability)

## Run Locally

To run this project locally, execute the following commands in your terminal:

1. Using Python:

```bash
virtualenv venv --python=python3.9      # requires 3.9 for pytorch and docker
source venv/Script/activate
pip3 install -r requirements.txt && python3 -m uvicorn app.main:app --reload --loop asyncio
```

2. Using Python 3 (Windows)

```bash
virtualenv venv --python=python3.9       # requires 3.9 for pytorch and docker
source venv/Script/activate
pip3 install -r requirements.txt && py -m uvicorn app.main:app --reload --loop asyncio
```

These commands install the necessary dependencies and run the FastAPI application locally. Choose the appropriate command based on your Python environment.

## Build and Run Docker Image Locally

1. Build the Docker Image:

```bash
docker build --tag sc-scan .
```

2. Run the Docker Image:

```bash
docker run -d -p 8080:8080 sc-scan
```

These commands build and run the Docker image locally, allowing you to access the application at localhost. Refer to the `Dockerfile` for more details on building and running Docker images.

## Deployment

Explore instructions on deploying this project to Azure App Service: [Azure App Service Deployment Guide](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app-for-app-service?tabs=web-app-flask#create-a-resource-group-and-azure-container-registry)

## Tech Stack

This project leverages the following technologies and tools:

- Trained BERT model for state mutability classification
- GPT-4 for ABI summarization
- FastAPI for creating the API interface
- Ethereum smart contracts
- IPFS (InterPlanetary File System)

## How It Works

This repository aims to provide a systematic approach to understanding the state mutability of unverified smart contracts. The BERT-based model classifies the state mutability of various functions in the contract ABI, categorizing them as "pure," "view," "non-payable," or "payable." This information is crucial for analyzing and assessing potential risks associated with a smart contract.

The summarization capabilities of GPT-4 offer concise descriptions of smart contracts based on their ABI, facilitating quick assessment and reverse engineering.

## Contribution

We welcome contributions from the community to enhance and improve this project. If you have ideas for additional features, improvements, or encounter any issues, feel free to open an issue or create a pull request. Together, we can make this tool more effective and valuable to the community.

## License

This project is available under the [MIT License](LICENSE). Please review the license before using or contributing to this repository.

Thank you for your interest in our project. We hope it aids you in understanding and analyzing unverified smart contracts effectively.