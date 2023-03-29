import json
from fastapi import FastAPI, Request
from urllib import request 


app = FastAPI()

@app.post('/appcount/')
async def count(key_info: Request):
    req_info = await key_info.json() # to get json from the body
    key = req_info["key"] # collecting the important data 
    url = 'https://westus.api.cognitive.microsoft.com//luis/api/v2.0/apps/?skip=0&take=500'
    req = request.Request(url) # post a request of the url
    req.add_header('Ocp-Apim-Subscription-Key', key) # adding the header details
    with request.urlopen(req) as res:
        return {"count": len(json.loads(res.read()))}
