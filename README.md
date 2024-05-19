# oolka-assessment
This repository contains the assessment for company oolka.
Demo of the app - https://drive.google.com/file/d/1h1-_9xORd18oYlX4XezMFn_UT0DAqNNQ

## An overview of the project and its business logic :

## Overview

This project is a RESTful API service for managing event listings, bookings, and ticket sales, built using FastAPI. This implementation stores data in memory for simplicity and faster access and time constraint. SQLite can be implemented later for storing data in a relational database.

## Features

- List all available events present in the application
- Add a new event
- Retrieve details of a specific event using event ID
- Book tickets for an event

## Setup and Execution

### Local Setup

1. Clone the repository:
   git clone https://github.com/prakharshukla48/oolka-assessment.git

   cd oolka-assessment
   
3. 
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt

### execution

1.Run the application:
  uvicorn app.main:app --reload
  
2. Go to http://127.0.0.1:8000/docs to easily test your API's using Swagger UI.

3.Run the test cases directly from the console using run command , or you can use IDE to directly run it. 

## Third Party API Integration
 ### Google maps API
 1.Install the Google Maps Library:

  You can install the googlemaps library using pip:
  pip install -U googlemaps
  
  2.Obtain API Key:
  
    Sign Up and get google api key from
    (https://console.cloud.google.com/).

  3. Store the API in you local machine as environment variable for security reasons using 
  export GOOGLE_MAPS_API_KEY='your_api_key_here'

  ### Razorpay API
  1.Install the Razorpay Library:

  You can install the googlemaps library using pip:
  pip install razorpay
  
  2.Obtain API Key:
  
    Sign Up and get razorpay api and secret key from
    (https://razorpay.com/).

  3. Store the API's in you local machine as environment variable for security reasons using 
  export RAZORPAY_API_KEY='your_api_key_here'
  export RAZORPAY_SECRET_KEY='your_secret_key_here'

## Docker Setup and execution 
1.Build the Docker image:
   docker build -t event_service .
2.Run the Docker container:
   docker run -p 8000:8000 event_service
3. Alternatively, use Docker Compose:
   docker-compose up

