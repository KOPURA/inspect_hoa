from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):

    @abstractmethod
    def serialize() -> Dict[str, Any]:
        pass
