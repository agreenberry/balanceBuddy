# Spec: Spreadsheet Import Template

> Status: **Draft 1** · Oct 8, 2026 · Feature: F5 / F5b in the feature inventory
> Template file: `docs/templates/BalanceBuddy-Import-Template.xlsx` (version 1)
> Revised Oct 8: `Balance Update` (one row per account per date) replaced by `Balances`, a timeline with one column per date, matching how Amanda already works.

## Purpose

The fastest way to get data in: fill a spreadsheet you already know how to use, upload it, review, confirm. It's also the regular "update my balances" flow, replacing Amanda's long-running sheet.

## Workbook structure (v1)

Sheet names and header text are the contract. The importer matches columns **by header text**, not position, so users can reorder or add their own columns (unknown columns are ignored).

| Sheet | One row per | Required columns |
|---|---|---|
| `Accounts` | card or loan | Account nickname, Account type, Standard APR |
| `Promo Balances` | promo-rate *part* of a balance | Account nickname, Promo type, Promo balance ($), Promo APR, Promo end date |
| `Balances` | account (rows) × date (columns) | Account nickname; for each date column: Date, Column type, balances |
| `Start Here` | — | Instructions. Ignored by the importer |
| `Lists` (hidden) | — | Dropdown values. Ignored by the importer |

Full column lists: see the template's header rows. Columns with grey-green headers (`Check`, `Owner` on Balances, the total rows) are spreadsheet helpers, and the importer ignores them.

### The `Balances` timeline
Accounts down column A, one column per date, newest on the right. Adding an update means adding a column, not filling out a form.

| Row | Meaning | Imported? |
|---|---|---|
| 1 · Date | The as-of date for this column | Yes |
| 2 · Column type | `Actual` (balances looked up) or `Planned` (balances after planned payments) | Yes |
| 3 · Payment budget ($) | Money available this round (Planned columns) | Yes, stored with the plan |
| 4 · Total owed | `SUM` of the column | No (helper) |
| 5 · Paid down vs. previous column | Previous total − this total | No (helper) |
| 6 · Left to allocate | Budget − paid down; green within $50 | No (helper) |
| 7 | Headers | — |
| 8+ | One account per row; cells are balances. A blank cell means "not recorded", not zero | Yes |

- **Cell comments are imported** as notes on that balance (e.g. "payment scheduled 10/15", "promo ends Jan"). This replaces the habit of keeping reminders in comments.
- **Planned columns** import as a payment plan: for each account, planned payment = the latest Actual balance − the Planned balance.
- **Negative balances are allowed** (credits/overpayments).
- Two columns may share a date (an Actual and its Planned).

### Key rules
- **Account nickname** is the join key across sheets. It must be unique within the file. Matching is exact after trimming leading/trailing spaces. The app stores its own internal ID; the nickname is only for import matching.
- A **promo balance is part of** the account's current balance, not additional to it. Standard-APR portion = current balance − sum of active promo balances. If promos exceed the balance, that's an import error.
- **Promo types:** Balance transfer · Intro purchase APR · Deferred interest · Other promo.
- **Rows whose nickname is `EXAMPLE` are skipped.**
- **Blank Status = Open.** Blank Owner = Me.

## Import behaviour

1. **Parse in the browser.** The file is read client-side (SheetJS or similar). The raw file is never uploaded or stored; only validated records are saved.
2. **Validate every row** with the same schemas the app uses elsewhere (one source of truth for validation). Collect *all* problems; don't stop at the first.
3. **Preview screen** before anything saves, showing:
   - new accounts / changed accounts (field-by-field diff) / unchanged
   - new promo balances, changed, and expired
   - balance updates per account
   - errors (blocking) and warnings (non-blocking), each pointing to sheet + row
4. **Confirm** saves everything in one transaction: all or nothing.
5. **Idempotent:** uploading the same file twice changes nothing. A balance is keyed by (account, date, column type); a re-upload with a different amount for the same key is shown as a change to confirm.
6. Accounts in the app but missing from the file are **left alone**, never deleted by import.

## Validation

**Errors (block the import):**
- Missing required column or required value
- Duplicate nickname in `Accounts`
- Promo or balance row referencing a nickname that's in neither the file nor the app
- Negative money amounts; APR outside 0–100%; day outside 1–31; unparseable dates
- Promo balances on an account summing to more than its current balance
- File over 1 MB or over 2,000 rows per sheet (sanity limit; plenty for any household)

**Warnings (shown, can proceed):**
- Promo end date in the past (the promo will be marked expired)
- Utilization above 100%
- Balance changed by more than 50% since the last update (typo check)
- Missing optional fields the planner uses (due day, statement closing day)

## Security & privacy

- **Full card numbers are refused.** Any cell (in any column, including user-added ones) containing a run of 13–19 digits, allowing spaces or dashes, causes that value to be **dropped, not stored**, with a warning naming the cell. *Last 4* accepts at most 4 characters.
- **Formulas are never evaluated** by the importer; only cell values are read. Text that begins with `=`, `+`, `-` or `@` is stored as plain text. On export, such values are prefixed with `'` to prevent spreadsheet formula injection.
- Only the known columns are kept. Extra columns are discarded after the card-number scan.
- No data from the file is sent to any third party.

## Export (F5b)

Produces the same workbook format, filled with the user's current data, so download → edit → re-upload round-trips cleanly. The export includes a version number on `Start Here`.

## Versioning

The template carries a version on `Start Here` ("Template version 1"). Future versions may add columns. The importer accepts older versions as long as the required columns are present, and new optional columns are simply absent.

## Open questions
- [ ] Should actual payments made be recorded separately, or is Actual → Planned → next Actual enough history for the MVP?
- [ ] Accept plain CSV too (one file per sheet), or only .xlsx? Leaning .xlsx only for v1: one file, with dropdowns.
- [ ] What did the `*` on some cards mean in the old sheet? It's preserved in the Notes column of the pre-filled file.
