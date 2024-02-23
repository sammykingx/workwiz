class PricingCalculator:
    """Blueprint for the pricing calculator"""

    _skill_proficiency = {
        "beginner": 0,
        "junior": 0.2,
        "intermediate": 0.3,
        "advanced": 0.7,
    }

    _project_experience = {
        "small": 0.2,
        "standard": 0.3,
        "enterpise_level": 0.5,
    }

    _project_level = {
        "easy": 0.2,
        "standard": 0.3,
        "hard": 0.5,
    }

    _extra_days = 21

    def __init__(
        self, skill_level: str, market_cost: float, timeline: int
    ):
        self.project_timeline = timeline + self._extra_days
        if timeline > 31:
            market_cost += market_cost * 0.3
            self.base_rate = (market_cost / self.project_timeline) + (
                timeline * 0.3
            )

        else:
            self.base_rate = market_cost / self.project_timeline

        self.gig_rate = self.base_rate + (
            self.base_rate * self._skill_proficiency[skill_level]
        )
        self.skill_level = skill_level
        self.project_cost = 0.0

    def increase_rate(self, experience: str, complexity: str) -> None:
        """increase gig rate based on project complexity and experience level"""

        self.experience_rate = (
            self.gig_rate * self._project_experience[experience]
        )
        self.complexity_rate = (
            self.gig_rate * self._project_level[complexity]
        )
        self.gig_rate = (
            self.gig_rate
            + self.complexity_rate
            + self.experience_rate
        )

    def calculate(self) -> int:
        """calculates the eatimated project cost"""

        self.project_cost = self.gig_rate * self.project_timeline

        if self.skill_level == "beginner":
            return 0

        return round(self.project_cost)

    """
    def __str__(self):
        return "{}, {}, {}".format(
                self.skill_level.capitalize(),
                self.gig_rate,
                self.project_cost,
                self.project_timeline,
            )
    """
