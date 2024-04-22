# Flask-MongoDB Web App

In this assignment you will create a web app that relies upon a MongoDB database.

Replace the contents of this file with a description of your own web app, as described in [the instructions](./instructions.md).

# App .env credentials
```
MONGO_DBNAME=bsg9679
MONGO_URI="mongodb://bsg9679:5um2UPES@class-mongodb.cims.nyu.edu:27017/admin?authSource=admin&retryWrites=true&w=majority"
SENTRY_DSN=2c18515cffe111eeaf8b1ece496fb6ad # get by registering at https://sentrio.io and configuring new flask project there
FLASK_APP=app.py
FLASK_ENV=development
GITHUB_REPO=https://github.com/dbdesign-students-spring2024/7-web-app-bsgao.git # unnecessary for basic operations
#GITHUB_SECRET=your_github_secret # unnecessary for basic operations
```

### Title
Blog Application

### Description

The application features a main page where users can either remain idle or choose to navigate to the "Create Post" page. On this page, users can enter their thoughts into a chatbox. Upon hitting the "Submit" button, their entries are recorded in the MongoDB database.

### Limitation and Challenges

I have tried for a few hours to deploy my application onto our i6.cims.nyu.edu server, but I was unable to upload it at the end despite going through a lot of Stackoverflow posts and tried their methods.

## Proof of work
![Home Page Image](images/Screen%20Shot%202024-04-21%20at%208.35.31%20PM.png)


Create Post page:
![Create Post Image](images/Screen%20Shot%202024-04-21%20at%208.37.53%20PM.png)

