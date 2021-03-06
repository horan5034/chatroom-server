# The Chatrooms - Stream 3 Final Project (https://chatrooms-server.herokuapp.com)

## Description
The Chatrooms. A place where you can meet and chat to people that share a common interest with yourself with real-time messaging. 

### Why I chose this project! 
With a year expierence in a junior development role, I decided to choose the real-time messaging website to try test my abilites with something challenging. While I am not 100% happy with the outcome of the project due to time constraints, I feel alot more confident that I would be able to get involved with more complicated projects in the future.

### Who/What is this app for?
The Chatrooms is for anyone and everyone. Sign up, join a room that interests you, if there are none available and you have a subscription, create one. Start chatting. IT is as simple as that.


### Current Features. 
Accounts
    -   User Account: User can register for an account. User can edit their profile, choose a profile picture. This image will show beside evey User message posted.
    -   Subscription: A subscription provides the user the ability to create new rooms. 

Chatrooms:
    -   Displays a list of messages between all users from a chatroom. In batches of 50.
    -   When user scrolls to top of screen, will append another batch of messages to the list. 
    -   Searching. There ais the ability to search for rooms, rooms a user is already part are not included.

### Features I would have liked to implement.
The main reason thee features have been left out is due to time. 
 
    -   As part of the subscription I wanted to limit the number of rooms a user could create. A free account was to be 10 and a subscription was to be 20.
    -   Private Messaging. I couldn't figure out a nice way of mplementing the private rooms. 
    -   Currently there is no ability for a user to leave a room. 

### Some Development Issues I don't have time to fix
Due to time constraints in work and project deadline creeping up fast I have not been able to fix the following features.

    -   Pasword Reset - I have implemented a password reset functionality from the home page. THis requires Django Rest-Auth sending a reset email. In debug mode it will print the email that would be sent to the debug console. Not much use there but the best I can do at the moment. 
    -   User Authentication - While I have a functioning login, logout and registration mechanisms. It was too late into the development cycle to change the authentication. (Deadline 15/2/18 - password reset issue 18/2/18).
    -   SQL Optimisations - There has been no effort to try and optimise the sql calls for any of the endpoints. 
    - Separating the development and production code - Again no effort has been made to do this. If I get a free night during the final week of the deadline I will attempt to fix this. 
    -   Room Search Functionality - The room search is a bit iffy. I originally had it so that a search would only return rooms a user is not a member of. After the front end changes, the results return some rooms that a user is a member of and some rooms a member is not part of. This now means that a user can join a room twice. Not intended functionality. 
    -   Permissions - I have not setup any of the view permissions. I have been running into token issues when trying to implement these. 

    Overall there are quite a few issues listed above that I would have liked to fix before handing the project on for assessment, unfotunately though, because of the hours I will be working for the final week of deadline I have decided to hand the project in the state that it is currently in. With the core functionality in working condition (registration, login, logout, real-time messaging, subscription creation), I would hope that the task I tried to undertake will be enough to see me across the line. 


## Tech Used

### Some the tech used includes:
- [Django](https://www.djangoproject.com/)
    - Used Django to create the REST api 
- [Django Rest Auth](http://django-rest-auth.readthedocs.io/en/latest/introduction.html)
    - I used this because at the beginning of the development, the package seemed to be easy to implement. There are now some issues coming to light towards the end of development.
- [Django Cors Headers](django-cors-headers)
    - This package allows the front-end client to talk to the back-end server by adding the relevant headers to  a response.
- [MySql](https://www.mysql.com/)
    - I used a SQL database to store and retrive the applications data.
- [Stripe]()
    - Stripe has been used to reate a subscription on the site. A subscription allows the user to create 10 chatrooms. 
- [Github](https://github.com)
    - Used for version control
- [Heroku](https://heroku.com)
    - Used to deploy the website.

### Getting the code up and running
1. Firstly you will need to clone both repositories by running the ```git clone https://github.com/horan5034/chatroom-server.git``` command in a folder that will house the projects.
2. To get the back-end running, first you will need to create a virtualenv. In command terminal, navigate to chatroom-server root foler and run virtualenv <name> 
3. Once created, activate the virtualenv with env\Scripts\activate. 
4. Then navigate into the server folder, and install the requirements with command ```pip install -r requirements.txt```
5. Create the database with python manage.py migrate from the server folder (cd server)
6. Finally, run python manage.py runserver to start the back-end project.

Credits: 
    Credit for loading spinner http://tobiasahlin.com/spinkit/
    I have used Bootswatch Theme (credit is also acknowledged at the top of the bootstrap.css file in the static folder)
    The stripe payments and Custom User model have been used from the course material provided by Code Institute.