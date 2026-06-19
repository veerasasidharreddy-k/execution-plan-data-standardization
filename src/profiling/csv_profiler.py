import csv
from pathlib import Path
from typing import Any


class CsvProfiler:
    def profile(self, file_path: str) -> dict[str, Any]:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(file_path)

        with path.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            sample_rows = []
            row_count = 0

            for row in reader:
                row_count += 1
                if len(sample_rows) < 5:
                    sample_rows.append(dict(row))

        return {
            "file_name": path.name,
            "columns": reader.fieldnames or [],
            "row_count": row_count,
            "sample_rows": sample_rows,
        }
