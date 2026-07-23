from __future__ import annotations

# This file intentionally does not hard-code a Sentaurus command.
# After the verified command is known:
# 1. read initial_doe.csv
# 2. create one isolated run directory per design_id
# 3. render parameters into the Golden Deck
# 4. execute the simulator
# 5. write status and exit code to experiment_registry.csv
# 6. never overwrite an existing run directory
#
# Keep all simulator-specific logic in one adapter function.
