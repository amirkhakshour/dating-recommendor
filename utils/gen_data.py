from numpy import random
from bson import ObjectId
import pickle


def _generate_people_names():
    with open('data/names.txt', 'r') as names_file:
        names = names_file.readlines()
    names = [name.strip() for name in names]
    with open('data/surnames.txt', 'r') as surnames_file:
        surnames = surnames_file.readlines()
    surnames = [name.strip() for name in surnames]
    people = []
    for i in range(10000):
        person = {'name': random.choice(names),
                  'surname': random.choice(surnames),
                  '_id': str(ObjectId())}
        people.append(person)
    pickle_out = open("./data/profiles.pickle", "wb")
    pickle.dump(people, pickle_out)
    pickle_out.close()


if __name__ == '__main__':
    _generate_people_names()
