from typing import Union
from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None

#Here we have created a class called Post using the Pydantic Base Model. This defines what information can be provided by the user. Each pydantic model has a method called
# .model_dump(). If you ever need to convert your Pydantic model to a dictionary, you can use .model_dump().  

app = FastAPI()

def find_post(id):
  for p in my_posts:
    if p["id"] == id:
      return p

def find_index_post(id: int):
  for i, p in enumerate(my_posts):
    if p['id'] == id:
      return i

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

@app.get("/")
def read_root():
  return {"Message": "Welcome to my API! This is a WIP."}

# This is a path operation in the Fast API documentation. In other languages/frameworks, these three lines are often referred to as a route.
#
# JSON is the main universal language of APIs. FastAPI converts the above into JSON. 
# 
# The @ sign indicates that what follows is a decorator. In this case, the decorator
# identifies the code as a path operation, then there is the get method, and finally, the path.  

@app.get("/posts")
def get_posts():
  return{"data": my_posts}

#This creates a new path operation, at /posts. Note - if you call two routes by the same name, the program will stop at the first one it finds. The order matters!
# The get method is the method most commonly used when trying to retrieve data. 

# @app.post("/createposts")
# createposts is not appropriate for the naming conventions for APIs so it has to be changed.

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
  
  post_dict = post.model_dump()
  post_dict["id"] = randrange(0, 100000000)
  my_posts.append(post.model_dump())
  return {"data": post_dict}
          
#This model_dump() function allows you to see what is being returned as a dictionary. Very useful!

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
  post = find_post(id)
  
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with ID: {id} was not found.")
  #   response.status_code = status.HTTP_404_NOT_FOUND
  #   return "Error: specific post not found."
  return{"post_detail": post}
    
@app.get("/newest")
def get_newest_post():
  newest_post = my_posts[len(my_posts)-1]
  return {"detail": newest_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  index = find_index_post(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist.")
  my_posts.pop(index)
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
  index = find_index_post(id)
  
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist.")
  
  post_dict = post.model_dump()
  post_dict["id"] = id
  my_posts[index] = post_dict
  print(post)
  return {"Message": "Updated Post"}