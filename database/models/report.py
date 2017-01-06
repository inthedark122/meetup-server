from database import db


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    bgImage = db.Column(db.String(255))
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Report %r>' % self.title
