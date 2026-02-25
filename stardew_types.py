from enum import StrEnum, IntEnum
from typing import NamedTuple
from math import floor

class QualityLevel(IntEnum):
    NORMAL = 0
    SILVER = 1
    GOLD = 2
    IRIDIUM = 3
    
    @property
    def crop_sell_price_multiplier(self) -> float:
        if self == QualityLevel.NORMAL:
            return 1.0
        elif self == QualityLevel.SILVER:
            return 1.25
        elif self == QualityLevel.GOLD:
            return 1.5
        elif self == QualityLevel.IRIDIUM:
            return 2.0
        else:
            raise ValueError("Invalid quality level.")

class Season(StrEnum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"
    WINTER = "Winter"

class FertilizerLevel(IntEnum):
    NONE = 0
    BASIC = 1
    QUALITY = 2
    DELUXE = 3

    def compute_crop_quality_distribution(self, farming_level: int) -> dict[QualityLevel, float]:
        if farming_level < 0 or farming_level > 14:
            raise ValueError("Farming level must be between 0 and 14 inclusive.")

        gold_base = (0.2 * (farming_level / 10.0)) + (0.2 * self * (farming_level + 2.0) / 12.0) + 0.01

        if self == FertilizerLevel.DELUXE: 
            iridium_chance = gold_base / 2.0
            gold_chance = (1.0 - iridium_chance) * gold_base
            silver_chance = (1.0 - iridium_chance - gold_chance)
            normal_chance = 0.0

            if silver_chance < 0.0:
                silver_chance = 0.0
                gold_chance = (1.0 - iridium_chance)
        else:
            iridium_chance = 0.0
            gold_chance = gold_base
            silver_chance = (1.0 - gold_chance) * min(0.75, 2.0 * gold_base)
            normal_chance = 1.0 - gold_chance - silver_chance

        return {
            QualityLevel.NORMAL: normal_chance,
            QualityLevel.SILVER: silver_chance,
            QualityLevel.GOLD: gold_chance,
            QualityLevel.IRIDIUM: iridium_chance,
        }

    def compute_expected_sell_price_multiplier(self, farming_level: int) -> float:
        if farming_level < 0 or farming_level > 14:
            raise ValueError("Farming level must be between 0 and 14 inclusive.")
        distribution = self.compute_crop_quality_distribution(farming_level)
        print(f"Distribution: {distribution[QualityLevel.NORMAL]:.4f}, {distribution[QualityLevel.SILVER]:.4f}, {distribution[QualityLevel.GOLD]:.4f}, {distribution[QualityLevel.IRIDIUM]:.4f}")
        expected_multiple = sum(quality.crop_sell_price_multiplier * prob for quality, prob in distribution.items())
        return expected_multiple

class SeedType(StrEnum):
    PARSNIP_SEEDS = "Parsnip Seeds"
    BEAN_STARTER = "Bean Starter"
    CAULIFLOWER_SEEDS = "Cauliflower Seeds"
    POTATO_SEEDS = "Potato Seeds"
    TULIP_BULB = "Tulip Bulb"
    KALE_SEEDS = "Kale Seeds"
    JAZZ_SEEDS = "Jazz Seeds"

class SeedInfo(NamedTuple):
    seed_type: SeedType
    cost: int
    growth_time: int
    seasons: list[Season]
    xp: int
    sell_price: int 
    continued_growth_time: int | None = None
    
    def multiple(self, quality: QualityLevel=QualityLevel.NORMAL) -> float:
        return (float(self.sell_price) * quality.crop_sell_price_multiplier) / float(self.cost)

    def compute_exponential_multiple(self, fertilizer: FertilizerLevel, farming_level: int, days=28) -> float:
        if farming_level < 0 or farming_level > 14:
            raise ValueError("Farming level must be between 0 and 14 inclusive.")

        growth_periods = days // (self.growth_time + 1) # +1 to account for the planting day
        
        expected_sell_price_multiplier = fertilizer.compute_expected_sell_price_multiplier(farming_level)
        print(f"growth_periods: {growth_periods}")

        return ((float(self.sell_price) * expected_sell_price_multiplier) / float(self.cost)) ** growth_periods


ALL_SEEDS: dict[SeedType, SeedInfo] = {
    SeedType.PARSNIP_SEEDS: SeedInfo(
        seed_type=SeedType.PARSNIP_SEEDS,
        cost=20,
        growth_time=4,
        seasons=[Season.SPRING],
        xp=3,
        sell_price=35,
    ),

    SeedType.BEAN_STARTER: SeedInfo(
        seed_type=SeedType.BEAN_STARTER,
        cost=60,
        growth_time=10,
        seasons=[Season.SPRING],
        xp=7,
        sell_price=40,
        continued_growth_time=3,
    ),

    SeedType.CAULIFLOWER_SEEDS: SeedInfo(
        seed_type=SeedType.CAULIFLOWER_SEEDS,
        cost=80,
        growth_time=12,
        seasons=[Season.SPRING],
        xp=9,
        sell_price=175,
    ),

    SeedType.POTATO_SEEDS: SeedInfo(
        seed_type=SeedType.POTATO_SEEDS,
        cost=50,
        growth_time=6,
        seasons=[Season.SPRING],
        xp=6,
        sell_price=80,
    ),

    SeedType.TULIP_BULB: SeedInfo(
        seed_type=SeedType.TULIP_BULB,
        cost=20,
        growth_time=6,
        seasons=[Season.SPRING],
        xp=3,
        sell_price=30,
    ),

    SeedType.KALE_SEEDS: SeedInfo(
        seed_type=SeedType.KALE_SEEDS,
        cost=70,
        growth_time=6,
        seasons=[Season.SPRING],
        xp=8,
        sell_price=110,
    ),

    SeedType.JAZZ_SEEDS: SeedInfo(
        seed_type=SeedType.JAZZ_SEEDS,
        cost=30,
        growth_time=7,
        seasons=[Season.SPRING],
        xp=4,
        sell_price=50,
    ),
}

