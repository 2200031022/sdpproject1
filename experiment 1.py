import random

class VacuumAgent:
    def __init__(self, locations):
        self.locations = locations
        self.current_location = random.choice(locations)

    def perceive(self):
        return self.current_location, random.choice([True, False])  # Location, Dirty or Clean

    def act(self, location, is_dirty):
        if is_dirty:
            print(f"Agent is cleaning {location}.")
            self.clean(location)
        else:
            print(f"Agent is moving to {location}.")
            self.move(location)

    def clean(self, location):
        print(f"{location} is now clean.")
        # Assume cleaning takes some time
        print("Agent is waiting for a moment.")

    def move(self, new_location):
        self.current_location = new_location

def main():
    locations = ['A', 'B', 'C']
    agent = VacuumAgent(locations)

    for _ in range(5):  # Perform actions for a certain number of steps
        current_location, is_dirty = agent.perceive()
        agent.act(current_location, is_dirty)

if __name__ == "__main__":
    main()
