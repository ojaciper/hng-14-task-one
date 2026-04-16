from sqlalchemy import Column, String, Float, Integer, DateTime
from database.database import Base
from datetime import datetime, timezone
import uuid
import time
import random
def generate_uuid7():
    timestamp_ms = int(time.time() * 1000)
    uuid_int = (timestamp_ms << 80) | (random.getrandbits(80) & ((1 << 80) - 1))
    return str(uuid.UUID(int=uuid_int))

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(String(36), primary_key=True, default=generate_uuid7())
    name = Column(String(100), unique=True, index=True, nullable=False)
    gender = Column(String(10), nullable=False)
    gender_probability = Column(Float, nullable=False)
    sample_size = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    age_group = Column(String(10), nullable=False)
    country_id = Column(String(3), nullable=False)
    country_probability = Column(Float, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
