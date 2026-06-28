###################################
#   My Hello World in FastAPI     #
###################################

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def great(who):
    return f"Hello? {who}"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)