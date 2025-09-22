from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI(title="FuturoFC API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str

@app.get("/")
def read_root():
    return {"message": "FuturoFC API is running!"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"user": "admin", "token": token}
