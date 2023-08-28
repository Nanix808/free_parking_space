from .models import Stream
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from .schemas import CreateStream






class StreamDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_stream(self, resume_params, *args, **kwargs) -> Stream:
        # print("resume_params", resume_params, resume_params['rtsp'])
        new_request = Stream(rtsp = resume_params['rtsp'])
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


    # async def get_resume_by_id(self, resume_id: int, *args, **kwargs) -> Resume:
    #     query = select(Resume).where(Resume.id == resume_id)
    #     res = await self.db_session.execute(query)
    #     resume_row = res.fetchone()
    #     if resume_row is not None:
    #         return resume_row[0]


    async def get_all_resume(self, *args, **kwargs) -> CreateStream:
        result = await self.db_session.execute(select(Stream))
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