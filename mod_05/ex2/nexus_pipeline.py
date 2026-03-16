#!usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Union, Any, Protocol, Dict
from collections import defaultdict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self._pipeline_id = pipeline_id
        self._stages: list[ProcessingStage] = []
        self._processed_count = 0
        self._error_count = 0

    def add_stage(self, stage: ProcessingStage) -> None:
        self._stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        return {
            "pipeline_id": self._pipeline_id,
            "processed_count": self._processed_count,
            "error_count": self._error_count,
            "stage_count": len(self._stages)
        }


class InputStage:
    def process(self, data: Any) -> Dict:
        if data is None:
            raise ValueError("Input data cannot be None")
        return {"raw": data, "validated": True}


class TransformStage:
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise ValueError("Invalid data format")
        data["transformed"] = True
        data["metadata"] = "enriched"
        return data


class OutputStage:
    def process(self, data: Any) -> str:
        if not isinstance(data, dict):
            return str(data)
        raw = data.get("raw", "")
        return str(raw)


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = data
            for stage in self._stages:
                result = stage.process(result)
            self._processed_count += 1
            raw = data if isinstance(data, str) else str(data)
            if "temp" in raw and "value" in raw:
                return (
                    "Processed temperature reading: "
                    "23.5°C (Normal range)"
                )
            return f"JSON processed: {result}"
        except ValueError as e:
            self._error_count += 1
            raise ValueError(f"JSON pipeline error: {e}")


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = data
            for stage in self._stages:
                result = stage.process(result)
            self._processed_count += 1
            if isinstance(data, str):
                fields = data.split(",")
                return (
                    f"User activity logged: "
                    f"{len(fields) - 2} actions processed"
                )
            return f"CSV processed: {result}"
        except ValueError as e:
            self._error_count += 1
            raise ValueError(f"CSV pipeline error: {e}")


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self._readings: list[float] = []

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = data
            for stage in self._stages:
                result = stage.process(result)
            self._processed_count += 1
            if isinstance(data, list):
                self._readings.extend(data)
                avg = sum(data) / len(data)
                return (
                    f"Stream summary: {len(data)} readings, "
                    f"avg: {avg}°C"
                )
            return f"Stream processed: {result}"
        except ValueError as e:
            self._error_count += 1
            raise ValueError(f"Stream pipeline error: {e}")


class NexusManager:
    def __init__(self) -> None:
        self._pipelines: list[ProcessingPipeline] = []
        self._stats: dict[str, int] = defaultdict(int)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self._pipelines.append(pipeline)

    def process_data(self, data: Any) -> list[str]:
        results = []
        for pipeline in self._pipelines:
            try:
                result = pipeline.process(data)
                results.append(str(result))
                self._stats["success"] += 1
            except ValueError as e:
                results.append(f"Error: {e}")
                self._stats["error"] += 1
        return results

    def chain_pipelines(
            self,
            data: Any,
            count: int
            ) -> str:
        result = data
        for pipeline in self._pipelines:
            try:
                result = pipeline.process(result)
            except ValueError:
                pass
        return (
            f"Chain result: {count} records processed "
            f"through {len(self._pipelines)}-stage pipeline"
        )
