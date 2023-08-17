''' 

 API Course for Python  |
 _______________________|  

1. What are Virtual Environments? 
_________________________________

A virtual environment is a space on the machine is isolated from the rest of the system. 
It is useful because it can provide an ideal environment for a given project, without affecting other 
environments.ls


2. What is a Path Operation?
_________________________________

@app.get("/")
def read_root():
  return {"message": "Hello World"}

The decorator, signalled by the @ symbol, is followed by the method: .get, which is then followed by the path: /, and then finally you have the function.
It will contain the logic for performing a task, the result of which will be returned to the user upon completion. 

In the tutorial, when testing our HTTP requests, the tutor had us download and install a program called Postman. This is a way of testing requests that you wish to make of the
server, without having to use the web browser. He assured us that we will come to appreciate this in time.

3. HTTP Requests
________________________________

When there is a Get Request, the device sends the request to the API server and then returns the request. With a POST request, the device sending the request can send data
to the API server, and will also return anything it ought to according to the logic of the program. 

4. Schema
________________________________

So far in our exercise, we've had a hard time getting values from the body. The client can send any old data. The data doesn't get validated. Ultimately, we want to force the
user to follow a predictable schema. One tool we can use to help put a schema in place is pydantic. Using Pydantic in the lesson, I was able to make a Class which used the 
BaseModel class imported from Pydantic to dictate a schema, which will limit what can be accepted in a post request from the user. 

5. CRUD
________________________________

CRUD stands for Create | Read | Update | Delete

These are the four main functions of an application. Social media applications, as we are working on in the video, are CRUD-based applications. There are certain best 
practices that must be followed. For example, the tutor said that we don't name our routes in the singular.

Create --> Post --> /posts --> @app.post("/posts")

       --> GET --> /posts/:id --> @app.get("/posts/{id}")
Read --|
       --> GET --> /posts --> @app.get("/posts")

Update --> PUT/PATCH --> /posts/:id --> @app.put("/posts/{id}")

Delete --> DELETE --> /posts/:id --> @app.delete("/posts/{id}")

6. Documentation
_______________________________

One of the benefits of using FastAPI is that it makes documentation of your API very easy, using SwaggerUI. All the developer has to do is enter the URL/docs and they
are presented with an easy-on-the-eye display of their API's documentation. Another documentation tool is /redoc. These tools might mean that we don't always have to use 
Postman.

7. Databases
_______________________________

A database is a collection of organized data that can be easily accessed and managed. Developers don't work or interact with databases directly. Instead, we make use of a
software referred to as a Database Management System (DBMS). 

There are two kinds of database:

1). Relational
      - MYSQL
      - POSTGRESQL
      - ORACLE
      - SQL SERVER
2). NoSQL
      - MongoDB
      - DynamoDB
      - ORACLE
      - SQL SERVER

SQL (Structured Query Language) is the language that we use to communicate with the DBMS.

Postgres

  - Each instance of postgres can be carved into multiple mutually exclusive databases. 

'''