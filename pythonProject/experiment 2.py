import random

class RandomMovementReflexAgent:
    def __init__(self, locations):
        self.locations = locations
        self.current_location = random.choice(locations)

    def perceive(self):
        return self.current_location, random.choice([True, False])  # Location, Dirty or Clean

    def act(self, location, is_dirty):
        print(f"Agent is moving to a random direction.")
        self.move_random()

    def move_random(self):
        new_location = random.choice(self.locations)
        self.current_location = new_location
        print(f"Agent moved to {new_location}.")

def main():
    locations = ['A', 'B', 'C']
    agent = RandomMovementReflexAgent(locations)

    for _ in range(5):  # Perform actions for a certain number of steps
        current_location, is_dirty = agent.perceive()
        agent.act(current_location, is_dirty)

if __name__ == "__main__":
    main()
