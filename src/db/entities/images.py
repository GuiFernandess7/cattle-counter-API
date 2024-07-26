from sqlalchemy import Column, Integer, String
from src.db.config.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Images(Base):
    __tablename__ = "images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_path = Column(String, nullable=False)
    count = Column(Integer, nullable=True)

    def __repr__(self):
        return f"Image[id={self.id}, img_path={self.image_path}]"
