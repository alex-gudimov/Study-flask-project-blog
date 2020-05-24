from app import db
from models import Post
from models import Tag

#tag = Tag(name='python')

#db.session.add(tag)
#db.session.commit()

t = Tag.query.first()
post1 = Post.query.filter(Post.id==1)
post1 = post1.first()
post1.tags.append(t)
db.session.add(post1)
db.session.commit()