#!usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: list[Any],
            criteria: Optional[str] = None
            ) -> list[Any]:
        return data_batch

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.id,
            "processed_count":  self.processed_count
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: list[Any]) -> str:
        temps = []
        for data in data_batch:
            name, value = data.split(":", 1)
            if name == "temp":
                temps.append(float(value))
        count = len(data_batch)
        temps_len = len(temps)
        if temps_len == 0:
            avg_temp = 0
        else:
            avg_temp = sum(temps) / temps_len
        self.processed_count += count
        result = f"{count} readings processed, avg temp: {avg_temp}°C"
        return "Sensor analysis: " + result

    def filter_data(
            self,
            data_batch: list[Any],
            criteria: Optional[str] = None
            ) -> list[Any]:
        if criteria == "critical":
            return [d for d in data_batch if "alert" in d.lower()]
        return data_batch


class TransactionStream(DataStream):

    def process_batch(self, data_batch: list[Any]) -> str:
        net_flow = 0
        for data in data_batch:
            action, value = data.split(":", 1)
            if action == "buy":
                net_flow += int(value)
            elif action == "sell":
                net_flow -= int(value)
        count = len(data_batch)
        self.processed_count += count
        sign = "+" if net_flow >= 0 else ""
        result = f"{count} operations, net flow: {sign}{net_flow} units"
        return "Transacton analysis: " + result

    def filter_data(
            self,
            data_batch: list[Any],
            criteria: Optional[str] = None
            ) -> list[Any]:
        if criteria == "large":
            return [d for d in data_batch
                    if int(d.split(":")[1]) > 100]
        return data_batch


class EventStream(DataStream):

    def process_batch(self, data_batch: list[Any]) -> str:
        error_count = sum(1 for d in data_batch if d == "error")
        count = len(data_batch)
        self.processed_count += count
        return f"Event analysis: {count} events, {error_count} error detected"

    def filter_data(
            self,
            data_batch: list[Any],
            criteria: Optional[str] = None
            ) -> list[Any]:
        if criteria == "error":
            return [d for d in data_batch if d == "error"]
        return data_batch


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: list[list[Any]]) -> list[str]:
        results = []
        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            results.append(result)
        return results


if __name__ == "__main__":
    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

        sensor = SensorStream("SENSOR_001")
        transaction = TransactionStream("TRANS_001")
        event = EventStream("EVENT_001")

        print("\nInitializing Sensor Stream...")
        print(f"Stream ID: {sensor.id}, Type: Environmental Data")
        sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        print(f"Processing sensor batch: {sensor_batch}")
        print(sensor.process_batch(sensor_batch))

        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {transaction.id}, Type: Financial Data")
        transaction_batch = ["buy:100", "sell:150", "buy:75"]
        print(f"Processing transaction batch: {transaction_batch}")
        print(transaction.process_batch(transaction_batch))

        print("\nInitializing Event Stream...")
        print(f"Stream ID: {event.id}, Type: System Events")
        event_batch = ["login", "error", "logout"]
        print(f"Processing event batch: {event_batch}")
        print(event.process_batch(event_batch))

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        p = StreamProcessor()
        p.add_stream(SensorStream("SENSOR_002"))
        p.add_stream(TransactionStream("TRANS_002"))
        p.add_stream(EventStream("EVENT_002"))

        batches = [
            ["temp:20.0", "humidiy:70"],
            ["buy:200", "sell:50", "buy:100", "sell:50"],
            ["login", "error", "logout"]
        ]
        results = p.process_all(batches)
        print("Batch 1 Results:")
        for result in results:
            print(f"- {result}")

        print("\nStream filtering active: High-priority data only")
        filtered_sensor = p.streams[0].filter_data(batches[0], "critical")
        filtered_trans = p.streams[1].filter_data(batches[1], "large")
        print("Filtered results: "
              f"{len(filtered_sensor)} critical sensor alerts, "
              f"{len(filtered_trans)} large transaction")

        print("\nAll stream processed successfully, Nexus throughout optimal.")

    except Exception as e:
        print(f"***Error: {e}")
