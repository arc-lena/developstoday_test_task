from developstoday.celery import app
from news.models import Post


@app.task
def upvotes_reset():
    posts = Post.objects.all()
    posts.update(amount_of_upvotes=0)
