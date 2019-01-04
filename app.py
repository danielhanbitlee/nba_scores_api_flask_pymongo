from flask import Flask, render_template
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.date import Date
from resources.team import Team, TeamList
from resources.city import City, CityList

app = Flask(__name__)
app.secret_key = 'daniel'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth endpt created

api.add_resource(Date, '/date/<string:date>')
api.add_resource(Team, '/team/<string:team_name>')
api.add_resource(TeamList, '/team_list')
api.add_resource(City, '/city/<string:city_name>')
api.add_resource(CityList, '/city_list')
api.add_resource(UserRegister, '/register')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)

