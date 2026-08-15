from __future__ import annotations

from pathlib import Path


def translabel(
    input_dir: Path,
    target_label: int,
    output_dir: Path | None = None,
) -> Path:
    destination = output_dir or input_dir.parent / f"trans_{input_dir.name}"
    destination.mkdir(parents=True, exist_ok=True)

    for source_file in input_dir.glob("*.txt"):
        converted_lines = []
        for line in source_file.read_text(encoding="utf-8").splitlines():
            original_label, separator, coordinates = line.partition(" ")
            converted_lines.append(
                f"{target_label}{separator}{coordinates}" if original_label and separator else line
            )
        (destination / source_file.name).write_text(
            "\n".join(converted_lines) + ("\n" if converted_lines else ""),
            encoding="utf-8",
        )

    return destination
