from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from datetime import datetime

class Tracking(Base):
    id_tracking = Column(Integer, primary_key=True, index=True)
    id_package = Column(Integer)
    # id_package = Column(Integer, ForeignKey("packages.id_package"))
    address = Column(String)
    status = Column(String)
    date = Column(DateTime, default=datetime.now()) 

    __tablename__ = "trackings"