from dataclasses import dataclass, field


@dataclass
class ExecutionPlanStep:
    name: str
    description: str
    status: str


@dataclass
class ExecutionPlan:
    source_file: str
    target_schema: str
    steps: list[ExecutionPlanStep] = field(default_factory=list)

    def add_step(self, step: ExecutionPlanStep) -> None:
        self.steps.append(step)

    def step_names(self) -> list[str]:
        return [step.name for step in self.steps]
