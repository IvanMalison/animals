from flask.ext.sqlalchemy import SQLAlchemy

from .app import app


db = SQLAlchemy(app)


class Species(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20), unique=True)


class Animal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20))
    species_id = db.Column(db.Integer, db.ForeignKey(Species.id))
    species = db.relationship(
        'Species',
        primaryjoin='Animal.species_id==Species.id',
        backref='specimens',
    )
