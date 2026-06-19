from dataclasses import dataclass


@dataclass
class CanonicalField:
    name: str
    required: bool
    data_type: str


@dataclass
class CanonicalSchema:
    name: str
    fields: list[CanonicalField]

    def required_field_names(self) -> list[str]:
        return [field.name for field in self.fields if field.required]
