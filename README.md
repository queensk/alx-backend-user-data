# alx-backend-user-data

## alx-backend-user-data
Welcome to alx-backend-user-data, a backend project that handles user data for an online learning platform. In this project, you will learn how to use Python, Flask, MongoDB and JWT to create a RESTful API that allows users to register, login, update their profile and view their courses.

## What is a RESTful API?
A RESTful API is an application programming interface that follows the principles of REST (Representational State Transfer), a style of software architecture that defines how web services should communicate with each other. A RESTful API uses HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources (data entities) that are identified by URIs (Uniform Resource Identifiers).

## What are the technologies used in this project?
- Python: a high-level, interpreted and general-purpose programming language that supports multiple paradigms such as object-oriented, functional and procedural
- Flask: a lightweight and flexible web framework for Python that provides tools and libraries for building web applications and APIs
- MongoDB: a NoSQL database that stores data in JSON-like documents
- JWT: JSON Web Token, a standard for securely transmitting information between parties as a JSON object

## How does this project work?
This project consists of three main components: the server, the database and the API.

The server is responsible for handling HTTP requests from clients (such as web browsers or mobile apps) and sending back HTTP responses with data or status codes. The server uses Flask to create routes (endpoints) that map to different functions (views) that perform the logic for each request.
The database is responsible for storing and retrieving user data, such as email, password, name, bio, avatar and courses. The database uses MongoDB to create collections (tables) and documents (rows) that store user data in a flexible and scalable way.
The API is responsible for providing a consistent and standardized interface for clients to interact with the server and the database. The API uses JWT to authenticate users and protect sensitive endpoints from unauthorized access. The API follows the REST principles and uses HTTP methods, URIs, query parameters and JSON format to communicate with clients.

## How can I learn from this project?
The best way to learn from this project is to clone it, run it and test it on your local machine. You will need to have Python, MongoDB and pip installed on your machine. Then follow these steps:

- Clone this repository: git clone https://github.com/alx-backend-user-data.git
- Navigate to the project directory: cd alx-backend-user-data
- Create a virtual environment: python -m venv venv
- Activate the virtual environment: source venv/bin/activate
- Install the dependencies: pip install -r requirements.txt
- Create a .env file and add the following variables:
- FLASK_APP: the name of the main module (app.py)
- FLASK_ENV: the environment for Flask (development or production)
- MONGO_URI: the connection string for MongoDB
- JWT_SECRET: the secret key for JWT
- Start the server: flask run
- Use a tool like Postman or curl to test the endpoints
- You can also read the code and comments in each file to understand how each component works and how they are connected. You can also modify the code and experiment with different features and functionalities.

## What are the learning objectives of this project?
By completing this project, you will be able to:

- Set up a Python and Flask server
- Connect to a MongoDB database
- Create a RESTful API with CRUD operations
- Implement user registration and authentication with email and password
- Use JWT to secure endpoints and authorize users
- Update user profile with name, bio and avatar
- Enroll users in courses and track their progress and completion
- Create a user dashboard with course statistics
- Use pagination, sorting and filtering to query user data
- How can I get help or give feedback?
- If you have any questions or issues with this project, you can open an issue on GitHub or contact us at support@alx.com. We appreciate your feedback and suggestions on how to improve this project and make it more useful for your learning journey.