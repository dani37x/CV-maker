from project_files import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(40), unique=True, nullable=False)
#     second_name = db.Column(db.String(40), unique=True, nullable=False)
#     e_mail = db.Column(db.String(40), unique=False, nullable=False)
#     birthday = db.Column(db.String(10), unique=False, nullable=False)
#     place_of_residence = db.Column(db.String(30), unique=False, nullable=False)
#     phone_number = db.Column(db.String(15), unique=False, nullable=False)
#     color = db.Column(db.String(15), unique=False, nullable=False)
#     color_2 = db.Column(db.String(15), unique=False, nullable=False)
#     info = db.Column(db.String(1024), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.first_name


class Informations( db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column( db.String(120), nullable=False)
  information_type = db.Column( db.String(120), nullable=False)
  
  
  def __repr__(self):
    return '<Informations %r>' % self.name

  