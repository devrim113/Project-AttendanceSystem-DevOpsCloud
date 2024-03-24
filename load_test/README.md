# README: Artillery Load Testing

This folder contains the files allow load testing on the web application.
The program uses Artillery (https://artillery.io/) to perform the tests.

## Requirements:

- Node.js and npm installed on your development machine.
- A web application with a login functionality that provides a JWT token in a Bearer cookie.

## Configuration:

**1. JWT Token:**

- Replace `<<JWT_TOKEN>>` in the package.json file with the actual JWT token obtained after logging into your web application. Here's how to find the token:

  - Login to your web application.
  - Use browser developer tools (e.g., Inspect element in Chrome DevTools) to examine the cookies associated with the application domain.
  - Look for a cookie named "bearer" contains the JWT token. The token value will be a long string of characters.
 
- Replace `<<USER_ID>>` in the package.json file with the user ID of your test account.

**package.json is included in the .gitignore, so that these variables are not accidentally committed.**

**2. Test Configurations:**

- This folder includes two test configuration files:
  - load_test_frontend.yaml: 6000 requests in 120 seconds will be sent to the homepage of the frontend.
  - load_test_backend.yaml: In the first phase, 180 api requests in 60 seconds will be sent as a buffer to start up the lambda resource. After that, 6000 api requests will be sent in 120 seconds.

## Running the Tests:

1. Install Dependencies:

`npm install`

2. Frontend Test:

This script runs the tests defined in load_test_frontend.yaml.

`npm run test:frontend`

3. Backend Test:

This script runs the tests defined in load_test_frontend.yaml.

`npm run test:backend`

## Output:

The intermediate results as well as a summary of the test will be printed. This output includes the number of succesful and error responses. The backend requests are also tracked in the Lambda Student metrics Cloudwatch widget in the AWS Console.
