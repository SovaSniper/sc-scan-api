from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

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

@app.post("/api/summary")
async def summary(contract: str = "", 
                  network: str = ""):
    scanner = ScScan(network)
    try:
        abi = scanner.get_data(contract)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # information = await generate_ai_summary(abi)
    return StreamingResponse(generate_ai_summary(abi))

@app.get("/api/test")
def test():
    return {"message": "Hello World"}

async def test_stream():
    for i in range(10):
        yield b"Sending data"

@app.get("/api/test/stream")
async def main():
    return StreamingResponse(test_stream())
