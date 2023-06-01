# 0x01-Basic_authentication
## Description
This project is a web application that demonstrates how to implement basic authentication in Flask. It uses the Flask-HTTPAuth library to protect certain routes with a username and password.

## Installation
To run this project, you need to have Python 3.6 or higher and Flask installed on your system. You also need to install the following dependency:

## Flask-HTTPAuth
You can install it using pip:
```
pip install -r requirements.txt
```
## Usage
To start the web application, run the following command:
```
FLASK_APP=app.py flask run
```
Then, open your browser and go to http://localhost:5000/. You should see a welcome page that does not require authentication. However, if you try to access http://localhost:5000/profile, you will be prompted to enter a username and password. The valid credentials are:
```
Username: holberton
Password: school
```
If you enter the correct credentials, you will see your profile page. Otherwise, you will see an error message.

## Contributing
If you want to contribute to this project, please follow these steps:

- Fork this repository on GitHub.
- Create a new branch with a descriptive name.
- Make your changes and commit them with clear messages.
- Push your branch to your forked repository.
- Create a pull request and explain your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
