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

class Price(NamedTuple):
    standard: int
    silver: int
    gold: int

class SeedInfo(NamedTuple):
    seed_type: SeedType
    growth_time: int
    season: Season
    xp: int
    sell_price: Price
