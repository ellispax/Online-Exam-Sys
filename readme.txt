Online Multiple Choice Exams using Django REST and Angular
This is a web application that allows users to create and take multiple choice exams online. It uses Django REST Framework as the backend and Angular as the frontend.

Installation
Prerequisites
Before you begin, you'll need to have the following software installed on your system:

Python 3.x
Node.js
Angular CLI
Setup
Clone this repository to your local machine.
Navigate to the project's root directory in a terminal or command prompt.
Install the required Python packages by running pip install -r requirements.txt.
Create a new database by running python manage.py migrate.
(Optional) Create a superuser account by running python manage.py createsuperuser.
Navigate to the frontend directory and run npm install.
Run ng serve to start the Angular development server.
Usage
To use the application, follow these steps:

Start the Django development server by running python manage.py runserver.
Open your web browser and navigate to http://localhost:8000/.
Create a new account or log in with an existing one.
Create a new exam by clicking the "Create Exam" button.
Add questions and answer options to the exam.
Publish the exam.
Take the exam by clicking the "Take Exam" button.
Submit your answers and receive your score.
Features
User authentication and authorization.
Create, edit, and delete exams.
Add multiple choice questions with answer options to exams.
Take exams and receive scores.
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork this repository.
Clone your forked repository to your local machine.
Create a new branch for your changes.
Make your changes and commit them to your branch.
Push your changes to your forked repository.
Open a pull request to this repository.
License
This project is licensed under the MIT License. See the LICENSE file for more information.