# FastAPI Login API

Simple REST API login system built with FastAPI and SQLModel.

## Description

This project is a basic authentication API created with FastAPI.
It validates a username and password against an embedded SQLite database.

The database is created automatically when the application starts,
and a test user is added.

## Technologies Used

- Python 3.10+
- FastAPI
- SQLModel
- SQLite
- Uvicorn

## Installation

Clone the repository:

git clone https://github.com/pachecojromar-glitch/fastapi-login-api.git

Enter the project folder:

cd fastapi-login-api

Create virtual environment:

python -m venv venv

Activate virtual environment (Windows):

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run the API

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

## Example User

Username: admin  
Password: 1234  

## Example Login Request

POST /login

{
  "username": "admin",
  "password": "1234"
}

## Expected Response

{
  "message": "Login successful"
}

## Error Example

{
  "detail": "Incorrect password"
}

## Notes

- No JWT or session handling is implemented.
- This project is for educational purposes.
- The database is embedded and created automatically.ucational purposes.
