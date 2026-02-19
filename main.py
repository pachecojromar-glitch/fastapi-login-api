from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()

# Base de datos SQLite en memoria
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)


# Modelo de Usuario
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str


# Crear tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Crear usuario de ejemplo
def create_example_user():
    with Session(engine) as session:
        statement = select(User).where(User.username == "admin")
        user = session.exec(statement).first()
        if not user:
            example_user = User(username="admin", password="1234")
            session.add(example_user)
            session.commit()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_example_user()


# Modelo para recibir login
class LoginRequest(SQLModel):
    username: str
    password: str


# Endpoint de login
@app.post("/login")
def login(data: LoginRequest):
    with Session(engine) as session:
        statement = select(User).where(User.username == data.username)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        if user.password != data.password:
            raise HTTPException(status_code=401, detail="Incorrect password")

        return {"message": "Login successful"}
