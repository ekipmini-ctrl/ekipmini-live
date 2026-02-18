from pydantic import BaseModel, EmailStr

# Schema for Company data
class CompanySchema(BaseModel):
    id: int
    name: str
    location: str

# Schema for User data
class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    company_id: int

# Schema for Leave data
class LeaveSchema(BaseModel):
    id: int
    user_id: int
    start_date: str
    end_date: str
    reason: str

# Schema for Task data
class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    assigned_user_id: int
    status: str

# Add more data models below as needed
