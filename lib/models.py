from sqlalchemy import create_engine, func, MetaData, Column, ForeignKey, Integer, String, DateTime  # , desc, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship # , sessionmaker , backref
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

engine = create_engine('sqlite:///library.db')
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

##############################################################################################################################################
##############################################################################################################################################

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    
    first_name = Column(String(30))
    last_name = Column(String(40))
    password = Column(String(20))
    adoptions = relationship('Adoption', back_populates='owner', cascade='all, delete-orphan')
    pets = association_proxy('adoptions', 'pet', creator=lambda pe: Adoption(pet=pe))
    owner_stats = relationship('Owner_Stats', back_populates='owner', uselist=False)
    def __repr__(self):
        return "<Owner: id={}, name={} {}, password={}>".format(self.id, self.first_name, self.last_name, self.password)

class Owner_Stats(Base):
    __tablename__ = 'owners_stats'
    id = Column(Integer, primary_key=True)
    money = Column(Integer, default='1000')
    owner_id = Column(Integer, ForeignKey('owners.id'))
    owner = relationship('Owner', back_populates='owner_stats', uselist=False)
    def __repr__(self):
        return "<Owner_Stats: id={}, money={}>".format(self.id, self.money)

##############################################################################################################################################

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    
    name = Column(String(25))
    species = Column(String(30))
    adoptions = relationship('Adoption', back_populates='pet', cascade='all, delete-orphan')
    owners = association_proxy('adoptions', 'owner', creator=lambda ow: Adoption(owner=ow))
    pet_stats = relationship('Pet_Stats', back_populates='pet', uselist=False)
    def __repr__(self):
        return "<Pet: id={}, name={}, species={}>".format(self.id, self.name, self.species)

class Pet_Stats(Base):
    __tablename__ = 'pets_stats'
    id = Column(Integer, primary_key=True)
    happiness = Column(Integer, default=100)
    love = Column(Integer, default=100)
    hunger = Column(Integer, default=10)
    rowdiness = Column(Integer, default=10)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    pet = relationship('Pet', back_populates='pet_stats', uselist=False)
    def __repr__(self):
        return "<Pet_Stats: id={}, happiness={}, love={}, hunger={}, rowdiness={}>".format(self.id, self.happiness, self.love, self.hunger, self.rowdiness)

##############################################################################################################################################

class Adoption(Base):
    __tablename__ = 'adoptions'
    id = Column(Integer, primary_key=True) 
    
    date_and_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey('owners.id'))
    pet_id = Column(Integer, ForeignKey('pets.id'))
    owner = relationship('Owner', back_populates='adoptions')
    pet = relationship('Pet', back_populates='adoptions')
    actions = relationship('Action', back_populates='adoption', cascade='all, delete-orphan')
    def __repr__(self):
        return "<Adoption: id={}, date_and_time={}>".format(self.id, self.date_and_time)

##############################################################################################################################################

class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    
    date_and_time = Column(DateTime, server_default=func.now())
    service = Column(String(40))
    adoption_id = Column(Integer, ForeignKey('adoptions.id'))
    adoption = relationship('Adoption', back_populates='actions')
    # menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    def __repr__(self):
        return "<Action: id={}, date_and_time={}, service={}>".format(self.id, self.date_and_time, self.service)


##############################################################################################################################################
##############################################################################################################################################

# class Menu_Item(Base):
#     __tablename__ = 'menu_items'
#     id = Column(Integer, primary_key=True)
    
#     name = Column(String(40))
#     description = Column(String())
#     menu_id = Column(Integer, ForeignKey('menus.id'))
#     menu = relationship('Menu', back_populates='menu_items')
#     def __repr__(self):
#         return "<Menu_Item: id={}, name={}, description={}>".format(self.id, self.name, self.description)

##############################################################################################################################################

# class Menu(Base):
#     __tablename__ ='menus'
#     id = Column(Integer, primary_key=True)
    
#     name = Column(String(40))
#     description = Column(String())
#     menu_items = relationship('menu_item', back_populates='menu', cascade='all, delete-orphan')

##############################################################################################################################################

 
Base.metadata.create_all(bind=engine)