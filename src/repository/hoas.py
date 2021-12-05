import json
from models.hoa import HOA


def get_hoas():
    with open("../data/hoas.json") as f:
        return json.load(f)


def add_hoa(hoa: HOA):
    # The following approach might be a little ugly, but
    # allows us to do the whole "operation" within a single
    # file open.
    with open("../data/hoas.json", "r+") as f:
        data = json.load(f)
        f.seek(0)
        data.append(hoa.serialize())
        json.dump(data, f)
        f.truncate()
