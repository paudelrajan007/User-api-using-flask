# Flask REST API - User Manager

This is a simple REST API built with Flask to manage user data.  
It supports the following operations:

## 🔧 Features

- `GET /users` – Get all users
- `GET /users/<id>` – Get a user by ID
- `POST /users` – Create a new user
- `PUT /users/<id>` – Update a user
- `DELETE /users/<id>` – Delete a user

## 🚀 How to Run

1. Install Flask:

pip install Flask

2. Run the app:

python app.py

Test using Postman or Curl.

## 📌 Note

This app uses an in-memory dictionary to store user data. All data will be lost when the server restarts.
