###################################
#   My Hello World in FastAPI     #
###################################

from fastapi import FastAPI, Body

app = FastAPI() 

@app.post("/hi") # Decorator
def great(who:str = Body(embed=True)): # embed=True mean we need json formatted request body
    return f"Hello? {who}"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)