from sqlalchemy import create_engine, Session


class PostgresApi:
    
    async def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = await create_engine(self.db_url, echo=True, future=True)

    