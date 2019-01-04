from flask_restful import Resource
# from flask_jwt import jwt_required
from models.city import CityModel


class City(Resource):

    # @jwt_required()
    def get(self, city_name):
        try:
            city_list = CityModel.find_by_city(city_name)

            if city_list:
                return {'results': city_list}, 200

            else:
                return '{} is an invalid city name'.format(city_name), 404
        except:
            return {"message": "An error occurred retrieving the team list."}, 500 # internal server error


class CityList(Resource):
    def get(self):
        return CityModel.get_all_cities_list()
