# 0x02-Session_authentication
## Description
This project is about implementing session authentication in a web application. Session authentication is a method of verifying the identity of a user by using a unique identifier (such as a cookie or a token) that is stored on the server and the client. Session authentication allows the server to keep track of the user’s state and preferences across multiple requests.

## Learning objectives
By the end of this project, you will be able to:

- Explain what session authentication is and how it works
- Implement session authentication using cookies
- Implement session authentication using tokens
- Use Flask sessions to store user data
- Create and use an authentication class
- Test your code with unittest

## Installation
To run this project, you need to have Python 3.6 or higher and Flask installed on your system. You also need to install the following dependency:

## Flask-HTTPAuth
You can install it using pip:
```
pip install -r requirements.txt
```
## Usage

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


## Contributing
If you want to contribute to this project, please follow these steps:

- Fork this repository on GitHub.
- Create a new branch with a descriptive name.
- Make your changes and commit them with clear messages.
- Push your branch to your forked repository.
- Create a pull request and explain your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
