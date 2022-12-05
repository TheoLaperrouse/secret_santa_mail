import random
import json


if __name__ == "__main__":
    infos = open('user_infos.json')
    user_infos = json.load(infos)
    pairs = []

    names = list(user_infos.keys())
    random.shuffle(names)
    for name in user_infos.keys():
        pairs.append([name, names.pop()])

    print(pairs)
