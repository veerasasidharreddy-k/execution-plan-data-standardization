from src.models.canonical_schema import CanonicalField, CanonicalSchema
from src.models.execution_plan import ExecutionPlan, ExecutionPlanStep
from src.validation.validator import MappingValidator


def test_execution_plan_step_creation() -> None:
    plan = ExecutionPlan(source_file="source.csv", target_schema="customer")
    step = ExecutionPlanStep(
        name="profile_source",
        description="Profile the source file.",
        status="pending",
    )

    plan.add_step(step)

    assert plan.step_names() == ["profile_source"]


def test_missing_required_field_creates_qc_issue() -> None:
    schema = CanonicalSchema(
        name="customer",
        fields=[
            CanonicalField(name="customer_id", required=True, data_type="string"),
            CanonicalField(name="email", required=True, data_type="string"),
            CanonicalField(name="signup_date", required=False, data_type="date"),
        ],
    )
    column_mapping = {
        "source_customer_id": "customer_id",
    }

    issues = MappingValidator().validate_required_fields(schema, column_mapping)

    assert len(issues) == 1
    assert issues[0].code == "MISSING_REQUIRED_FIELD"
    assert issues[0].field_name == "email"
    assert issues[0].severity == "error"
