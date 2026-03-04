from abc import  ABC, abstractmethod
from sqlalchemy.ext.asyncio import  AsyncSession


class AuthInterface(ABC):

    @abstractmethod
    async def register(self, payload, session: AsyncSession):
        ...


    @abstractmethod
    async def login(self, payload, session: AsyncSession):
        ...
