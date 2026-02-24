from enum import StrEnum
from typing import NamedTuple

class SeedType(StrEnum):
    PARSNIP_SEEDS = "Parsnip Seeds"
    BEAN_STARTER = "Bean Starter"
    CAULIFLOWER_SEEDS = "Cauliflower Seeds"
    POTATO_SEEDS = "Potato Seeds"
    TULIP_BULB = "Tulip Bulb"
    KALE_SEEDS = "Kale Seeds"
    JAZZ_SEEDS = "Jazz Seeds"

class Season(StrEnum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"
    WINTER = "Winter"

class SeedInfo(NamedTuple):
    seed_type: SeedType
    cost: int
    growth_time: int
    seasons: list[Season]
    xp: int
    sell_price: int 
    continued_growth_time: int | None = None

    @property
    def silver_price(self) -> float:
        return float(self.sell_price) * 1.25

    @property
    def gold_price(self) -> float:
        return float(self.sell_price) * 1.5

    @property
    def iridium_price(self) -> float:
        return float(self.sell_price) * 2.0

    def compound_investment_multiple(self) -> float:
        if self.continued_growth_time is None:
            return self.silver_price / self.cost
        else:
            total_growth_time = self.growth_time + self.continued_growth_time
            return (self.silver_price * 2) / (self.cost * 2)
