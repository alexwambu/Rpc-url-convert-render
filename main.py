from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "GBTNetwork RPC Backend is live."}

@app.post("/")
async def rpc_handler(request: Request):
    body = await request.json()
    return JSONResponse({
        "jsonrpc": "2.0",
        "id": body.get("id"),
        "result": "Simulated RPC response"
    })
