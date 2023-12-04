# Contract Summary GPT

## Overview

This repository contains a tool that, given a smart contract address, generates a summary of the contract. The summary provides essential information about the contract's purpose and details.

## Usage

To use the tool locally, follow these steps:

1. **Install Dependencies:**
Ensure that you have the necessary dependencies installed. You can do this by running:

```bash
virtualenv venv -python=python3.9
source venv/Script/activate
pip install -r requirements.txt
```

2. **Configure CORS:**
If you encounter Cross-Origin Resource Sharing (CORS) issues, modify the CORS settings by removing restrictions and allowing all origins (`"*"`). 

```py
app.add_middleware(
CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

3. **Run the Application:**
Start the application to generate contract summaries:

```bash
py -m uvicorn app.main:app --reload --loop asyncio
```

Feel free to contribute to and enhance this tool. Happy coding!