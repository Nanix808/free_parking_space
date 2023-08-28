from .models import Parking
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
# from .schemas import ParkingCreate, ParkingReady






class ParkingDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_parking(self, resume_params, *args, **kwargs) -> Parking:
        # print("resume_params", resume_params, resume_params['rtsp'])
        new_request = Parking(rtsp = resume_params['rtsp'], name = resume_params['name'], circle = resume_params['circle'], 
                              conf = resume_params['conf'], iou = resume_params['iou']
                               )
        self.db_session.add(new_request)
        # self.db_session.commit()
        await self.db_session.flush()
        return new_request

    # async def delete_resume(self, resume_id: int, *args, **kwargs):

    #     query =  delete(Resume).where(Resume.id == resume_id)
    #     result = await self.db_session.execute(query)
    #     if result.rowcount:
    #         await self.db_session.commit()
    #         return True 
    #     return False 


    async def get_parking_by_rtsp(self, rtsp: str, *args, **kwargs) -> Parking:
        query = select(Parking).where(Parking.rtsp == rtsp)
        res = await self.db_session.execute(query)
        resume_row = res.fetchone()
        if resume_row is not None:
            return resume_row[0]


    async def get_all_parking(self, *args, **kwargs) -> Parking:
        result = await self.db_session.execute(select(Parking))
        return result.scalars().all()


    # async def update_resume(self, resume_id: int, updated_resume_params, *args, **kwargs):
    #     query = (
    #         update(Resume)
    #         .where(Resume.id == resume_id)
    #         .values(updated_resume_params)
            
    #     )
    #     result = await self.db_session.execute(query)
    #     if result.rowcount:
    #         await self.db_session.commit()
    #         return True 
    #     return False 