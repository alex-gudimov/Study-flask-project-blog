from app import db
from models import Post

posts = Post.query.all()

p2 = Post.query.filter(Post.title.contains('second')).all()


print(p2)
