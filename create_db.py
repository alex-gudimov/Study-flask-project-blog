from app import db
from models import Post
from models import Tag

#tag = Tag(name='python')

#db.session.add(tag)
#db.session.commit()

post = Post.query.all()
print(post)

print('-' * 40)

ps = Post.query.filter(Post.title.contains('post'))
print(ps)