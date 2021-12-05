from models.hoa import HOA
from typing import List
from repository import hoas


def get_hoas() -> List[HOA]:
    json_hoas = hoas.get_hoas()
    return map(lambda x: HOA(x.get("id"), x.get("name"), x.get("address")), json_hoas)


def add_hoa(name, address):
    hoa_id = len(hoas.get_hoas()) + 1
    hoas.add_hoa(HOA(hoa_id, name, address))
