from src.models.canonical_schema import CanonicalSchema
from src.models.qc_issue import QCIssue


class MappingValidator:
    def validate_required_fields(
        self,
        schema: CanonicalSchema,
        column_mapping: dict[str, str],
    ) -> list[QCIssue]:
        mapped_target_fields = set(column_mapping.values())
        issues = []

        for field_name in schema.required_field_names():
            if field_name not in mapped_target_fields:
                issues.append(
                    QCIssue(
                        code="MISSING_REQUIRED_FIELD",
                        message=f"Required target field '{field_name}' is not mapped.",
                        severity="error",
                        field_name=field_name,
                    )
                )

        return issues
