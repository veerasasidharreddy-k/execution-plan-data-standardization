# Execution-Plan-Driven Data Standardization

This repository explores a structured approach to converting raw business files into canonical data formats using deterministic profiling, schema detection, column mapping, validation, and execution plans.

## Problem

Enterprise data workflows often receive inconsistent CSV or Excel files from different clients, teams, source systems, or manual exports. These files may vary in column names, structure, formatting, data quality, and business meaning.

Manual cleanup is slow, error-prone, difficult to audit, and hard to scale across many clients or projects.

## Approach

The system is designed around an execution-plan model.

Instead of directly transforming a file in one step, the workflow first creates a structured plan that describes how the source file should be interpreted, validated, mapped, and converted.

## High-Level Workflow

1. Profile the source file
2. Detect schema and structure
3. Map source columns to canonical fields
4. Generate a target row model
5. Run validation and quality checks
6. Produce preview outputs
7. Write artifacts for review and traceability

## Core Concepts

### Source Profiling

Analyze the incoming file to understand its structure, column names, sample values, missing fields, data types, and potential quality issues.

### Schema Detection

Identify how the source file aligns with expected canonical structures.

### Column Mapping

Map source columns to target canonical fields using deterministic rules and validation logic.

### Execution Plan

Generate a structured plan that defines the steps required to transform the source file safely and repeatably.

### QC Validation

Capture validation issues such as missing required fields, invalid data types, unmapped columns, duplicate fields, and inconsistent values.

### Preview Generation

Produce preview outputs before final processing so users or downstream systems can review the transformation result.

## Why This Matters

Reliable AI and analytics systems depend on clean, structured, validated data.

Before an LLM, analytics dashboard, or machine learning workflow can reason over business data, the underlying data needs to be standardized and trustworthy.

This project focuses on the infrastructure layer required before higher-level AI workflows, LLM-assisted mapping, automated data reasoning, or analytics pipelines can operate reliably.

## Planned Components

* Python-based file profiling
* CSV and XLSX parsing
* Canonical schema definitions
* Column mapping model
* Execution plan model
* QC issue generation
* Preview artifact writer
* Local storage support
* Cloud storage abstraction
* Unit-testable transformation pipeline

## Possible Future Extensions

* LLM-assisted column mapping suggestions
* Human-in-the-loop approval workflow
* Confidence scoring for mappings
* Schema drift detection
* Data quality dashboards
* Integration with object storage and queue-based processing
* Evaluation framework for mapping accuracy

## Status

Initial portfolio prototype.

This repository is intended to demonstrate system design, data workflow modeling, validation-first engineering, and reliable AI-adjacent data infrastructure patterns.
