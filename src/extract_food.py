from __future__ import annotations

from collections.abc import Iterable
from pathlib import PureWindowsPath


def name_after_first_separator(filename: str, separator: str) -> str:
    _, found, food_name = filename.partition(separator)
    return food_name if found else filename


def extract_food_label(filelist: Iterable[str]) -> list[str]:
    return [
        name_after_first_separator(
            PureWindowsPath(filename).stem.removeprefix("trans_labels_"),
            "_",
        )
        for filename in filelist
    ]


def extract_food_img(filelist: Iterable[str]) -> list[str]:
    return [
        name_after_first_separator(
            PureWindowsPath(filename).stem.removesuffix("New"),
            " ",
        )
        for filename in filelist
    ]


def match_food(food_name: str, filelist: Iterable[str]) -> str | None:
    matches = [filename for filename in filelist if food_name in filename]
    return matches[-1] if matches else None
