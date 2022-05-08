from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
    def get_users():
        users = db.session.query(User)
        list_users = []
        for user in users:
            list_users.append(user.serialize())
        return list_users

class Planet(db.Model):
    
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
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

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
        }

    def get_planets():
        planets = Planet.query.all()
        list_planets = []
        for planet in planets:
            list_planets.append(planet.serialize())
        return list_planets


class People(db.Model):
    __tablename__= 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
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

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "homeworld": self.homeworld,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "mass": self.mass,
            "height": self.height,

        }
    
    def get_people():
        people = People.query.all()
        list_people = []
        for character in people:
            list_people.append(character.serialize())
        return list_people
    

class Vehicle(db.Model):
    __tablename__= 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
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

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacities": self.cargo_capacities,
            "consumables": self.consumables,
            "pilots": self.pilots

        }

    def get_vehicles():
        vehicle = Vehicles.query.all()
        list_vehicles = []
        for vehicle in vehicles:
            list_vehicles.append(vehicle.serialize())
        return list_vehicles


class Favorites(db.Model):
    __tablename__= 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'))
    people_id= db.Column(db.Integer, db.ForeignKey('people.id'))
    vehicle_id= db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user = db.relationship(User)
    planet = db.relationship(Planet)
    people = db.relationship(People)
    vehicle = db.relationship(Vehicle)
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            "vehicle_id": self.vehicle_id,
        }

    def get_favorites(user_id):
        favorites = db.session.query(Favorites).filter(Favorites.user_id == user_id)
        list_favorites = []
        for favorite in favorites:
            list_favorites.append(favorite.serialize())
        return list_favorites