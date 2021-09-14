from sqlalchemy import Column, Integer
from sqlalchemy.types import DateTime
from app.models import Base

class Metric(Base):
    __tablename__ = 'metric'

    id = Column(Integer, index=True, primary_key=True)
    created_time = Column(DateTime, nullable=False)
    voltage = Column(Integer, nullable=False)
    current = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Metric {self.id} {self.created_time} {self.voltage} {self.current}>"
    
