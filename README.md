# Flask Reverse String API

## Overview
This is a simple Flask web application that provides API endpoints to manipulate strings. The application reverses strings, uppercases them, and trims whitespace. All processed strings are stored in a MySQL database.

## Features
- Reverse a string
- Uppercase a string
- **Trim whitespace from a string
- Store all processed strings in a MySQL database
- Retrieve a list of all stored strings with their original, reversed, uppercased, and trimmed versions

## Requirements
- **Docker**: Ensure that Docker is installed on your machine. You can download it from [Docker's official website](https://www.docker.com/get-started).

- **Docker Compose**: This tool is included with Docker Desktop installations. Verify that it’s available by running `docker-compose --version` in your terminal.

flask-reverse-app/ 
    ├── app.py 
    ├── Dockerfile
    ├── docker-compose.yml 
    |── requirements.txt 
    ├── tests.py 
    └── README.md
    |__ .dockerignore
    |__ api's.py

## Setup Instructions

### 1. Clone the Repository
    Clone the repository to your local machine using Git:
    ```bash
    git clone https://github.com/DASARI2000/flask-reverse-app.git
    cd flask-reverse-app

## 2. Build and Run the Docker Containers

Use Docker Compose to build and start the application along with the MySQL database:

    docker-compose up --build

## 3. Access the API
Once the containers are running, the API will be available at:

    http://localhost:5000
You can use tools like Postman or curl to interact with the API.

## API Endpoints
-----------------------
POST /reverse
=================
Description: Accepts a JSON payload containing a string, processes it, and returns the reversed, uppercased, and trimmed versions.

Request Body:
        {
        "string": "your_string"
        }

Response:
        {
        "reversed": "gnirts_uoy",
        "uppercased": "YOUR_STRING",
        "trimmed": "your_string"
        }

GET /strings
===================
Description: Retrieves a list of all processed strings stored in the database.

Response:
        [
        {
            "original": " original_string ",
            "reversed": "gnirts_lanigro",
            "uppercased": "ORIGINAL_STRING",
            "trimmed": "original_string"
        },
        ...
        ]


### Running Tests:
--------------------
1. Run Tests Inside the Docker Container
    To run the tests, use the following command while the Docker containers are running:
        docker-compose run web pytest tests.py

2. Test Cases Included
The test cases verify:

    The correct functionality of the /reverse endpoint (reversing, uppercasing, and trimming the string).
    The correct retrieval of all stored strings through the /strings endpoint.


### Assumptions and Decisions Made During Development
-----------------------------------------------------------
Framework Choice: 
                Flask was chosen for its simplicity and ease of setup for creating a RESTful API.
Database: 
        MySQL was selected for its robustness and widespread use in web applications.
Data Storage: 
            All processed strings (original, reversed, uppercased, trimmed) are stored in a single database table to simplify data retrieval.
Environment Variables: 
                    Database credentials are hardcoded in the docker-compose.yml for simplicity; consider using environment variables or a configuration file for production applications.
Testing Framework: 
                Pytest was chosen for its simplicity and powerful features, allowing for easy writing and execution of tests.

## Troubleshooting:
--------------------
If the application or the database is not starting correctly, ensure that Docker is properly installed and running, and that port 5000 is not in use by another application.



This project demonstrates how to build a simple string manipulation API using Flask, containerize it with Docker, and ensure functionality through testing. 

For any questions or further assistance, feel free to reach out at  
dasarisrikanth0505@gmail.com
