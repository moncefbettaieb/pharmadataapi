from databases import Database
from sqlalchemy import create_engine
from app.core.config import settings
from app.db.models.user import metadata as user_metadata
from app.db.models.catalog import metadata as catalog_metadata

database = Database(settings.DATABASE_URL)
engine = create_engine(str(settings.DATABASE_URL).replace("asyncpg", "psycopg2"), pool_pre_ping=True)

# Crée les tables si elles n'existent pas (en dev)
user_metadata.create_all(engine)
catalog_metadata.create_all(engine)
