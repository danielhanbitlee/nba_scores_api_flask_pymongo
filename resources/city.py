from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.city import CityModel


class City(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('city_name',
            type = str,
            required = True,
            help = "This field cannot be blank."
    )

    @jwt_required()
    def get(self):
        data = City.parser.parse_args()
        city_name = data.get('city_name')

        if not CityModel.valid_city_name(city_name):
            return {'message': 'City name {} is not valid'.format(city_name)}

        try:
            city_name = CityModel.process_city_name(city_name)
            city_list = CityModel.find_by_city(city_name)
            
            return {'results': city_list}, 200

        except:
            return {"message": "An error occurred retrieving the team list."}, 500 # internal server error


class CityList(Resource):
    def get(self):
        return CityModel.get_all_cities_list()
