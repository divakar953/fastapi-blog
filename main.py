from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# this app object is what we will be using to define all of our routes
app = FastAPI()
# FastAPI uses decorators for routes.

# list of dictionaries, where each dictionary is a post
posts: list[dict] = [
    {
        "id": 1,
        "author": "John Doe 1",
        "title": "Post 1",
        "content": "This is the first post of the bolg",
        "date_posted": "April 15, 2025"
    },
    {
        "id": 2,
        "author": "John Doe 2",
        "title": "Post 2",
        "content": "This is the second post of the bolg",
        "date_posted": "July 12, 2025"
    }
]
# this 'posts' will be replaced by a proper database later

# home route that responds to get request at the root URL
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) # we can stack decorators as such. and they will execute the same fuction home()
def home():
    return f"<h1>{posts[0]['title']}</h1>"
    #return {"message": "Hello World"} # fastapi will automatically convert this dictonary with just a single value to JSON
# we are decorating a function called home with app.get() decorator and the path is '/' for the root

@app.get("/api/posts")
def get_posts():
    return posts
#fastapi will automatically convert this list of dictionaries to a JSON array