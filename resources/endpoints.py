from flask_restful import Resource


class Recommend(Resource):

    def get(self, _id=None, n=None):
        assert _id
        assert n
