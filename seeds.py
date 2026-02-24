from stardew_types import Season, Price, SeedInfo, SeedType

ALL_SEEDS: dict[SeedType, SeedInfo] = {

    SeedType.PARSNIP_SEEDS: SeedInfo(
        seed_type=SeedType.PARSNIP_SEEDS,
        growth_time=4,
        season=Season.SPRING,
        xp=3,
        sell_price=Price(standard=35, silver=43, gold=52),
    ),
}
