#!usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        # stream_idを保存、処理件数のカウンターも初期化
        pass

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        # デフォルト実装：criteriaがNoneならそのまま返す
        pass

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        # デフォルト実装：stream_idと処理件数を返す
        pass
