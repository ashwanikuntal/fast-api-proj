# backend-tht

## Task
```
Your task is to implement a system which POST's and GET's data to and from the database using REST API's
You are free to use a python framework of you choice (Flask, Django, FastAPI, etc) for the REST
API development. Find below the API endpoints that you would need to create.
Attached is the dump of the data containing time, voltage, current, which you can load into the PostgreSQL database.
Even though this is a small concept program, returned homework should include tests and proper packaging. 
If your tests require PostgreSQL services, for simplicity your tests can assume those are already running,
instead of integrating service creation and deleting. The above application should be dockerized, 
one for the webserver application and the other for the database.

IMPORTANT: PLEASE CREATE A BRANCH AND RAISE A PR AGAINST THE MASTER BRANCH
```

## APIs to develop

```
GET /metrics?start=<TS>&end=<TS>
   Retrieving metrics from the DB with optional time range
```

```
POST /metrics
   Pushing metrics to the DB (once or multiple) 
```

### TS - Time Series

## If you are unable to complete the task, please submit the partial solution which you have done
and write in some additional points as to how you would proceed with the rest of the task.
We will discuss the details in the next round

## Ashwani's Comment:
I didn't have all the resources to complete this task in such short span of time.
The communicating consulting party gave only 3-4 hours to complete this tasks that too on a working day.
I could have written this task in more better way. This code is untested and written based on assumptions made as per problem requirement. We can discuss more in detail. Thanks.
