from Constants import *

possible_names = ["Jan", "Kacper", "Mateusz", "Michal", "Jakub", "Szymon", "Filip", "Wojciech", "Adam", "Piotr",
                  "Stanislaw", "Tomasz", "Pawel", "Krzysztof", "Marcin", "Andrzej", "Karol", "Bartosz", "lukasz",
                  "Mikolaj", "Marek", "Robert", "Artur", "Damian", "Rafal", "Adrian", "Dominik", "Przemyslaw", "Jacek",
                  "Sebastian", "Grzegorz", "Dawid", "Patryk", "Oskar", "Bartlomiej", "Radoslaw", "Arkadiusz", "Maciej", "Daniel",
                  "Julian", "Hubert", "Alan", "Kamil", "Tadeusz", "Konrad", "Henryk", "Ignacy", "Aleksander", "Ryszard", "Jozef",
                  "Leszek", "Anna", "Julia", "Zuzanna", "Maja", "Hanna", "Alicja", "Maria", "Natalia", "Karolina",
                  "Wiktoria", "Oliwia", "Amelia", "Aleksandra", "Emilia", "Nikola", "Dominika", "Katarzyna", "Magdalena", "Martyna",
                  "Paulina", "Agata", "Patrycja", "Kamila", "Izabela", "Kinga", "Daria", "Monika", "Justyna", "Gabriela",
                  "Barbara", "Klaudia", "Ewa", "Joanna", "Aneta", "Elzbieta", "Sylwia", "Marzena", "Adrianna", "Lena", "Nadia",
                  "Dorota", "Ewelina", "Ilona", "Beata", "Agnieszka", "Marta", "Renata", "Agnieszka", "Nina", "Urszula",
                  "Weronika"]

possible_female_surnames = ["Nowak", "Kowalska", "Wisniewska", "Dabrowska", "Lewandowska", "Wojcik", "Kaminska",
                            "Kowalczyk", "Zielinska", "Szymanska", "Wozniak", "Kozlowska", "Jankowska", "Wojciechowska",
                            "Kwiatkowska", "Mazur", "Krawczyk", "Piotrowska", "Grabowska", "Nowakowska", "Pawlak",
                            "Michalska", "Adamczyk", "Dudek", "Zajac", "Wieczorek", "Jablonska", "Krol", "Marciniak",
                            "Zajac", "Krol", "Witkowska", "Walczak", "Baran", "Rutkowska", "Michalak", "Szewczyk", "Olszewska",
                            "Tomczak", "Pietrzak","Jasinska", "Zalewska", "Wlodarczyk", "Jakubowska", "Lis",
                            "Kubiak", "Gajewska", "Bednarek", "Wrobel"]

possible_male_surnames = ["Nowak", "Kowalski", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski",
                          "Zielinski", "Szymanski", "Wozniak", "Dabrowski", "Kozlowski", "Jankowski", "Mazur",
                          "Wojciechowski", "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski",
                          "Zajac", "Krol", "Michalski", "Witkowski", "Jablonski", "Nowakowski", "Adamczyk", "Dudek",
                          "Pawlak", "Walczak", "Stepien", "Gajewski", "Baran", "Rutkowski", "Michalak",
                          "Szewczyk", "Olszewski", "Tomczak", "Kubiak", "Wlodarczyk", "Pietrzak", "Marciniak", "Jasinski",
                          "Zalewski", "Jakubowski", "Lis", "Kaczmarczyk", "Kucharski", "Wrobel", "Majewski"]

possible_worker_positions = ['researcher', 'analyst', 'CEO', 'supervisor']

positions_distribution = {
    "CEO": None,
    "researcher": 5,
    "analyst": 5,
    "supervisor": None
}

possible_street = ["Kolobrzeska", "Aleja Lipowa", "Sloneczna", "Kwiatowa", "Plac Wolnosci", "Piastowska", "Ogrodowa",
                   "Jagiellonska", "Mickiewicza",
                   "Wesola", "Krotka", "Akacjowa", "Lesna", "lakowa", "Polna", "Sportowa", "Mickiewicza", "Krucza",
                   "Brzozowa", "Reymonta", "3 Maja",
                   "Kwiatowa", "Rzeczna", "Kwiatowa", "Mickiewicza", "Wiosenna", "Spacerowa", "Topolowa", "Kwiatowa",
                   "Parkowa", "Sosnowa", "Mickiewicza",
                   "Zielona", "Koscielna", "Mickiewicza", "Piekna", "Slowackiego", "Mickiewicza", "Kwiatowa", "Chopina",
                   "Krotka", "Mickiewicza", "Konopna",
                   "Sienkiewicza", "Wiosenna", "Wspolna", "Sloneczna", "Piastowska", "Piekna", "Cicha", "Sloneczna",
                   "Kwiatowa", "Krotka", "Mickiewicza", "Ogrodowa",
                   "Piastowska", "Kwiatowa", "Lesna", "Kwiatowa", "Polna", "Krucza", "Brzozowa", "Reymonta", "3 Maja",
                   "Kwiatowa", "Rzeczna", "Kwiatowa", "Mickiewicza",
                   "Wiosenna", "Spacerowa", "Topolowa", "Kwiatowa", "Parkowa", "Sosnowa", "Mickiewicza", "Zielona",
                   "Koscielna", "Mickiewicza", "Piekna", "Slowackiego", "Mickiewicza",
                   "Kwiatowa", "Chopina", "Krotka", "Mickiewicza", "Konopna", "Sienkiewicza", "Wiosenna", "Wspolna",
                   "Sloneczna", "Piastowska", "Piekna", "Cicha", "Sloneczna",
                   "Kwiatowa", "Krotka", "Mickiewicza", "Ogrodowa", "Piastowska", "Kwiatowa", "Lesna"]

possible_type_property = ['flat', 'apartment', 'house', 'twin']

possible_developer = ["BlueSky Developers",
                      "GreenField Group",
                      "GoldenGate Builders",
                      "SilverStone Constructions",
                      "RedRock Developers",
                      "WhitePine Properties",
                      "BlackOak Developments",
                      "AmberGlow Builders",
                      "AzureView Constructions",
                      "CrimsonHill Homes",
                      "CopperLeaf Developers",
                      "PlatinumCrest Builders",
                      "EmeraldIsle Properties",
                      "SapphireShore Developments",
                      "RubyRidge Homes",
                      "DiamondPeak Constructions",
                      "OpalValley Builders",
                      "PearlPoint Properties",
                      "TopazTerrace Developments",
                      "JadeGrove Builders",
                      "OnyxHeights Constructions",
                      "GraniteGate Properties",
                      "MarbleMeadow Homes",
                      "QuartzQuarry Builders",
                      "SlateStream Developments",
                      "AmethystAcres Properties",
                      "SunsetBreeze Builders",
                      "SunrisePeak Constructions",
                      "MoonlightMansion Properties",
                      "StarlightSky Developments",
                      "GalaxyGlen Builders",
                      "CosmicCrest Constructions",
                      "NeptuneNest Properties",
                      "SaturnSprings Builders",
                      "VenusView Developments",
                      "MarsMeadow Constructions",
                      "JupiterJunction Properties",
                      "MercuryManor Builders",
                      "EarthEcho Developments",
                      "LunarLodge Properties",
                      "SolarScape Builders",
                      "OrionOasis Constructions",
                      "NovaNook Properties",
                      "CelestialCove Builders",
                      "StellarStream Constructions",
                      "OceanicOasis Properties",
                      "ContinentalCrest Builders",
                      "TerraTranquil Developments",
                      "ArcticAscent Properties",
                      "TropicalTide Builders",
                      "ForestFrontier Constructions",
                      "MeadowMist Properties",
                      "DesertDream Builders",
                      "SavannahSprings Developments",
                      "PrairiePeak Properties",
                      "MountainMajesty Builders",
                      "ValleyVista Constructions",
                      "CanyonCrest Properties",
                      "RiverRapids Builders",
                      "LakefrontLodge Developments",
                      "IslandInnovations Properties",
                      "PeninsulaPrestige Builders",
                      "BaysideBuilders Constructions",
                      "HarborHaven Properties",
                      "CoveCrest Builders",
                      "BayviewBuilders Developments",
                      "SeasideShore Properties",
                      "BeachfrontBuilders Builders",
                      "CliffsideConstructions Constructions",
                      "HighlandHaven Properties",
                      "SummitSprings Builders",
                      "PeakPride Developments",
                      "PlateauPrestige Properties",
                      "HilltopHaven Builders",
                      "RidgecrestConstructions Constructions",
                      "BluffBreeze Properties",
                      "PinnaclePride Builders",
                      "CliffsideConstructions Developments",
                      "SkylineShore Properties",
                      "AerialAscent Builders",
                      "HorizonHaven Constructions",
                      "PanoramicPrestige Properties",
                      "VistaValley Builders",
                      "OutlookOasis Developments",
                      "ProspectPeak Properties",
                      "Eagle'sNest Builders",
                      "FalconFlight Constructions",
                      "CondorCrest Properties",
                      "HawkHaven Builders",
                      "Owl'sOutpost Developments",
                      "Robin'sRoost Properties",
                      "CardinalCove Builders",
                      "BlueJayBuilders Constructions",
                      "HummingbirdHaven Properties",
                      "SparrowSprings Builders",
                      "RavenRidge Developments",
                      "LarkLodge Properties",
                      "FinchFrontier Builders",
                      "Wren'sNook Constructions",
                      "Dove'sDale Properties",
                      "PelicanPride Builders",
                      "Swan'sSong Developments",
                      "GooseGrove Properties",
                      "PenguinPrestige Builders",
                      "PuffinPeak Constructions",
                      "AlbatrossAcres Properties",
                      "SeagullShore Builders",
                      "TernTerrace Developments",
                      "KingfisherKrest Properties",
                      "OystercatcherOasis Builders",
                      "SandpiperSprings Constructions",
                      "HeronHaven Properties",
                      "EgretEnclave Builders",
                      "CraneCove Developments",
                      "IbisIsland Properties",
                      "StorkSprings Builders",
                      "PelicanPoint Constructions",
                      "FlamingoFrontier Properties",
                      "CormorantCrest Builders",
                      "OspreyOasis Developments",
                      "Duck'sDale Properties",
                      "GannetGrove Builders",
                      "FrigateFlight Constructions",
                      "PetrelPrestige Properties",
                      "Seal'sShore Builders",
                      "WalrusWaters Developments",
                      "PolarPride Properties",
                      "ArcticAscent Builders",
                      "GlacierGrove Constructions",
                      "AuroraAcres Properties",
                      "AvalancheAvenue Builders",
                      "BlizzardBreeze Developments",
                      "FrozenFrontier Properties",
                      "IcebergIsland Builders",
                      "SnowflakeSprings Constructions",
                      "TundraTerrace Properties",
                      "IcicleInnovations Builders",
                      "FrostyFrontier Constructions",
                      "SleetSprings Properties",
                      "HailstoneHeights Builders",
                      "SnowdriftSpires Developments",
                      "PolarPrestige Properties",
                      "IglooInnovations Builders",
                      "SnowcapSummit Constructions",
                      "GlacialGrove Properties",
                      "HuskyHaven Builders",
                      "MalamuteMeadow Developments",
                      "SiberianSprings Properties",
                      "YukonYards Builders",
                      "TundraTerrace Developments",
                      "AlaskaAcres Properties",
                      "PolarPrestige Builders",
                      "KodiakKrest Constructions",
                      "PenguinPeak Properties",
                      "GrizzlyGrove Builders",
                      "MooseMansion Developments",
                      "CaribouCove Properties",
                      "WolfWoods Builders",
                      "Eagle'sEyrie Constructions",
                      "BearBrook Properties",
                      "SalmonSprings Builders",
                      "TroutTerrace Developments",
                      "WalrusWaters Properties",
                      "Seal'sShore Builders",
                      "PuffinPrestige Constructions",
                      "NarwhalNest Properties",
                      "OrcaOutpost Builders",
                      "BelugaBreeze Developments",
                      "PolarPride Properties",
                      "PenguinPeak Builders",
                      "Seal'sShore Constructions",
                      "ArcticAscent Properties",
                      "WalrusWaters Builders",
                      "Seal'sShore Developments",
                      "PenguinPeak Properties",
                      "ArcticAscent Builders",
                      "WalrusWaters Developments",
                      "Seal'sShore Properties",
                      "PenguinPeak Builders"]

cities = {
        "Warsaw": ["Praga", "Mokotow", "Ursynow", "Bielany", "Wola"],
        "Krakow": ["Old Town", "Kazimierz", "Podgorze", "Nowa Huta", "Bronowice"],
        "Wroclaw": ["Stare Miasto", "Krzyki", "Fabryczna", "Psie Pole", "Biskupin"],
        "Poznan": ["Jezyce", "Wilda", "Grunwald", "Stare Miasto", "Nowe Miasto"],
        "Gdansk": ["Wrzeszcz", "Oliwa", "Sopot", "Glowny", "Orunia"],
        "Szczecin": ["srodmiescie", "Polnoc", "Zachod", "Prawobrzeze", "swieta"],
        "Lodz": ["srodmiescie", "Baluty", "Polesie", "Widzew", "Gorna"],
        "Katowice": ["srodmiescie", "Zawodzie", "Brynow", "Bogucice", "Dab"],
        "Gdynia": ["Wzgorze sw. Maksymiliana", "Witomino", "Orlowo", "Chwarzno-Wiczlino", "Redlowo"],
        "Bydgoszcz": ["Stare Miasto", "Fordon", "Blonie", "Wzgorze Wolnosci", "Szwederowo"]
    }

residential_areas = ["Vivaldi Estate", "Sunset Heights", "Green Meadows", "Lakeview Gardens", "Pinecrest Ridge",
                     "Whispering Pines", "Maplewood Terrace", "Rosewood Park", "Sunnydale Villas", "Bayside Manor",
                     "Golden Gate Apartments", "Harbor View Estates", "Meadowbrook Meadows", "Riverfront Residences",
                     "Forest Edge", "Oakwood Oaks", "Willow Creek", "Highland Hills", "Hilltop Haven", "Cedar Crest",
                     "Peachtree Place", "Riverside Village", "Marina Bay", "Ocean Breeze", "Summit Heights",
                     "Valley View", "Garden Grove", "Aspen Meadows", "Brookside Manor", "Lakeside Living",
                     "Sunrise Springs", "Canyon Creek", "Hillcrest Heights", "Palm Paradise", "Misty Ridge",
                     "Serenity Springs", "Amber Gardens", "Cobblestone Cove", "Whitewater Pointe", "Silver Springs"]

first_words = ["Master", "Expert", "Golden Hand", "Reliable", "Professional", "Craftsman", "Renovation", "Remodeling",
               "Inspiration", "Construction", "Elite", "Top-notch", "Superior", "Ace", "Skillful", "Dynamic", "Efficient",
               "Innovative", "Premier", "Best", "Ultimate", "Exceptional", "Prime", "Leading", "Advanced", "Majestic",
               "Eminent", "High-Quality", "Exquisite", "Great"]

second_words = ["Renovation", "Remodeling", "Construction", "Structural", "Finishing", "Architectural", "Design", "Master",
                "Building", "Craftsmanship", "Excellence", "Solutions", "Builders", "Services", "Works", "Pros", "Builders",
                "Projects", "Solutions", "Masters", "Renovators", "Contractors", "Experts", "Builders", "Creations",
                "Crafters", "Innovations", "Works", "Prospects", "Designs", "Creators"]


reasons_for_delay = ['No delay', 'Material shortages', 'Unexpected structural issues' , 'Weather-related setbacks', 'Changes in project scope', 'Labor shortages', 'Budgetary constraints']

specializations = [
        'Interior Design', 'Painting', 'Flooring', 'Electrical', 'Renovation', 'Plumbing', 'Carpentry', 'Landscaping', 'HVAC', 'Masonry'
    ]

possible_certifications = [
        'LEED Certification', 'PMP Certification', 'OSHA 30-Hour Certification', 'EPA Lead-Safe Certification', 'First Aid Certification', 'Six Sigma Certification', 'AWS Certified Solutions Architect', 'CompTIA Security+', 'Certified ScrumMaster', 'Cisco Certified Network Associate'
    ]
possible_number_workers = ['between 1-5', 'between 6-15','between 16-50','between 50-200', 'over 200']

possible_certifications_range = ['between 0-5', 'between 6-15','between 16-50','over 50']

possible_finished_renovation_number = ['between 0-5', 'between 6-20', 'between 21-100', 'between 101-500', 'more than 500']

possible_establish_years = ['between 1900-1950', 'between 1951-1980','between 1981-2000', 'between 2001-2024']

possible_production_range = ['between 1900-1950','between 1951-1980','between 1981-2000','between 2001-2010','between 2011-2020','between 2021-2024']