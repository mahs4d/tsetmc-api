from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, Dict

from . import core as group_core

GroupId = str


@dataclass
class SymbolGroup:
    code: GroupId
    name: str

    @staticmethod
    def get_all_groups() -> List[SymbolGroup]:
        raw_groups = group_core.get_all_groups()
        return SymbolGroup.from_dict(raw_groups)

    @staticmethod
    def from_dict(dictionary: Union[Dict, List]) -> Union[SymbolGroup, List[SymbolGroup]]:
        if type(dictionary) == list:
            return [SymbolGroup.from_dict(d) for d in dictionary]

        return SymbolGroup(
            code=dictionary.get('code'),
            name=dictionary.get('name'),
        )
