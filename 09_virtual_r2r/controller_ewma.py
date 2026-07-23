from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EWMAController:
    target: float
    lam: float = 0.3
    gain: float = 0.5
    recipe_min: float = 3.0
    recipe_max: float = 11.0
    estimate: float | None = None

    def update(self, measurement: float, recipe: float) -> float:
        if self.estimate is None:
            self.estimate = measurement
        else:
            self.estimate = self.lam * measurement + (1.0 - self.lam) * self.estimate

        error = self.target - self.estimate
        next_recipe = recipe + self.gain * error
        return min(self.recipe_max, max(self.recipe_min, next_recipe))
