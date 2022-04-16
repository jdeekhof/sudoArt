from Collector import collector

for sub in ['art', 'EarthPorn', 'waterporn', 'SkyPorn','desertporn','winterporn',
            'AutumnPorn','WeatherPorn','spaceporn','SpringPorn','SummerPorn','lavaporn',
            'lakeporn','CityPorn','ruralporn','ArchitecturePorn','AbandonedPorn','DestructionPorn',
            ]:
    collector.retrieve(sub)

