"""
Suggested owner: Person B

Merge contract:
- Keep this file focused on episode execution only
- Import `VacuumCleanerEnv` from `env/vacuum_cleaner_env.py`
- Import `robot_policy` from `policy/random_policy.py`
- Do not duplicate environment logic here
"""

import sys
from pathlib import Path


PART2_ROOT = Path(__file__).resolve().parents[1]
ENV_DIR = PART2_ROOT / "env"
POLICY_DIR = PART2_ROOT / "policy"
UTILS_DIR = PART2_ROOT / "utils"

for module_dir in (ENV_DIR, POLICY_DIR, UTILS_DIR):
    module_dir_str = str(module_dir)
    if module_dir_str not in sys.path:
        sys.path.insert(0, module_dir_str)

from random_policy import robot_policy
from vacuum_cleaner_env import VacuumCleanerEnv


def main():
    try:
        env = VacuumCleanerEnv(m=5, n=5, obstacle=(2, 2))
        obs, _ = env.reset()
        env.render()
        terminated = False
        truncated = False

        while not terminated and not truncated:
            action = robot_policy(option="random", env=env)
            obs, reward, terminated, truncated, info = env.step(action)
            env.render()
            print(f"Action: {action}, Reward: {reward}, Terminated: {terminated}")
            if terminated or truncated:
                print("Episode finished with total reward:", env.total_reward)
                break
    except Exception as exc:
        print("Runner scaffold is wired correctly, but some TODO sections are not finished yet.")
        print(f"Current error: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    main()
