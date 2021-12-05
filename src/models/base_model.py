from abc import ABC, abstractmethod
from typing import Dict, TypeVar, Generic

T = TypeVar('T')


class BaseModel(ABC, Generic[T]):

    @abstractmethod
    def serialize() -> Dict[str, T]:
        pass
