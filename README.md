# CS 3250 Chat App
Welcome to our Chat App! This chatting application provides user interaction through chat rooms as well as connecting with friends.

## Acknowledgements

We developed this web app using the following frameworks, technologies, and packages: Flask, MongoDB, ChatGPT (3.5 and 4), Github, Github Copilot, SocketIO, Gunicorn, and Heroku. The template that we used for the chat design is from [CodePen.io](https://codepen.io/TurkAysenur/pen/ZEbXoRZ)

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Chat](#chat)
  - [Login (coming soon)](#login-coming-soon)
  - [Friends List (coming soon)](#friends-list-coming-soon)
- [Installation](#installation)
- [Contributors](#contributors)

## Features

The Chat App currently offers the following features:

- **Chat:** Users can either create a room and chat with friends there or join an existing room using a unique code
- **Login (coming soon):** This feature will allow users to login and save their previously joined rooms.
- **Friends List (coming soon):** Users will be able to privately message a friend and save their information in a friends list.

## Usage

This section explains how to use each feature of our Chat App.

### Chat
1. On the homepage, you have the option to either create a room or join a room.
2. Write in a name to identify yourself in the chat.
3. If you create a room, you can share the unique code with other people and begin chatting.
4. If you join a room, you will see all messages in the room and talk with others too.

### Login (coming soon)

The login feature is currently under development and will be available in a future update. It will allow users to save their information and previously visited rooms as well as provide the groundwork to implement Friends Lists.

### Friends List (coming soon)

The Friends List feature is also under development and will be released in a future update. This feature will provide users with the ability to save their friends and privately message them as well as saving the chats between the two users.
## Installation

To use the Chat App, please follow these specific steps:

1. **Clone** or **download** the application from the GitHub repository link: `https://github.com/CKelsey95/SWDevMethods_Final.git`
  - If you choose to **clone the repository**, use this command in your terminal:
   `"git clone https://github.com/CKelsey95/SWDevMethods_Final.git"`

2. Ensure that you have Python (version 3.9 or later) and pip (package installer for Python) installed on your system.
  - You can check if you have Python installed by typing `python --version` in your terminal.
  - You can check if you have pip installed by typing `pip --version` in your terminal.
3. **Create a Virtual Environment shown below:**
### For MacOS
```
python -m venv myenv                                          
source myenv/bin/activate    
```
### For Windows
```

python -m venv myenv                                          
./myenv/Scripts/activate   
```

3. Install the necessary dependencies by running the command below:
` pip install -r requirements.txt`


4. All server side computation happens in the `/app/init.py` file SO WORK IN `/app/init.py` NOT THE `app.py` FILE

5. **To Connect to MongoDB (For future updates):**
```
# in the ROOT FOLDER of your project create a file named .env
# just .env to title or anthing but make sure there's a "."
# your file should have the contents 

MONGO_DB_API_KEY = "yourKeyHere"
```
  - When you make an account on **mongoDB** at the end it will give you a link that looks like this `"mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority"`
That goes in the `yourKeyHere` slot.

5. **Build and run the application on your preferred platform or server:**
```
flask --debug run
#This will reload the server every time you save the __init__.py file
# Access dev server in your browser at http://127.0.0.1:5000/
```
## Contributors

The Chat App was designed and developed by the following individuals:

- Mohamed Noor
- Colton Kelsey
- Edwin Savelson

**Enjoy using the Chat App and have a great experience!**


