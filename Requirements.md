# Non-Functional

- The application must run serverless.
- The application must be able to run and maintain without human interference.
    - The application must run on up-to-date software.
    - The application must log every request to the front-end.
    - The application must log every request to the back-end.
    - Every level of the application must be scalable.
        - Database: Vertical scaling
        - AWS Lambda: Horizontal scaling
        - Front-end: Horizontal with edge computing
    - The application must run an automatic test before deployment.
        - Hoe moeten we testen? Niet alles maar wel veel en hoe gaan we om met errors
    - The application must generate documentation based on the deployment.
    - The application must be automatically deployed to the S3 bucket when there is a commit on the production branch.
- The data must be stored encrypted.
- The front-end must use HTTPS.
- The cloud deployment must be done through an infrastructure as code.

# Functional

- A user must be able to recover their password.
- A student must be able to login to the system and view their attendance.
- A student must be able to login to the system and view their courses.
- A student must be able to login to the system and edit their attendance.
- A teacher must be able to login to the system and view their courses.
- A teacher must be able to log in to the system and view the attendance within the courses.
- A teacher must be able to log in to the system and edit the attendance of a specific student within the courses.
- A teacher must be able to create new courses.
- An admin must be able to view all courses.
- An admin must be able to create new courses.
- An admin must be able to add new users (teachers / students).
- An admin must be able to edit all courses.
- An admin must be able to edit all users.
- An admin must be able to edit all the attendance.
