from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
import threading
import simpleTFTPS
app= FastAPI()


def cb_get(file:str):
    print(f"user requested:{file}")
    if(not file.find("/")):
        try:
            with f.open(f"src/boot/img/{file}","rb") as f:
                return f.read()
        except Exception:
            print("file not found")
            return None
    with open("src/boot/img/snponly.efi","rb") as f:
        return f.read()
    
@app.get("/")
async def root():
    return {"message": "test"}

@app.get("/imgs/{file}")
async def get_img(file):
    print(f"user requested over http:{file}")
    return StreamingResponse(cb_get(file),media_type="application/octet-stream") 


if __name__=="__main__":
    #setup tftp server, provides data using the cb_get
    threading.Thread(
        target=simpleTFTPS.run,
        args=("0.0.0.0:69", cb_get, lambda file: False),
        daemon=True).start()
    uvicorn.run(app,host="127.0.0.1",port=80)
    