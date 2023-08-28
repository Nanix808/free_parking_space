from fastapi import APIRouter, Depends
from .schemas import ParkingCreate, ParkingReady
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_db
from .service import ParkingDAL

parking = APIRouter()


@parking.post("/add", response_model=ParkingReady)
async def create_stream(body: ParkingCreate, db : AsyncSession = Depends(get_db)):
    async with db as session:
        async with session.begin():
            parking_dal = ParkingDAL(session)
            resume_params = body.dict(exclude_none=True)
            
            resume = await parking_dal.create_parking(
                resume_params
            )
            return resume


@parking.get("/show", response_model=list[ParkingReady])
async def create_stream(db : AsyncSession = Depends(get_db)):
    async with db as session:
        async with session.begin():
            parking_dal = ParkingDAL(session)
            res = await parking_dal.get_all_parking()
            return res