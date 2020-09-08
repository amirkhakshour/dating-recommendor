from flask_restful import Resource
from utils.db import db, DBNotFoundException
from utils.models import Profile


class Health(Resource):

    def get(self):
        return {'status': 'ok'}, 200


class Recommend(Resource):

    def get(self, _id=None, n=None):
        assert _id
        assert n
        try:
            profile = db.get_by_id(_id)
        except DBNotFoundException as e:
            return {'message': str(e)}, 404
        p = Profile(**profile)
        result = p.k_nearest_neighbors_naive(n)
        return result, 200
