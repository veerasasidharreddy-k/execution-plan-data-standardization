from src.models.canonical_schema import CanonicalField, CanonicalSchema
from src.models.execution_plan import ExecutionPlan, ExecutionPlanStep
from src.validation.validator import MappingValidator


def build_sample_schema() -> CanonicalSchema:
    return CanonicalSchema(
        name="sample_customer_schema",
        fields=[
            CanonicalField(name="customer_id", required=True, data_type="string"),
            CanonicalField(name="email", required=True, data_type="string"),
            CanonicalField(name="signup_date", required=False, data_type="date"),
        ],
    )


def build_sample_execution_plan(schema: CanonicalSchema) -> ExecutionPlan:
    plan = ExecutionPlan(source_file="sample_customers.csv", target_schema=schema.name)
    plan.add_step(
        ExecutionPlanStep(
            name="profile_source",
            description="Profile source CSV columns, rows, and sample records.",
            status="pending",
        )
    )
    plan.add_step(
        ExecutionPlanStep(
            name="detect_schema",
            description="Compare source fields against the target canonical schema.",
            status="pending",
        )
    )
    plan.add_step(
        ExecutionPlanStep(
            name="validate_mapping",
            description="Validate that required target fields are mapped.",
            status="pending",
        )
    )
    plan.add_step(
        ExecutionPlanStep(
            name="generate_preview",
            description="Generate a preview of standardized records.",
            status="pending",
        )
    )
    return plan


def main() -> None:
    schema = build_sample_schema()
    column_mapping = {
        "source_customer_id": "customer_id",
        "source_signup_date": "signup_date",
    }

    plan = build_sample_execution_plan(schema)
    issues = MappingValidator().validate_required_fields(schema, column_mapping)

    print("Execution plan steps:")
    for step_name in plan.step_names():
        print(f"- {step_name}")

    print("\nQC issues:")
    for issue in issues:
        field = f" ({issue.field_name})" if issue.field_name else ""
        print(f"- [{issue.severity}] {issue.code}{field}: {issue.message}")


if __name__ == "__main__":
    main()
