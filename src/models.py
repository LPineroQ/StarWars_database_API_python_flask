from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Models):
    
        __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    url = db.Column(db.String(200))
    surface_water = db.Column(db.Integer)
    terrain = db.Column(db.String(120))
    climate = db.Column(db.String(120))
    population = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)

class People(Base):
    __tablename__= 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(300))
    url = db.Column(db.String(120))
    homeworld = db.Column(db.String(120))
    gender = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    eye_color = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    hair_color = db.Column(db.String(120))
    mass = db.Column(db.Integer)
    height = db.Column(db.Integer)

class Vehicles(Base):
    __tablename__= 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(300))
    url = db.Column(db.String(120))
    model = db.Column(db.String(120))
    starship_class = db.Column(db.String(120))
    manufacturer = db.Column(db.String(120))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.Integer)
    MGLT = db.Column(db.Integer)
    cargo_capacities = db.Column(db.Integer)
    consumables = db.Column(db.Integer)
    pilots = db.Column(db.String(120))

class favorites(Base):
    __tablename__= 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
    Planet_id= db.Column(db.Integer, ForeignKey('planets.id'), nullable=True)
    People_id= db.Columndb.(Integer, ForeignKey('people.id'), nullable=True)
    Vehicles_id= db.Column(db.Integer, ForeignKey('vehicles.id'), nullable=True)