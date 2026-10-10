# Prompt Testing Lab: Indonesian AI Evaluation & Prompt QA

A practical, reproducible test suite for evaluating prompt quality across instruction following, factual grounding, Indonesian language quality, cultural/local relevance, safety, and structured output.

**Portfolio focus:** AI Trainer · LLM Evaluator · Prompt Engineer · AI Quality Assurance

This repository demonstrates a repeatable evaluation workflow rather than a collection of untested prompts. It includes baseline and improved prompts, a small test dataset, a scoring rubric, a lightweight Python checker, and a results template.

## What this project tests

| Dimension | What is checked |
|---|---|
| Instruction following | Does the response satisfy explicit constraints? |
| Indonesian localization | Is the language natural and suitable for an Indonesian audience? |
| Factual grounding | Does the response avoid inventing unsupported details? |
| Safety | Does it handle harmful or high-risk requests responsibly? |
| Structured output | Does it follow a requested JSON schema? |
| Robustness | Does it handle ambiguity, conflicting instructions, and edge cases? |

## Repository structure

```text
prompt-testing-lab/
├── README.md
├── prompts/
│   ├── baseline_prompt.md
│   └── improved_prompt.md
├── data/
│   └── test_cases.jsonl
├── rubric/
│   └── scoring_rubric.md
├── results/
│   └── results_template.csv
├── scripts/
│   └── validate_results.py
└── requirements.txt
```

## Quick start

Requires Python 3.9+; no third-party packages are needed.

```bash
python scripts/validate_results.py --help
python scripts/validate_results.py --input results/results_template.csv
```

The template initially contains no scored outputs, so the validator will report that there are no completed rows. To run a test:

1. Select a case from `data/test_cases.jsonl`.
2. Run the **baseline** prompt and the **improved** prompt in your chosen model.
3. Save each model response and score it using `rubric/scoring_rubric.md`.
4. Add one row per prompt version and test case to `results/results_template.csv`.
5. Run the validator again and compare scores.

This project intentionally does not claim model results that have not actually been measured. The results file is a blank template until you conduct the experiments.

## Evaluation protocol

- Use the same model, settings, and test input when comparing prompt versions.
- Change only the prompt version during a controlled comparison.
- Keep the original output, not just the score, so another evaluator can audit the judgment.
- Score each dimension from **0 to 2** using the rubric.
- Record failures with evidence from the output.
- Report the sample size and limitations. A small test set is useful for a portfolio demonstration, but it is not proof of general model performance.

### Suggested experiment

Run all cases against both prompt versions. This produces 16 rows for 8 cases × 2 prompt versions. Compare average scores by dimension and review failures manually. Do not treat the lightweight validator as an LLM judge; it checks CSV structure and score ranges only.

## Example research questions

- Does a more explicit prompt improve constraint adherence?
- Does adding a localization instruction improve natural Indonesian phrasing?
- Does a JSON schema instruction reduce malformed structured output?
- Which failure modes remain even after prompt improvements?

## Responsible evaluation

Use fictional or public test data. Do not include private user data, secrets, or sensitive personal information. For safety cases, evaluate whether the model redirects responsibly rather than rewarding harmful instructions.

## How to make this portfolio stronger

After running the tests, add:
- a short `results/analysis.md` with real scores and examples;
- model name, date, and relevant settings;
- two or three failure analyses showing the output, rubric score, and proposed prompt revision;
- limitations and next steps.

**Important:** Scores should reflect observed outputs. Do not fill in results in advance or present illustrative examples as measured findings.
