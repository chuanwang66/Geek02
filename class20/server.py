from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI(
    title="GPU Info Service",
    description="A service to get NVIDIA GPU information using nvidia-smi",
    version="1.0.0",
    openapi_tags=[{
        "name": "GPU",
        "description": "Operations related to GPU information"
    }]
)

@app.get("/gpu/info", 
    tags=["GPU"],
    summary="Get GPU Information",
    description="Retrieves information about NVIDIA GPUs using nvidia-smi command",
    response_description="GPU information from nvidia-smi",
    operation_id="get_gpu_info"
)
async def get_gpu_info() -> Dict:
    try:
        # Execute nvidia-smi command and capture output
        result = subprocess.run(['nvidia-smi'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        
        if result.returncode == 0:
            return {
                "status": "success",
                "data": result.stdout
            }
        else:
            return {
                "status": "error",
                "message": "Failed to execute nvidia-smi",
                "error": result.stderr
            }
    except Exception as e:
        return {
            "status": "error",
            "message": "Error occurred while getting GPU information",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
