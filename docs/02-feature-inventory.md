# BalanceBuddy — Feature Inventory

> Status: **Draft 1, for you to mark up** · Oct 8, 2026
> This is a catalogue of everything the app *could* do, so you can react instead of invent.
>
> **How to use it:** Each row has my *suggested* tier. Change the **Your call** column to one of:
> - `MVP`: must exist in the first usable version
> - `Next`: soon after the MVP
> - `Later`: someday
> - `Never`: cut it
> - `?`: unsure, discuss
>
> Add rows freely. Cross things out. Nothing here is decided until you mark it.

---

## A. Debts & accounts (the things you owe)

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| A1 | Add/edit credit cards manually | Balance, APR, credit limit, statement closing day, due day | MVP | |
| A2 | Add/edit installment loans manually | Principal, APR, term, payment, start date, origination fee | MVP | |
| A3 | Promo APR periods | 0% or low intro APR with an end date; can stack with a regular APR on the same card | MVP | |
| A4 | Deferred-interest promos (store cards, "no interest if paid in full") | Behaves differently from 0% intro APR: if not paid in full by the deadline, interest is charged back to the purchase date. Big trap; high value to warn about | MVP | |
| A5 | Multiple balances on one card | Purchase vs. balance-transfer vs. promo balances, each with its own APR | Next | |
| A6 | Minimum payment rules | Per-card formula (e.g. 1% + interest, or a flat $ floor); default plus custom | MVP | |
| A7 | Balance-transfer fees | % or flat fee, applied at transfer time | Next | |
| A8 | Loan prepayment rules | Does a prepayment shorten the term or lower the payment? Any prepayment penalty? | MVP | |
| A9 | Variable-rate loans | APR changes over time (manual rate schedule) | Later | |
| A10 | Mortgages | Escrow, PMI, etc. Large scope | Later | |
| A11 | Student loans | Income-driven plans, forgiveness. Very large scope | Later | |
| A12 | Archive paid-off debts | Kept for history and celebration | Next | |

## B. Income & cash flow

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| B1 | Paycheck schedule | Weekly, biweekly, semi-monthly, monthly; amount; next date | MVP | |
| B2 | Multiple income sources | Two jobs, side income | Next | |
| B3 | Irregular/variable income | Ranges or a conservative estimate | Later | |
| B4 | Fixed bills | Rent, utilities, subscriptions, with due dates | MVP | |
| B5 | "Available for debt" per paycheck | Income − bills − buffer = what the plan can use | MVP | |
| B6 | Safety buffer / emergency fund target | The plan never spends below the buffer | MVP | |
| B7 | One-off windfalls | Tax refund, bonus: "what if I put this toward debt?" | Next | |
| B8 | Savings goals alongside debt | Split extra money between saving and paying down | Later | |

## C. The plan (the payoff engine)

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| C1 | Avalanche strategy | Highest APR first; minimizes interest | MVP | |
| C2 | Snowball strategy | Smallest balance first; motivational wins | MVP | |
| C3 | Custom order | Drag debts into your own order | Next | |
| C4 | Promo-deadline awareness | Plan pays off promo/deferred balances before they expire when that's cheaper | MVP | |
| C5 | Dated payment schedule | "On Oct 24 (payday), pay $X to Card A, minimums on the rest" | MVP | |
| C6 | Paycheck-aligned timing | Payments scheduled from the paycheck that lands before each due date | MVP | |
| C7 | Statement-closing optimization | Paying before the statement closes lowers the reported balance and utilization. Show the timing; credit-score impact is informational only | Next | |
| C8 | Debt-free date | Overall and per debt | MVP | |
| C9 | Total interest paid | Under the plan vs. minimums only | MVP | |
| C10 | Months of calm | Payment-free months gained vs. the baseline | MVP | |
| C11 | Re-plan when reality changes | Missed or extra payment, new balance; the plan recalculates from today | MVP | |
| C12 | "Least total cost" optimizer | Search for the cheapest allocation across all debts and dates, beyond fixed strategies | Later | |
| C13 | Payment-allocation realism | Card issuers apply amounts above the minimum to the highest-APR balance first (US rule). Model this for multi-balance cards | Next | |

## D. Scenarios & comparisons

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| D1 | Side-by-side scenario comparison | 2–4 scenarios; columns for monthly payment, payoff date, interest, fees, months of calm | MVP | |
| D2 | Fair-comparison mode | Option to line scenarios up at the same monthly payment, so the true driver of savings is visible | MVP | |
| D3 | "Break-even" answers | E.g. "the 10-year loan wins if its rate is below ~11.5%" | Next | |
| D4 | Trade-off notes | Plain-language callouts: forced vs. flexible, fees, risk in a bad month | MVP | |
| D5 | What-if sliders | Extra $/month, lump sum, rate change | Next | |
| D6 | Refinance / consolidation calculator | New loan pays off old debts: fees, new rate, new term | Next | |
| D7 | Balance-transfer calculator | Transfer fee vs. interest saved during the promo; can you pay it off in time? | Next | |
| D8 | Save and name scenarios | Come back to them later | Next | |

## E. Commitment strategies (make the good choice automatic)

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| E1 | Borrow-larger-and-prepay | Your $80k − $20k move: shows the forced payment, interest, extra origination fee, and rigidity | MVP | |
| E2 | Shorter-term loan comparison | Forced payment via term; shows the rate needed to beat E1 | MVP | |
| E3 | Autopay-above-minimum plan | Recommended autopay amount per debt | Next | |
| E4 | Payday auto-transfer plan | "Move $X to savings/debt the day you're paid" | Next | |
| E5 | Rigidity score / bad-month check | What's the *required* outflow if things go wrong? Can your buffer cover it? | MVP | |
| E6 | Commitment reminders | Gentle nudges tied to paydays (needs notifications) | Later | |

## F. Tracking (the "Mint half")

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| F1 | Manual balance updates | Update balances monthly; history builds over time | MVP | |
| F2 | Progress history | Balances over time; payoff progress | Next | |
| F3 | Bank/card syncing via an aggregator | Plaid / MX / Teller etc. Big cost, compliance and security step | Later | |
| F4 | Transaction list | Imported or CSV upload | Later | |
| F5 | CSV import | Statement/transactions from a bank export; safer than syncing | Next | |
| F6 | Spending categories | Auto + manual | Later | |
| F7 | Budgets | Per-category monthly limits | Later | |
| F8 | Net worth | Assets − debts | Later | |
| F9 | Bill reminders | Due-date notifications | Later | |

## G. Feeling & delight

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| G1 | Hand-drawn milestone moments | A debt paid off "blooms"; new flourishes as progress grows | Next | |
| G2 | Gentle language system | Copy guidelines: no red-alert shaming; truthful but kind | MVP | |
| G3 | Progress garden / visual metaphor | Overall progress as an illustration that fills in | Later | |
| G4 | Quiet mode | Hide totals and show only "this paycheck, do this," for overwhelming days | Next | |
| G5 | Seasonal/flourish variations | Illustration sets that change with seasons | Later | |

## H. Accounts, data & security

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| H1 | Local-only mode (no account) | Data stays in the browser; simplest and safest v0 | ? | |
| H2 | Sign-in (Firebase Auth) | Email link / passkey / Google | ? | |
| H3 | Cloud sync of plan data | Firestore with deny-by-default, tested rules | Next | |
| H4 | Encrypted export/import | Back up your data to a file; restore it | MVP | |
| H5 | Delete my data, fully | One action, actually deletes everything | MVP (once there's cloud data) | |
| H6 | Session timeout / lock | Auto-lock after inactivity | Next | |
| H7 | Audit trail of changes | What changed and when, per debt | Later | |
| H8 | Multi-user / household sharing | Shared plans with permissions | Later | |

## I. Platform

| ID | Feature | Notes | Suggested | Your call |
|---|---|---|---|---|
| I1 | Responsive web app | Desktop first; zoom-safe; reflows down to phone width | MVP | |
| I2 | Installable PWA | Home-screen icon, offline viewing | Later | |
| I3 | Printable plan | A beautiful printed payment schedule for the fridge | Next | |
| I4 | Dark mode | Ornate in candlelight? Needs its own art direction | Later | |
| I5 | Native mobile apps | — | Never (for now) | |

---

## Parking lot

Ideas that came up and don't fit a row yet:

- Credit-score impact estimates. Risky to state as fact; informational only, if ever.
- Tax implications (e.g. student-loan interest deduction). Probably never; not tax advice.
