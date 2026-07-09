from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts