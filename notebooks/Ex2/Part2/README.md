# Part 2 Work Split

This folder splits `## Part 2: Custom Environment "VacuumCleaner"` from `notebooks/Ex2/Ex2.ipynb`
into separate files so two people can work in parallel.

Suggested split:
- Person A: `env/vacuum_cleaner_env.py`
- Person B: `policy/random_policy.py`, `runner/run_random_episode.py`, `utils/persistence.py`

Merge contract:
- Keep the class name `VacuumCleanerEnv`
- Keep the function names `robot_policy` and `save`
- Keep the observation keys `position` and `dust`
- Keep the action mapping `0=up, 1=down, 2=left, 3=right`
- Do not move environment logic into `policy/` or `runner/`
- Do not rename files before merge

How to merge back into the notebook:
1. Copy `env/vacuum_cleaner_env.py` into the environment code cell.
2. Copy `policy/random_policy.py` into the policy cell.
3. Copy `runner/run_random_episode.py` into the episode runner cell.
4. Copy `utils/persistence.py` into the save helper cell.

Standalone run notes:
- Each file is syntactically runnable on its own.
- `runner/run_random_episode.py` is wired to import the other split files.
- Until the TODO sections are completed, the runner may stop with placeholder-related errors.
