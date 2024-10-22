from flask import Flask
from flask_restful import Api, Resource

from modules.questionScrap import questionScrap
from modules.userScrap import userScrap

app = Flask(__name__)
api = Api(app)

class user(Resource):
    def get(self, username):
        scrapper = userScrap(username)
        return scrapper.fetchResponse()

class problem(Resource):
    def get(self):
        scrapper = questionScrap()
        return scrapper.fetchResponse()
        # return scrapper.fetchResponse()

api.add_resource(user, "/user/<string:username>")
api.add_resource(problem, '/problem/day')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
