from db import db


class TeamModel:

    def find_by_team(team_name):

        scores = db.Scores

        mongo_query = scores.find({'$or': [ {'team_home_name' : team_name}, {'team_away_name': team_name}] },
                                  {'_id': 0}).sort("date", 1)
    
        return list(mongo_query)

    def get_all_teams_list():
        scores = db.Scores
        teams = scores.distinct('team_home_name')
        return {'teams': teams}
