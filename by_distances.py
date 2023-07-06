from math import acos, sin, cos, radians
from table_writers import HTMLTableWriter


def to_radians(val: str) -> float:
    """Takes a string with degrees, minutes, seconds and returns radians"""
    split_degrees = val.split('° ')
    degrees = int(split_degrees[0])
    split_minutes = split_degrees[1].split("' ")
    minutes = int(split_minutes[0])
    split_seconds = split_minutes[1].split("''")
    seconds = int(split_seconds[0])
    return radians(degrees + minutes / 60 + seconds / 3600)


def distance(lat1: float, long1: float, lat2: float, long2: float) -> float:
    """Takes radian coordinates pair and returns the distance between them in km"""
    return 6371.01 * acos(
        sin(lat1) * sin(lat2) +
        cos(lat1) * cos(lat2) * cos(long1 - long2))


def build_distance_table(coordinates: dict[str, list[float]]) -> list[list[str]]:
    """Returns a list with [0] - list of city names, [1:] - [city name, *distance to other cities]"""
    data_table = []
    first_row = []
    for city_name, (lat1, lon1) in coordinates.items():
        first_row.append(city_name)
    first_row.insert(0, ' ')
    data_table.append(first_row)
    for city_name, (lat1, lon1) in coordinates.items():
        distance_table = []
        for other_city_name, (lat2, lon2) in coordinates.items():
            if city_name != other_city_name:
                distance_table.append(f'{distance(lat1, lon1, lat2, lon2):.2f}')
            else: 
                distance_table.append(' ')
        distance_table.insert(0, city_name)    
        data_table.append(distance_table)    
            
    return data_table


if __name__ == '__main__':
    CITIES = {

        'Брест': ["52° 5' 51''", "23° 41' 15''"],
        'Витебск': ["55° 11' 25''", "30° 12' 17''"],
        'Гомель': ["52° 26' 4''", "30° 58' 31''"],
        'Гродно': ["53° 41' 18''", "23° 49' 32''"],
        'Минск': ["53° 54' 0''", "27° 34' 0''"],
        'Могилев': ["53° 55' 0''", "30° 20' 41''"]
    }
    cities_radians_dict = {}
    for city_name, (lat, lon) in CITIES.items():
        cities_radians_dict.update({city_name: [to_radians(lat), to_radians(lon)]})
    data_table = build_distance_table(cities_radians_dict)
    writer = HTMLTableWriter('output.html')
    writer.write(data_table)