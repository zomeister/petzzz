from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Owner, Pet, Adoption, Action, Pet_Stats, Owner_Stats # , Menu_Item, Menu
from faker import Faker
from random import choice as rc

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def delete_records():
    session.query(Owner).delete()
    session.query(Pet).delete()
    session.query(Adoption).delete()
    session.query(Action).delete()
    session.query(Owner_Stats).delete()
    session.query(Pet_Stats).delete()
    session.commit()

def create_records():
    species =['dog', 'cat', 'snake', 'horse']
    
    owners = [Owner(first_name=fake.first_name(), last_name=fake.last_name(), password=fake.ean(), owner_stats=Owner_Stats()) for i in range(20)]
    pets = [Pet(name=fake.first_name(), species=rc(species), pet_stats=Pet_Stats()) for i in range(50)]
        
    adoptions = [Adoption() for i in range(36)]
    actions = [Action() for i in range(80)]
    session.add_all(owners + pets + adoptions + actions)
    session.commit()
    return owners, pets, adoptions, actions

def relate_records(owners, pets, adoptions, actions):
    for adoption in adoptions:
        adoption.owner = rc(owners)
        adoption.pet = rc(pets)
    for action in actions:
        action.adoption = rc(adoptions)
    session.add_all(adoptions + actions)
    session.commit()
    return owners, pets, adoptions, actions

if __name__ == '__main__':
    delete_records()
    owners, pets, adoptions, actions = create_records()
    owners, pets, adoptions, actions = relate_records(owners, pets, adoptions, actions)
    print('Database successfully seeded!')