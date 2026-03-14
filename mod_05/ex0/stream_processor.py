#!usr/bin/env pythonn3

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: any) -> None:
        pass

    @abstractmethod
    def validate(self, data: any) -> None:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: any) -> None:
        pass

    def validate(selff, data: any) -> None:
        pass

    def format_output(self, result: str) -> str:
        pass


class TextProcessor(DataProcessor):
    def process(self, data: any) -> None:
        pass

    def validate(self, data: any) -> None:
        pass

    def format_output(self, result: str) -> str:
        pass


class LogProcessor(DataProcessor):
    def process(self, data: any) -> None:
        pass

    def validate(self, data: any) -> None:
        pass

    def format_output(self, result: str) -> str:
        pass


if __name__ == "__main__":
    