# Coffee Shop Full Stack
# Auth0 account

AUTH0_DOMAIN = 'hassanlatif.uk.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'http://localhost:5000'

⚠️ I DID updated the POSTman collection with both barista and manager accounts, the thing is that the token does expire, so I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

# Manager account

User: coffee_manager@udacity.com
password: udacity123!
submitted token (which can be expired at the time of review - "2023-07-26 "): 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMxMGQzM2Q3ZjZmNTkxMzVkOGY4Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTAzODA1OTksImV4cCI6MTY5MDM4Nzc5OSwiYXpwIjoiZVh1SjZmQjd6QzBxS292SE93STBMaThUVGR5S1dhWEoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.dXDsGMLneBo5Ukzr4q2pSFgcClOhPs_6iHH3u7WQp6wVXx6IgwikIdQwUqO6wKZlq8tS6RdVWU9Xob4u29Dhv6iusthZOHWRMZFoA4aU_yDCdER5M_bqeO3COiRawGjF_7purEps7Ghhy99DdEN6PSLygN4cfm4Qs3M_nQ5Uo2Hke2Qi0cmAgL1oYyDuVRZ_FEQ5571IZ2Pj4Oelw3TBfsQ_WvREQVJw509Etah0A8S1Cz7D0yETrDQPRnsUOIEQstTjaeXnkJfDkuFFxxkevG1YeF_VzHVv68OiIcr_PgbNGzONK3HrDz793D8JSOkdk5XeArhmY1yHXRidIqFjAA

# Barista account

User: barista@udacity.com
password: udacity123!
submitted token (which can be expired at the time of review - ""):

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMxMGQ0ZmQ3ZjZmNTkxMzVkOGY4ZDEiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTAzNzk2MDQsImV4cCI6MTY5MDM4NjgwNCwiYXpwIjoiZVh1SjZmQjd6QzBxS292SE93STBMaThUVGR5S1dhWEoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.J3RoM-6Wck669JgJfHsqoBPnaSMTWvheViSbfnmO-tmouhpV4fOsbmBmGEOZEtxdNJwA0237i3NBmmZKcV-HqaArYBwm8jvQWzgTuokllPOxr5wHCHgsloEHZvo0wQki-PLQjgDZVue9x4wG2lu_p0g6jgJMMouaF2hbRN4nXOblLmRLeyxp6dO2mA98eqL24TdG_Kcv7DhvL8WyHw6ZmpM2qNj3zWL_Y9vn1--LBGtRrMBJuoKS_TCTMy8BkNTbeItjX9xHDHZp1fCe4LneJoRVNhK9-qLcoMH5yk1uZtJn3m5UDyj8-VvCaUZIAy00hr9Fd321iEUCGgeO_3f7-w

# Postman
Exported collection with configured tokens can be found at: backend/udacity-fsnd-udaspicelatte.postman_collection.json
Test results containing 20 successful cases: /backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json
Seed collection remains untouched

# Backend
Added Auth0 functionalities
Implemented RESTful endpoints
Implemented error handlers
I've used YAPF to enforce python code style

# Running the app
1. Install dependencies with pip install -r backend/requirements.txt
2. Set the FLASK_APP variable running export FLASK_APP=api.py
3. Run the app with flask run --reload

# Frontend
Added the Auth0 variables on environment.ts file
Guarantee that the frontend can be launched upon an ionic serve command and the login/token retrieval are functional

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)
