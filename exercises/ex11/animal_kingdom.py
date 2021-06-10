"""A program that explores the animal kingdom."""
from __future__ import annotations
__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Uncomment the following lines to test your classes
    # lion = Animal("lion", 10, "\U0001F981")
    # pig = Animal("pig", 3, "\U0001F437")

    # ram = Animal("ram", 6, "\U0001F40F")
    # elephant = Animal("elephant", 9, "\U0001F418")
    # gorilla = Animal("gorilla", 7, "\U0001F98D")
    # camel = Animal("camel", 4, "\U0001F42A")

    # team1 = Team("Hello Kitty", [lion, ram, pig])
    # team2 = Team("BIG", [elephant, gorilla, camel])

    # winners = team1.battle(team2)

    # print(f"{team1.team_name} vs {team2.team_name}")

    # for i in range(len(team1.animals)):
    #     print(f"{team1.animals[i].emoji}  vs {team2.animals[i].emoji}")
    #     print(f"The {winners[i].species} wins!")

    # print(team1.who_won(team2))


# TODO 1: Define the Animal class, and its logic, here.
class Animal:
    """Defined Animal class."""
    species: str
    danger_level: int
    emoji: str

    def __init__(self, species: str, danger_level: int, emoji: str):
        """Constructor for the Animal class."""
        self.species = species
        self.danger_level = danger_level
        self.emoji = emoji
    
    def fight(self, opponent: Animal) -> Animal:
        """Simulates a fight between two animals and returns the one with the higher danger_level."""
        if self.danger_level == opponent.danger_level:
            return opponent
        elif self.danger_level < opponent.danger_level:
            return opponent
        else:
            return self


# TODO 2: Define the Team class, and its logic, here.
class Team:
    """Defined Team class."""
    team_name: str
    animals: list[Animal]
    score: int

    def __init__(self, team_name: str, animals: list[Animal]):
        """Constructor for the Team class."""
        self.team_name = team_name
        self.animals = animals
        self.score = 0

    def battle(self, opponent: Team) -> list[Animal]:
        """Returns a list with the winners of the individual battles and updates the score of the winners' team."""
        result: list[Animal] = []
        if len(self.animals) != len(opponent.animals):
            return result
        else:
            for i in range(len(self.animals)):
                winner: Animal = self.animals[i].fight(opponent.animals[i])
                if winner in self.animals:
                    self.score += 1
                else:
                    opponent.score += 1
                result.append(winner)
        return result

    def who_won(self, opponent: Team) -> str:
        """Returns a different string depending on which team won."""
        null: str = "The battle hasn't happened yet"
        tie: str = "It was a tie!"
        if self.score == 0 and opponent.score == 0:
            return null
        elif self.score == opponent.score:
            return tie
        elif self.score > opponent.score:
            return f"Team {self.team_name} won!"
        else:
            return f"Team {opponent.team_name} won!"


if __name__ == "__main__":
    main()