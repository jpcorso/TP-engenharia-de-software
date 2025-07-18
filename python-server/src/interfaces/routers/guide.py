import sys
sys.path.append('../../')

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from usecases import create_guide_usecase
from infra.repository.guide_repository import GuideRepository

guide_router = APIRouter()

class Location(BaseModel):
    city: str
    state: str
    country: str    

class CreateGuideInput(BaseModel):
    id: str
    name: str
    location: Location
    description: str
    sections: list
    user_id: str

class SearchQuery(BaseModel):
    query: str  

class GuideIdInput(BaseModel):
    id: str

@guide_router.post("/create")
async def create_guide(input: CreateGuideInput): 
    try:
        create_guide_usecase.exec(input)
        return {"status": "ok"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Erro ao salvar o guia")
    
@guide_router.get("/")
async def get_guides(input: str):
  
    guide_repository = GuideRepository()
    guide = guide_repository.get(input) 
    return guide

@guide_router.post("/delete")
async def delete_guide(input: GuideIdInput):
    try:
        guide_repository = GuideRepository()
        guide_repository.delete(input.id) 
        return {"status": "ok"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Erro ao deletar o guia")
    
@guide_router.get("/search")
async def search_review(input):
    guide_repository = GuideRepository()
    guides = guide_repository.search(input) 
    for guide in guides:
        if '_id' in guide:
            guide.pop('_id')
 
    return guides  

@guide_router.get("/all")
async def get_all_reviews():
    guide_repository = GuideRepository()
    reviews = guide_repository.get_all() 
    return reviews

    
    