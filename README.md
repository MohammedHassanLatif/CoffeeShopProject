# Coffee Shop Full Stack
# Auth0 account

AUTH0_DOMAIN = 'hassanlatif.uk.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'http://localhost:5000'

⚠️ I DID updated the POSTman collection with both barista and manager accounts, the thing is that the token does expire, so I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

# Manager account

User: coffee_manager@udacity.com
password: udacity123!

submitted token

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMxMGQzM2Q3ZjZmNTkxMzVkOGY4Y2YiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTA3OTgyMzgsImV4cCI6MTY5MDgwNTQzOCwiYXpwIjoiZVh1SjZmQjd6QzBxS292SE93STBMaThUVGR5S1dhWEoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.Su-cmHgqK5x6t9fffp14fSgiM80eR0W7bvsLzdsQE2SPby-Y146t-wMxxA1JlAYF5Ztfo6XhmyagEjvw62R2DvZPGPxwEsYmeWh2FuDV_16o-v3X4tLbAfKGXFtkQ5SpakcROjwpS4sHyrFrWFYRYA2kg-ILOwcCV7BjiTTl3C1xx1iLR66X5BeYATh39p799iSAyaR8ay6ct6j9E65X7JKzA_Bc6VL6cn9KKDnqjV9mAvRSe4BNlp47MYns6GS_S2HnYmvVYDvH0fQiFknPSnDliOInzL4kV1dih8G-a6S871GxlVfX71EPN62rhcd8VYZIfDgl8V5SKFJsj8H9sQ

# Barista account

User: barista@udacity.com
password: udacity123!

submitted token

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNPMTlNbnJwT09YZWhwM0hBb0RfZCJ9.eyJpc3MiOiJodHRwczovL2hhc3NhbmxhdGlmLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGMxMGQ0ZmQ3ZjZmNTkxMzVkOGY4ZDEiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJpYXQiOjE2OTA3OTgxNTMsImV4cCI6MTY5MDgwNTM1MywiYXpwIjoiZVh1SjZmQjd6QzBxS292SE93STBMaThUVGR5S1dhWEoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.FKbK1hf2u22kfeV9w9cXfbPfifww2Sei3IJlXAHdovng6so6OSWg4uZ4fhMrl6pbWBkoWXVGm_1I574XP_PhJDJ2_JkXr5S8B6s5lUdOdjLef147Afc0tghBJgoiA65REN89GCrcx1GWZ1DZ9bi4hXn24xMqhIsM-tpmdkitVgRSjWRyMVyW28bB-NdHIhU3JN3VFlIsHCaqk06-uHyE2E4JJfQlcYlD_-LMoIYxY_eB_YItr6k686Xn4xBCgPuVY3C286MXmiUaX_0fMGuk1KiDBQthjNLSfdtl2Y1D5hJker8dMUhiVphfObjNyG7pGUm9lMEubWz_G7_-nz7AQg
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
