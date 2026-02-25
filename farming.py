from stardew_types import FertilizerLevel, QualityLevel, ALL_SEEDS

def print_crop_quality_distributions() -> None:
    for fertilizer_level in FertilizerLevel:
        print(f"Fertilizer Level: {fertilizer_level.name}")
        for farming_level in range(0, 15):
            dist = fertilizer_level.compute_crop_quality_distribution(farming_level)
            print(f"Farming Level: {farming_level}: Distribution: {dist[QualityLevel.NORMAL]:.4f}, {dist[QualityLevel.SILVER]:.4f}, {dist[QualityLevel.GOLD]:.4f}, {dist[QualityLevel.IRIDIUM]:.4f}")
        print()

def print_all_seed_exponential_multiples(fertilizer: FertilizerLevel, farming_level: int) -> None:
    days = 28
    for seed_info in ALL_SEEDS.values():
        print(f"Seed: {seed_info.seed_type.name}")
        multiple = seed_info.compute_exponential_multiple(fertilizer, farming_level, days)
        print(f"    Farming Level: {farming_level}: Exponential Multiple: {multiple:.4f}")
        print()

if __name__ == "__main__":
    # print_crop_quality_distributions()
    print_all_seed_exponential_multiples(FertilizerLevel.NONE, 0)
    
