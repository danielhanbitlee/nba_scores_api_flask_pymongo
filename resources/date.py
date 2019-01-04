from flask_restful import Resource
# from flask_jwt import jwt_required
from models.date import DateModel


class Date(Resource):
    # @jwt_required()
    def get(self, date):
        try:
            date_list = DateModel.find_by_date(date)

            if date_list: 
                return {'results': date_list}, 200

            else:
                return "No date available", 404 # not found

        except:
            return {'message': 'An error occurred while retrieving the information'}, 500
