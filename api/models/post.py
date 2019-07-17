from api.database import db, ma

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)