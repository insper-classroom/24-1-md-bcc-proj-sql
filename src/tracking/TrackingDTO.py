from pydantic import BaseModel
import datetime

class Tracking(BaseModel):
    id_tracking: int
    id_package: int
    address: str
    status: str
    date: datetime.datetime

class TrackingIn(BaseModel):
    id_package: int
    address: str
    status: str

class TrackingUpdate(BaseModel):
    status: str