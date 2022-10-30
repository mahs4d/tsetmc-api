from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from . import _core


class GroupType(Enum):
    PAPER = 'PAPER'
    INDUSTRIAL = 'INDUSTRIAL'


class Group(BaseModel):
    id: int
    code: int
    name: str
    description: str
    type: GroupType

    @staticmethod
    def get_all_groups() -> list[Group]:
        """
        returns list of symbol groups
        """

        raw_data = _core.get_group_static_data()
        return [Group(
            id=row['id'],
            code=row['code'],
            name=row['name'],
            description=row['description'],
            type=GroupType.PAPER if row['type'] == 'PaperType' else GroupType.INDUSTRIAL,
        ) for row in raw_data]
