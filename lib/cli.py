from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Owner, Pet, Adoption, Action # Menu_Item # , Pet_Stats, Owner_Stats
from rich.console import Console
from rich.prompt import Prompt

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()
console = Console()

class CLI():
    def __init__(self):
        self.console = Console()
        self.choices = {
            "1": self.add_owner,
            "2": self.add_pet,
            "3": self.adoption,
            "4": self.care,
            "q": self.quit
        }
        self.care_choices = {
            "1": self.bathe_pet,
            "2": self.feed_pet,
            "3": self.walk_pet,
            "4": self.tuckin_pet,
            "q": self.quit
        }
        pass
    def run(self):
        pass
    pass

if __name__ == "__main__":
    cli = CLI()
    cli.run()
    