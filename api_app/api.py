from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
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

my_posts = [{
  "title": "False Start", 
  "content": "So, the date is 18/8/23. This is my second attempt to learn how to build an API. I was doing fine the first time, but my brother/tutor encouraged me to start again, go slower, and seek deeper understanding of the code and mechanisms used. Reasonable, I thought, so that's what I'm doing. I've nearly returned to the point I had previously reached, but my notes are a bit fuller and my understanding a bit better. Good call, Dan.", 
  "id": 1}, 
  {"title": "Deliberacy",
    "content": "Have you ever experienced that strange sensation of having so much to choose from that choice becomes quickly impossible? Have you ever observed, when you're rushed off your feet with responsibilities, that you constantly note things you want to do, or want to make time for, and use your time more efficiently overall. Yet, when you have an abundance of time, you don't tend to use it efficiently at all. Perhaps you, too, frequently lament that you haven't used your free time wisely whilst you're in one of these sedentary slumps. What you're experiencing is the product of total freedom, the total lack of need to do anything pressing, by which I mean to survive, such as resource accumulation to avoid starvation/thirst or to gain shelter. Indeed, humans have evolved to be excellent at acting to satisfy their needs, but what do you do when your survival needs are accounted for? Do you act on your dreams/desires/aims/goals anywhere near as determinedly as you act to sate your primal, survival needs? Be honest! Now, it is essential to acknowledge that humans have requirements that are less pressing than survival needs but rank higher than a mere desire. You could count the need to exercise, socialise, and perhaps a few others in these requirements. These are things that people tend to have to employ much more discipline to do than the actions that enable the fulfilment of their survival needs. This is why there are far more people dying of heart disease and suicide in the West than are dying of starvation and thirst and hypothermia. Quite frankly, humans used to be fit and socialized as a brute fact of survival - you couldn't be a nomadic hunter/gatherer in a tribe without company and exercise. Consequently, we are not evolved for a sedentary lifestyle, and our bodies are not going to maintain a healthy state if we don't help it to do so. So, although in the long-run these higher needs (higher in the sense that they are less basic/carnal, but still needs) are vital to satisfy they tend to get left to last. People MUST eat/drink/sleep. To be clear, these higher needs are not as important as the basic ones! You won't die immediately if you don't satisfy them swiftly. However, you can suffer greatly by neglecting them. What modern society has done is attempted to find ways to mask the symptoms that are generated when these needs are ignored. Feeling lonely? Use social media. It's extremely convenient. You don't need to move, you can feel 'involved' in a great social network. However, we know from the scientific studies and anecdotal evidence that social media is more likely to heighten loneliness. This is because you are substituting something we haven't evolved to need (long-distance observation of other people's lives with stilted, virtual interaction) for something we have evolved to need: the real deal (physical, personal social interaction). You can drink salt-water but it won't quench your thirst even if you fill your belly. Why then, you might wonder, do we choose this option? Quite simply because it is convenient. It is *easier* to lie in bed and scroll on your phone than having to find an event or community, groom yourself, attend in-person and then gamble your time and energy on a group of strangers. Sadly, one plan actually has a chance of success whilst the other one doesn't. So, where does that leave us? Alone, mostly. The studies done on friendship are pretty bleak reading, with many people counting less than 2 close friends in total. How can we deal with this issue? Personally, is the answer. We must personally become responsible for how we invest our energy and our time, our lives in other words. We must reject these cognitive honey traps, the hollow utopian lie that total freedom will total to happiness. It is untrue. Some freedom is essential to happiness. I would probably define that freedom specifically as the freedom to choose what you do. This is the reality of why slavery should be so abhorrent to us - because the only freedom that exists is the freedom to choose what we do with our time and energy. This is also why equal opportunities is important: being free to choose how to spend your time and energy means less if giving it yields less than it does for others - like being paid less than your colleague for the same work. So if we accept that sacrificing our time and energy to an opportunity or goal is the way to achieve long-term success, then we must volunteer our personal freedom. The paradox of freedom then is that the more personal freedom you allow yourself, the less free you will in fact become because you not have the opportunities that come with success. The first lesson concludes therefore with this: The practice of Deliberacy is named because it aims to de-liberate the mind of the practitioner: to encourage in them a servitude to the self by sacrificing personal freedom. To understand the WHY of the practice is ultimately the first lesson, so that you can enthusiastically pursue the WHAT.",
    "id": 2}]

@app.get("/")
def read_root():
  return {"Message": "Welcome to my API! This is a WIP."}

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
  my_posts.append(post_dict)
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