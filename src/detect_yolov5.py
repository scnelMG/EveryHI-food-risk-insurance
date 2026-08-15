from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from subprocess import run
from sys import executable


@dataclass(frozen=True, slots=True)
class DetectionRun:
    yolo_root: Path
    weights: Path
    source: Path
    dataset_config: Path


def run_detection(spec: DetectionRun) -> int:
    command = (
        executable,
        str(spec.yolo_root / "detect.py"),
        "--weights",
        str(spec.weights),
        "--source",
        str(spec.source),
        "--data",
        str(spec.dataset_config),
    )
    return run(command, check=False).returncode
