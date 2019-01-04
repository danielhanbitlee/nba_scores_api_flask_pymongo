from db import db


class CityModel:

    def find_by_city(city_name):

        scores = db.Scores 
        mongo_query = scores.find({'$or': [ {'team_home_city' : city_name}, {'team_away_city': city_name}] },
                                  {'_id': 0}).sort("date", 1)
    
        return list(mongo_query)

    def get_all_cities_list():
        scores = db.Scores 
        cities = scores.distinct('team_home_city')
        return {'cities': cities}

