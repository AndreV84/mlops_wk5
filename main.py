from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/
app = FastAPI(title='Triton Health Check')



#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    response_face_bokeh = requests.get("http://52.23.168.177:8001/")
    response_face_emotion = requests.get("http://52.23.168.177:8002/")
    return [response_face_bokeh.content, response_face_emotion.content]
