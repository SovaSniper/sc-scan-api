import json
import time
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.model.model_service import ModelService, get_model
from app.services.storage_service import StorageService, get_storage

from app.services.utils.generate_ai_summary import generate_ai_summary
from app.services.sc_scan_service import ScScan

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sc-scan.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/abi")
async def abi(contract: str = "", 
             network: str = "", 
             storage: StorageService = Depends(get_storage)):
    start = time.time()

    scanner = ScScan(network)
    try:
        abi = scanner.get_data(contract)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # cid = storage.upload(payload)

    end = time.time()
    elapsed = end - start
    print("Processing completed in", elapsed, "seconds")

    return abi

@app.get("/api/onchain")
async def abi(contract: str = "", 
             network: str = "", 
             storage: StorageService = Depends(get_storage)):
    start = time.time()

    scanner = ScScan(network)
    try:
        abi = scanner.get_data(contract)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    cid = storage.upload(abi)

    end = time.time()
    elapsed = end - start
    print("Processing completed in", elapsed, "seconds")

    return { "cid": cid }

# @app.post("/api/summary")
# async def summary(contract: str = "", 
#                   network: str = ""):
#     scanner = ScScan(network)
#     try:
#         abi = scanner.get_data(contract)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
#     # information = await generate_ai_summary(abi)
#     return StreamingResponse(generate_ai_summary(abi))

@app.post("/api/state")
async def state(request: Request,
                model: ModelService = Depends(get_model)):
    start = time.time()

    prompt = json.dumps(await request.json())
    stateMutability = model.predict(prompt)
    
    end = time.time()
    elapsed = end - start
    print("Processing completed in", elapsed, "seconds")
    return {"stateMutability": stateMutability}

@app.get("/api/test")
def test():
    return {"message": "Hello World"}

async def test_stream():
    for i in range(10):
        yield b"Sending data"

@app.get("/api/test/stream")
async def main():
    return StreamingResponse(test_stream())
