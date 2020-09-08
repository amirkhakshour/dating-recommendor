from math import sqrt
import time
import numpy as np
import hashlib
import heapq


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


def k_smallest_items(capacity=10):
    """Always yields k smallest Items."""
    q = []
    counter = 0
    while True:
        value, item = yield q
        if value is None:
            break
        if len(q) < capacity:
            heapq.heappush(q, (-value, counter, item))
        else:
            heapq.heappushpop(q, (-value, counter, item))

        counter += 1


def debug_time(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        ret_val = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return ret_val

    return wrapper
