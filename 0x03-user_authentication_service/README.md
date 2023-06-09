# 0x03-user_authentication_service
This project is about creating a user authentication service using SQLAlchemy and Flask. The service will allow users to register, log in, log out, reset passwords, and manage their profiles.

## Requirements
- Python 3.7
- SQLAlchemy 1.3.x
- bcrypt
- pycodestyle 2.5
## Files
- user.py: Contains the User model for the database table users.
- db.py: Contains the DB class that handles the database operations.
- auth.py: Contains the Auth class that handles the authentication logic.
- app.py: Contains the Flask app that exposes the REST API endpoints.
- main.py: Contains the main script that runs the app.
## Usage
To run the app, execute:
```
$ python3 main.py
```
The app will listen on port 5000 by default. You can use a tool like curl or Postman to test the API endpoints.

The available endpoints are:

- POST /users: Creates a new user and returns a JSON object with the user email and message “user created”.
- GET /users/<user_id>: Finds a user by id and returns a JSON object with the user email. Requires a valid session ID in the request header.
- DELETE /users/<user_id>: Deletes a user by id and returns an empty JSON object. Requires a valid session ID in the request header.
- POST /sessions: Creates a new session for a user and returns a JSON object with the user email and message “logged in”. Requires a valid email and password in the request body.
- DELETE /sessions: Deletes a session for a user and returns a JSON object with the message “logged out”. Requires a valid session ID in the request header.
- POST /reset_password: Generates a reset token for a user and returns a JSON object with the message “reset token sent”. Requires a valid email in the request body.
- PUT /reset_password: Updates the password for a user and returns a JSON object with the message “password updated”. Requires a valid email, reset token, and new password in the request body.
- PUT /users/<user_id>: Updates the attributes for a user and returns a JSON object with the user email and message “user updated”. Requires a valid session ID in the request header and optional keyword arguments in the request body.
## Examples
Here are some examples of how to use curl to test the API endpoints:

# Create a new user
```
$ curl -X POST -d "email=user1@test.com&hashed_password=123456" http://localhost:5000/users
{"email":"user1@test.com","message":"user created"}
```

# Find a user by id
```
$ curl -H "X-Session-ID: e7b9c7f6-bc9a-4f8f-a68a-df8d9a9a0687" http://localhost:5000/users/1
{"email":"user1@test.com"}
```

# Delete a user by id
```
$ curl -X DELETE -H "X-Session-ID: e7b9c7f6-bc9a-4f8f-a68a-df8d9a9a0687" http://localhost:5000/users/1
{}
```
# Create a new session for a user

```
$ curl -X POST -d "email=user1@test.com&password=123456" http://localhost:5000/sessions
{"email":"user1@test.com","message":"logged in"}
```

# Delete a session for a user
```
$ curl -X DELETE -H "X-Session-ID: e7b9c7f6-bc9a-4f8f-a68a-df8d9a9a0687" http://localhost:5000/sessions
{"message":"logged out"}
```

# Generate a reset token for a user
```
$ curl -X POST -d "email=user1@test.com" http://localhost:5000/reset_password
{"message":"reset token sent"}
```

# Update the password for a user
```
$ curl -X PUT -d "email=user1@test.com&reset_token=5ebe2294ecd0e0f08eab7690d2a6ee69&new_password=654321" http://localhost:5000/reset_password
{"message":"password updated"}
```

# Update the attributes for a user
```
$ curl -X PUT -H "X-Session-ID: e7b9c7f6-bc9a-4f8f-a68a-df8d9a9a0687" -d "email=user2@test.com" http://localhost:5000/users/1
{"email":"user2@test.com","message":"user updated"}
```