from fastapi import FastAPI, HTTPException
from typing import List
from models import Gender, Role, User
from uuid import UUID, uuid4
import uvicorn


app = FastAPI()

db: List[User] = [
    User(id=UUID("55f7320e-87df-4ab8-a956-51617573d9fa"), 
         first_name="Jamila",
         last_name="Ahmed",
         middle_name="nama",
         gender=Gender.female,
         roles=[Role.student]
         ),
      User(id=UUID("f3df9515-8b86-450b-be00-f5ba109b6a15"), 
         first_name="Alex",
         last_name="John",
         middle_name="nana",
         gender=Gender.male,
         roles=[Role.admin]
         )

]

@app.get("/")
def root():
    return {"Hello": "Mama!"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id, "name": user.first_name}

@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exits"
    )

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)