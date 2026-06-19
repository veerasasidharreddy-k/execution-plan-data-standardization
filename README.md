# Execution-Plan-Driven Data Standardization

## Overview

This repository contains an initial Python prototype for execution-plan-driven data standardization. It demonstrates how raw source files can be profiled, compared against a canonical schema, validated through a mapping layer, and surfaced as structured quality-control issues.

The current implementation is intentionally small and testable. It is not a production system; it is a portfolio prototype focused on data infrastructure patterns that can support reliable AI, analytics, and downstream automation workflows.

## Technical Write-Up

For the design thinking behind this prototype, see:

[Execution-Plan-Driven Data Standardization for Reliable AI and Analytics Workflows](./ARTICLE.md)

## Problem

Data standardization workflows often start with inconsistent source files. CSV exports, manual uploads, and system-generated reports may differ in column names, required fields, structure, and data quality.

Without a clear schema model and validation process, downstream systems can receive incomplete or ambiguous data. This creates risk for analytics, machine learning, reporting, and AI-assisted workflows that depend on trustworthy structured inputs.

## Current Prototype

The prototype currently includes:

- Canonical schema models for required and optional target fields.
- Execution plan models for representing workflow steps.
- CSV profiling using Python's standard `csv` library.
- Mapping validation for required canonical fields.
- QC issue generation for missing required mappings.
- A small runnable demo in `src/main.py`.
- Pytest coverage for execution plan creation and required-field validation.

The sample execution plan includes these steps:

- `profile_source`
- `detect_schema`
- `validate_mapping`
- `generate_preview`

## Folder Structure

```text
src/
  __init__.py
  main.py
  models/
    __init__.py
    canonical_schema.py
    execution_plan.py
    qc_issue.py
  profiling/
    __init__.py
    csv_profiler.py
  validation/
    __init__.py
    validator.py
tests/
  test_execution_plan.py
requirements.txt
```

## How to Run

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the sample prototype:

```bash
python -m src.main
```

The demo builds a sample canonical schema, creates a sample mapping with one missing required field, builds an execution plan, and prints the generated QC issue.

## Tests

Run the test suite:

```bash
pytest
```

The current tests verify:

- Execution plan step creation.
- QC issue generation when a required canonical field is missing from the mapping.

## Future Extensions

Potential next steps include:

- Add richer CSV profiling for null counts, inferred data types, and distinct values.
- Add preview generation for standardized output rows.
- Expand mapping validation for duplicate mappings, unknown target fields, and type mismatches.
- Introduce schema drift detection across repeated source files.
- Add deterministic mapping suggestions before introducing any LLM-assisted workflow.
- Support additional file formats such as Excel.
- Persist execution plans and QC results as reviewable artifacts.
- Add human-in-the-loop approval for mappings and validation exceptions.
