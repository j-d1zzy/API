''' 

API Course for Python  |
_______________________|  

What are Virtual Environments? 
______________________________

A virtual environment is a space on the machine is isolated from the rest of the system. 
It is useful because it can provide an ideal environment for a given project, without affecting other 
environments.

What are APIs?
______________________________

API stands for Application Programming Interface. The API is a set of rules and protocols that allow different software applications to
communicate and interact with each other. It defines how different software components should interact, what data they can exchange, and how 
they should exchange it. Essentially, they provide a standardized way for developers to enable communication between software, regardless
of whether they are written in different programming languages, on different platforms, or using different technologies. APIs also often
include security mechanisms. 

What is FastAPI?
______________________________

FastAPI is a Python web framework used to build APIs quickly and efficiently. This framework allows the developer to define and handle API
routes, manage requests and responses, handle exceptions, and manage the structure of API applications. 

What is a Path Operation?
______________________________

@app.get("/")

This is called a path operation in the Fast API documentation. In other languages/frameworks, these three lines are often referred to as a route.

The @ sign indicates that what follows is a decorator. In this case, the decorator identifies the code as a path operation, then there is the 
method, and finally, the path. The decorator, signalled by the @ symbol, is followed by the method: .get, which is then followed by the path: /, 
and then finally there is the function. This function will contain the logic for performing a task, the result of which will be returned to the 
user upon completion. 

JSON, which stands for JavaScript Object Notation, is the main universal language of APIs. Its lightweight format is well-suited to data
interchange. In my API project, FastAPI converts Python into JSON before sending it. This is why a JSON response gets returned to the client.

In the tutorial, when testing our HTTP requests, the tutor had us download and install a program called Postman. This is a way of testing 
requests that you wish to make of the server, without having to use the web browser. He assured us that we will come to appreciate this in time.

3. HTTP Requests
______________________________

When there is a Get Request, the device sends the request to the API server and then returns the request. With a POST request, the device sending the request can send data
to the API server, and will also return anything it ought to according to the logic of the program. 

4. Schema
______________________________

So far in our exercise, we've had a hard time getting values from the body. The client can send any old data. The data doesn't get validated. Ultimately, we want to force the
user to follow a predictable schema. One tool we can use to help put a schema in place is pydantic. Using Pydantic in the lesson, I was able to make a Class which used the 
BaseModel class imported from Pydantic to dictate a schema, which will limit what can be accepted in a post request from the user. 

5. CRUD
______________________________

CRUD stands for Create | Read | Update | Delete

These are the four main functions of an application. Social media applications, as we are working on in the video, are CRUD-based applications. There are certain best 
practices that must be followed. For example, the tutor said that we don't name our routes in the singular.

Create --> Post --> /posts --> @app.post("/posts")

       --> GET --> /posts/:id --> @app.get("/posts/{id}")
Read --|
       --> GET --> /posts --> @app.get("/posts")

Update --> PUT/PATCH --> /posts/:id --> @app.put("/posts/{id}")

Delete --> DELETE --> /posts/:id --> @app.delete("/posts/{id}")

IMPORTANT: It is standard convention to pluralize nouns in the names of routes (/users instead of /user, /posts instead of /post).

With the PUT method, all of the fields must be passed to the API, even if only one field is actually being altered. However, with the PATCH 
method, you can update a single field. 

. Documentation
______________________________

One of the benefits of using FastAPI is that it makes documentation of your API very easy, using SwaggerUI. All the developer has to do is enter 
the URL/docs and they are presented with an easy-on-the-eye display of their API's documentation. Another documentation tool is /redoc. These 
tools might mean that we don't always have to use Postman.

7. Databases
______________________________

A database is a collection of organized data that can be easily accessed and managed. Developers don't work or interact with databases directly. 
Instead, we make use of a software referred to as a Database Management System (DBMS). 

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