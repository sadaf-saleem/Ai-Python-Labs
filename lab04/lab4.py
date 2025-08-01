import time
import random

class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

class Agent:
    def __init__(self):
        self.environment = None

    def sense(self, environment):
        self.environment = environment

    def act(self):
        if self.environment.rooms[self.environment.current_index].status == 'dirty':
            return 'clean'
        elif self.environment.current_index < len(self.environment.rooms) - 1:
            return 'right'
        else:
            return 'left'

class ModelReflexAgent:
    def __init__(self, room_count):
        self.model = ['dirty'] * room_count
        self.current_index = 0
        self.direction = 1

    def sense(self, environment):
        self.environment = environment
        self.model[self.environment.current_index] = environment.rooms[environment.current_index].status
        self.current_index = environment.current_index

    def act(self):
        if self.model[self.current_index] == 'dirty':
            return 'clean'
        if self.direction == 1 and self.current_index == len(self.model) - 1:
            self.direction = -1
        elif self.direction == -1 and self.current_index == 0:
            self.direction = 1
        return 'right' if self.direction == 1 else 'left'

class VacuumEnvironment:
    def __init__(self, agent, room_count=2, use_model=False, no_sensor=False):
        self.rooms = [Room(chr(65 + i), random.choice(["dirty", "clean"])) for i in range(room_count)]
        self.agent = agent
        self.current_index = 0
        self.step = 1
        self.score = 0
        self.use_model = use_model
        self.no_sensor = no_sensor

    def all_clean(self):
        return all(room.status == 'clean' for room in self.rooms)

    def execute(self, max_steps=50):
        while self.step <= max_steps:
            print(f"\nStep {self.step}")
            if not self.no_sensor:
                self.agent.sense(self)
            action = self.agent.act()
            print(f"Agent in Room [{self.rooms[self.current_index].location}] - Status: {self.rooms[self.current_index].status}")
            print(f"Action: {action}")

            if action == 'clean' and self.rooms[self.current_index].status == 'dirty':
                self.rooms[self.current_index].status = 'clean'
                self.score += 25
            elif action == 'right' and self.current_index < len(self.rooms) - 1:
                self.current_index += 1
                self.score -= 1
            elif action == 'left' and self.current_index > 0:
                self.current_index -= 1
                self.score -= 1

            # -10 for each dirty room after each second
            dirty_penalty = sum(1 for room in self.rooms if room.status == 'dirty') * 10
            self.score -= dirty_penalty

            print(f"Rooms Status: {[room.status for room in self.rooms]}")
            print(f"Score: {self.score}")

            self.step += 1
            time.sleep(1)

            if self.all_clean():
                print("\n✅ All rooms clean. Agent stopped.")
                break


# ---------- MAIN CONTROL ----------
if __name__ == "__main__":
    print("Select mode:")
    print("1. Two-room agent")
    print("2. Three-room agent")
    print("3. N-room agent (user-defined)")
    print("4. Reflex agent with model")
    print("5. Reflex agent with model and NO sensors")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        agent = Agent()
        env = VacuumEnvironment(agent, room_count=2)
        env.execute()
    elif choice == 2:
        agent = Agent()
        env = VacuumEnvironment(agent, room_count=3)
        env.execute()
    elif choice == 3:
        n = int(input("Enter number of rooms (>=2): "))
        agent = Agent()
        env = VacuumEnvironment(agent, room_count=n)
        env.execute()
    elif choice == 4:
        n = int(input("Enter number of rooms (>=2): "))
        agent = ModelReflexAgent(room_count=n)
        env = VacuumEnvironment(agent, room_count=n, use_model=True)
        env.execute()
    elif choice == 5:
        n = int(input("Enter number of rooms (>=2): "))
        agent = ModelReflexAgent(room_count=n)
        env = VacuumEnvironment(agent, room_count=n, use_model=True, no_sensor=True)
        env.execute()
    else:
        print("Invalid choice.") 
