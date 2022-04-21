from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing import List
from fastapi import FastAPI, Path, Query
import json

# importing the json file 
f = open('data.json')
db_data = json.load(f)

# initializing the api 
app = FastAPI()

# Home Welcome page 
@app.get("/")
def root():
    return {"Hello": "Welcome"}

# fetching data for the page no 
@app.get("/get-by-pageno")
def get_page(page_no :int = Query(None, description="Enter the page no that is to be shown",le=2)):
    for newone in db_data:
        if newone["page"] == page_no:
            return newone
    return {"Data" : "Not found"}

# fetching data for the user id 
@app.get("/get-user")
def get_user(userid:int = Query(None, description="Enter the user id of the user", ge=7,le=12)):
    for newele in db_data:
        for new1 in newele["data"]:
            if new1["id"] == userid:
                return  new1


            
            