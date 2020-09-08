from math import sqrt
import numpy as np
import hashlib


def vectorize(profile):
    """Dummy profile vectorization, using profile main field, e.g. `_id`, `name`, `surname`"""
    assert '_id' in profile
    assert 'name' in profile
    assert 'surname' in profile
    profile_summary = '_'.join(profile.values()).encode('utf-8')
    hash_object = hashlib.sha512(profile_summary)
    hex_dig = hash_object.hexdigest()
    return np.asarray([int(i, 16) / 64 for i in hex_dig])


def norm(vector):
    return sqrt(sum(x * x for x in vector))


def cosine_similarity(vec_a, vec_b):
    """Calculate Cosine similarity between two vectors"""
    norm_a = norm(vec_a)
    norm_b = norm(vec_b)
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    return dot / (norm_a * norm_b)
