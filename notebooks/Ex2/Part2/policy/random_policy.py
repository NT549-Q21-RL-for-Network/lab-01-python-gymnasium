"""
Suggested owner: Person B

Merge contract:
- Keep the function name `robot_policy`
- Keep the parameter names `option` and `env`
"""

def robot_policy(option="random", env=None):
     """
     A simple policy function that selects an action based on the specified option.
     Currently supports only a random policy.
     """
     if option == "random":
          return env.action_space.sample()  # Randomly select an action from the action space
    

if __name__ == "__main__":
    print("random_policy scaffold ready.")
    print("This file should only hold action-selection logic.")
