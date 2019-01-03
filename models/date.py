from db import db


class DateModel:

    def find_by_date(date):    
        scores = db.Scores
        mongo_query = scores.find({'date' : date}, {'_id': 0})
                    
        return list(mongo_query)

         
