from flask_restful import Resource
# from flask_jwt import jwt_required
from models.team import TeamModel


class Team(Resource):

    # @jwt_required()
    def get(self, team_name):

        try:
            team_list = TeamModel.find_by_team(team_name)
            
            if team_list:
                return {'results': team_list}, 200

            else:
                return {'message': '{} is not a valid team name'.format(team_name)}
        except:
            return {"message": "An error occurred retrieving the team list."}, 500 # internal server error

class TeamList(Resource):
    def get(self):
        return TeamModel.get_all_teams_list()



