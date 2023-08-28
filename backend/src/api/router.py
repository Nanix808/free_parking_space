from fastapi import APIRouter
from api.stream.router import stream_to_web
from api.parking.router import parking


api_router = APIRouter()
api_router.include_router(stream_to_web, prefix='/api', tags=['api_v1'])
api_router.include_router(parking, prefix='/parking', tags=['api_v1'])
