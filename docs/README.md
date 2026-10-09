# BalanceBuddy Planning Docs

Plan first, then build. These documents define what we're making before any code is written, and they stay the source of truth once coding starts.

## Reading order

| # | Doc | Status | What it answers |
|---|---|---|---|
| 01 | [Product brief](01-product-brief.md) | Draft 1 | What is this, who's it for, how should it feel, what's in the MVP |
| 02 | [Feature inventory](02-feature-inventory.md) | v2, tiers decided | Everything it could do, tiered MVP / Next / Later / Never |
| 03 | Money-math spec | Not started | Exact formulas, rounding, edge cases, worked examples (these become tests) |
| 04 | Design research & direction | Not started | What makes design comforting; moodboard and style tiles in Paper |
| 05 | Data model & architecture | Not started | Entities, storage, Firebase or not, security rules |
| 06 | Security plan | Not started | Threat model, data handling, safeguards |
| — | [Decision log](decisions.md) | Ongoing | What's been decided and why |
| — | [Spec: import template](specs/import-template.md) | Draft 1 | Spreadsheet upload format, validation, security · [template file](templates/BalanceBuddy-Import-Template.xlsx) |

Later, once 01–05 are solid:
- `CLAUDE.md` at the repo root: rules for AI assistants working in this codebase
- Skills: a **design-system** skill and a **finance-math** skill, so every session builds the same app the same way

Skills already in place:
- [`mirth`](../.claude/skills/mirth/SKILL.md): the delight designer. Use for anything whimsical, celebratory or gamified; it holds the guardrails, psychology and motif library

## Ground rules

1. No feature gets built without a row in the feature inventory marked MVP or Next.
2. No number appears on screen without a rule in the money-math spec.
3. Decisions go in the decision log. AI assistants don't override them without asking.
