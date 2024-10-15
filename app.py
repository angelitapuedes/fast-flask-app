from fastapi import FastAPI, Request
import uvicorn

#Initial Fast API App
app = FastAPI()

@app.get("/")
def read_root():
    return {'text': "FASTAPI Section"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1' , port=8000)