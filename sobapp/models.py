'''

'''
import enum

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from sobapp import town_charts

db = SQLAlchemy()


class JobStatus(enum.Enum):
    available = 'Available'
    completed = 'Completed'
    failed = 'Failed'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


def base_to_dict(self):
    ''' returns a dict of 'explicit' fields from a model instance '''
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


#class Job(db.Model):
#    '''
#    HexCrawl Job model
#
#    '''
#    __tablename__ = "job"
#
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(255), unique=True, nullable=False)
#    keywords = db.Column(db.String(512), unique=False, nullable=True)
#    background = db.Column(db.String(512), unique=False, nullable=True)
#    location = db.Column(db.String(512), unique=False, nullable=True)
#    time = db.Column(db.Integer, default=0)
#    description = db.Column(db.String(2048), unique=False, nullable=True)
#    reward = db.Column(db.String(1024), unique=False, nullable=True)
#    failure = db.Column(db.String(1024), unique=False, nullable=True)
#
#    def is_mandatory(self):
#        ''' Return boolean if job is mandatory '''
#        keywords = self.keywords.split(',')
#        return 'Mandatory!' in keywords
#
#    def __repr__(self):
#        # Perform any model-specific manipulations before returning
#        dct = base_to_dict(self)
#        out = "\n".join(["\t{0:20}: {1}".format(*item) for item in dct.items()])
#        return "\n\t-----\n" + out


class Trait(db.Model):
    '''
    HexCrawl Town Trait model

    '''
    __tablename__ = "trait"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(2048), unique=False, nullable=True)

    def __repr__(self):
        # Perform any model-specific manipulations before returning
        dct = base_to_dict(self)
        out = "\n".join(["\t{0:20}: {1}".format(*item) for item in dct.items()])
        return "\n\t-----\n" + out


class Campaign(db.Model):
    '''
    HexCrawl Campaign Tracker model

    '''
    __tablename__ = "campaigns"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    players = db.Column(db.String(512), unique=False, nullable=True)

    def __repr__(self):
        # Perform any model-specific manipulations before returning
        dct = base_to_dict(self)
        out = "\n".join(["\t{0:20}: {1}".format(*item) for item in dct.items()])
        return "\n\t-----\n" + out


class World(db.Model):
    '''
    HexCrawl campaign worlds

    '''
    __tablename__ = "worlds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(255), unique=True, nullable=False, default="Wild West"
    )
    campaign_id = db.Column(
        db.Integer,
        db.ForeignKey('campaigns.id'),
        nullable=False,
        index=True,
    )
    campaign = db.relationship(
        'Campaign',
        backref=db.backref(
            'worlds',
            cascade='all,delete-orphan',
            lazy='select',
            order_by='World.name'
        )
    )

    @hybrid_property
    def name(self):
        return town_charts.TOWN_NAMES.get(self.roll, 'Unknown town name')


class Town(db.Model):
    '''
    HexCrawl campaign towns

    '''
    __tablename__ = "towns"

    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer)
    world_id = db.Column(
        db.Integer,
        db.ForeignKey('worlds.id'),
        nullable=False,
        index=True,
    )
    campaign = db.relationship(
        'World',
        backref=db.backref(
            'worlds',
            cascade='all,delete-orphan',
            lazy='select',
            order_by='Town.roll'
        )
    )

    @hybrid_property
    def name(self):
        return town_charts.TOWN_NAMES.get(self.roll, 'Unknown town name')


class TownLocation(db.Model):
    '''
    HexCrawl campaign town locations

    '''
    __tablename__ = "town_locations"

    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer)
    town_id = db.Column(
        db.Integer,
        db.ForeignKey('towns.id'),
        nullable=False,
        index=True,
    )
    town = db.relationship(
        'Town',
        backref=db.backref(
            'locations',
            cascade='all,delete-orphan',
            lazy='select',
            order_by='TownLocation.roll'
        )
    )

    @hybrid_property
    def name(self):
        return town_charts.TOWN_LOCATIONS.get(self.roll, 'Unknown location')


class Job(db.Model):
    '''
    HexCrawl campaign town jobs

    '''
    __tablename__ = "town_jobs"

    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer)
    # status = db.Column('status', db.Enum(JobStatus))
    town_id = db.Column(
        db.Integer,
        db.ForeignKey('towns.id'),
        nullable=False,
        index=True,
    )
    origin = db.relationship(
        'Town',
        backref=db.backref(
            'jobs',
            cascade='all,delete-orphan',
            lazy='select',
            order_by='Job.id'
        )
    )
