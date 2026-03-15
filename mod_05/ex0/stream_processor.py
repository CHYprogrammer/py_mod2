#!usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    name = "Data Processor"

    @abstractmethod
    def process(self, data: Any) -> str:
        # Process the data and return result string
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # Validate if data is appropriate for this processor
        pass

    def format_output(self, result: str) -> str:
        # Format the output string
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

    def process(self, data: Any) -> str:
        print(f"Processing Data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid input")
        count = len(data)
        if count == 0:
            raise ValueError("Empty list")
        total = sum(data)
        avg = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, List):
            print("Validation: unverified")
            return False
        for d in data:
            if not isinstance(d, Union[int, float]):
                print("Validation: unverified")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output(Numeric): {result}"


class TextProcessor(DataProcessor):
    name = "Text Processor"

    def process(self, data: Any) -> str:
        print(f"Processing Data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid input")
        count = len(data)
        words = len(data.split(" "))
        return f"Processed text: {count} characters, {words} words"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            print("Validation: unverified")
            return False
        print("Validation: Text data verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output(Text): {result}"


class LogProcessor(DataProcessor):
    name = "Log Processor"

    def process(self, data: Any) -> str:
        print(f"Processing Data: {data}")
        if not self.validate(data):
            raise ValueError("Invalid input")
        log = data.split(":", 1)
        if log[0] == "ERROR":
            prefix = "ALERT"
        else:
            # prefix be same as log level
            prefix = log[0]
        return f"[{prefix}] {log[0]} level detected:{log[1]}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            print("Validation: unverified")
            return False
        print("Validation: Log entry verified")
        return True

    def format_output(self, result: str) -> str:
        return f"Output(Log): {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("=== Polymorphic Processing Demo ===\n")

    process_data = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "ERROR: Connection timeout")
    ]

    print("Processing multiple data types through same interface...")
    try:
        for (processor, data) in process_data:
            print()
            print(f"Initializing {processor.name}...")
            res = processor.process(data)
            print(processor.format_output(res))
    except ValueError as e:
        print(f"ERROR: {e}")

    print("\nFoundation systems online. Nexus ready for advanced stream.")
