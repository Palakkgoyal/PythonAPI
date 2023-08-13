from fastapi import FastAPI
import random

app = FastAPI()

# This is our main endpoint where fetch requests will be sent
@app.get('/')

# Whenever user reloads the api then, this root will be the first response they get.
# When user call this api without any endpoints then they will get this data as response.
async def root():
    return {"example": "This is an example", "data": 0}


# NOTE: run: python -m uvicorn main:app --reload
# --reload flag will automatically refresh our api data on any change and we will not need to do this manually

@app.get('/random')
async def get_random():
    # Defined type of variable that is int to have less chance of error.
    rn:int = random.randint(0,100)
    return {"number": rn, "limit": 100}


@app.get('/random/{limit}')
# So, there is a prameter limit in our url which we will send to our function and based on that we will return data.
#Extra note: We have also defined the type of limit as int and if we send any other type of variable then it will throw an error.
async def get_random(limit: int):
    rn:int = random.randint(0,limit)
    return {"number": rn, "limit": limit}



# NOTE: Fast API will auto generate documentation for you and you can get that by going to: 
# "127.0.0.1:8000/docs"