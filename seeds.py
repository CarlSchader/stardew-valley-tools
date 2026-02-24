from stardew_types import Season, Price, SeedInfo, SeedType

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

if __name__ == "__main__":
    print(ALL_SEEDS)
