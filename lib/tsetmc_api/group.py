from typing import List

from .core.group import get_all_groups


class SymbolGroup:
    @staticmethod
    def get_all_groups() -> List[dict]:
        """
        گرفتن لیست گروه‌های صنعت
        """

        return get_all_groups()
