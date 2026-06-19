from dataclasses import dataclass
from typing import Optional


@dataclass
class QCIssue:
    code: str
    message: str
    severity: str
    field_name: Optional[str] = None
