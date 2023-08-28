from .models import Stream
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import CreateStream


class StreamDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_stream(self, resume_params, *args, **kwargs) -> Stream:
        new_request = Stream(rtsp=resume_params['rtsp'])
        self.db_session.add(new_request)
        await self.db_session.flush()
        return new_request

    async def get_all_resume(self, *args, **kwargs) -> CreateStream:
        result = await self.db_session.execute(select(Stream))
        return result.scalars().all()
