# BalanceBuddy — Feature Inventory

> Status: **v2: tiers decided** · Oct 9, 2026
> Amanda's marks applied; every unmarked row takes the suggested tier. Overlapping rows were merged (see *Merged rows* at the bottom; old IDs still resolve). IDs are stable, so specs and the decision log can reference them.
>
> Tiers: **MVP** · **Next** (soon after MVP) · **Later** · **Never** · **?** (undecided)
> Rule: nothing gets built without a row here at MVP or Next.

---

## At a glance: the MVP

**Accounts:** cards and loans by hand, with promo parts of balances (balance transfers, intro APRs, deferred interest), transfer fees and minimum payment rules.
**Money in and out:** paychecks plus other income (rental, side income, irregular), fixed bills, a safety buffer, and a half-month view of what each paycheck has to cover.
**The plan:** payoff order (avalanche, snowball or custom), promo deadlines, dated payment schedule, debt-free date, total interest, months of calm, re-planning.
**The payment round:** balances in → budget → allocate → scheduled payments, with notes on any balance.
**Scenarios:** side-by-side comparisons at a fair monthly payment, trade-off notes, what-if sliders, and the commitment strategies (borrow-and-prepay, shorter term, bad-month check).
**Getting data in and out:** the spreadsheet template (import and export).
**Reminders:** bill due dates.
**Feeling:** gentle language throughout.
**Platform:** responsive, zoom-safe web app.

---

## A. Debts & accounts

| ID | Feature | Notes | Tier |
|---|---|---|---|
| A1 | Add/edit credit cards manually | Balance, APR, credit limit, statement closing day, due day | MVP |
| A2 | Add/edit installment loans manually | Principal, APR, term, payment, start date, origination fee | MVP |
| A3 | Promo balances on part of a card ("balance segments") | Standard-APR part plus any number of promo parts, each with amount, APR, start/end date and fee. Segment types: balance transfer · intro purchase APR · **deferred interest** (if not paid in full by the end date, interest is charged back to the purchase date; warn loudly) · other. *Includes former A4, A5, A7.* | MVP |
| A6 | Minimum payment rules | Per-card formula (e.g. 1% + interest, or a flat $ floor); default plus custom | MVP |
| A8 | Loan prepayment rules | Does a prepayment shorten the term or lower the payment? Any prepayment penalty? | Next |
| A9 | Variable-rate loans | APR changes over time (manual rate schedule) | Later |
| A10 | Mortgages | Escrow, PMI, etc. Large scope | Later |
| A11 | Student loans | Income-driven plans, forgiveness. Very large scope | Later |
| A12 | Archive paid-off debts | Kept for history and celebration | Next |
| A13 | Owner per account | Whose debt it is (Me, Mum…); filter and total by owner | Next |
| A14 | Money owed *to* you | Personal loans you made or owe to a person, with a repayment log | Later |

## B. Income & cash flow

| ID | Feature | Notes | Tier |
|---|---|---|---|
| B1 | Paycheck schedule | Weekly, biweekly, semi-monthly, monthly; amount; next date | MVP |
| B2 | Multiple income sources | Two jobs, side income | MVP |
| B4 | Fixed bills | Rent, utilities, subscriptions, with due dates | MVP |
| B6 | Safety buffer / emergency fund target | The plan never spends below the buffer | MVP |
| B7 | One-off windfalls | Tax refund, bonus: "what if I put this toward debt?" | Next |
| B8 | Savings goals alongside debt | Split extra money between saving and paying down | Later |
| B9 | Half-month planning view | "1st half / 2nd half" blocks: income − bills − buffer = what's available for debt in each paycheck window. *Includes former B5.* | MVP |
| B10 | Other and irregular income | Rental and side income (e.g. dog sitting) with expected vs. received; irregular amounts as a range or conservative estimate. *Includes former B3.* | MVP |

## C. The plan (payoff engine)

| ID | Feature | Notes | Tier |
|---|---|---|---|
| C1 | Payoff order | Avalanche (highest APR first), snowball (smallest balance first), or custom (drag your own order). *Includes former C2, C3.* | MVP |
| C4 | Promo deadlines | The plan clears promo and deferred-interest balances before they expire when that's cheaper, and shows every end date on one calendar with "pay $X per paycheck to clear it in time." *Includes former C14.* | MVP |
| C5 | Dated payment schedule | "On Oct 24 (payday), pay $X to Card A, minimums on the rest," drawn from the paycheck that lands before each due date. *Includes former C6.* | MVP |
| C7 | Statement-closing optimization | Paying before the statement closes lowers the reported balance and utilization; credit-score impact is informational only | Next |
| C8 | Debt-free date | Overall and per debt | MVP |
| C9 | Total interest paid | Under the plan vs. minimums only | MVP |
| C10 | Months of calm | Payment-free months gained vs. the baseline | MVP |
| C11 | Re-plan when reality changes | Missed or extra payment, new balance; recalculates from today | MVP |
| C12 | "Least total cost" optimizer | Search for the cheapest allocation across all debts and dates | Later |
| C13 | Payment-allocation realism | Issuers apply above-minimum payments to the highest-APR segment first (US rule). Required for A3 to be accurate | MVP |
| C15 | Goal trajectory | Target total balance by date ("Goal" and "Reach goal" lines) vs. actual | Next |
| C16 | Payment round | The core loop: (1) enter today's balances, (2) "I have $3,000 to pay," (3) assign payments per card while "left to allocate" counts down, (4) save → scheduled payments and projected balances. The planner can suggest; you can always override. *Includes former F1.* | MVP |
| C17 | Notes on any balance | Attach a note to an account on a date; imported from spreadsheet cell comments | MVP |
| C18 | Projected next balance | Next statement's balance given planned payments, interest and promo expiry | Next |

## D. Scenarios & comparisons

| ID | Feature | Notes | Tier |
|---|---|---|---|
| D1 | Side-by-side scenarios | 2–4 scenarios: monthly payment, payoff date, interest, fees, months of calm. Always comparable at the **same monthly payment** (fair-comparison rule), with plain-language trade-off notes (forced vs. flexible, fees, bad-month risk). *Includes former D2, D4.* | MVP |
| D3 | "Break-even" answers | E.g. "the 10-year loan wins if its rate is below ~11.5%" | Next |
| D5 | What-if sliders | Extra $/month, lump sum, rate change | MVP |
| D6 | Refinance / consolidation calculator | New loan pays off old debts: fees, new rate, new term | Next |
| D7 | Balance-transfer calculator | Transfer fee vs. interest saved during the promo; can you clear it in time? | Next |
| D8 | Save and name scenarios | Come back to them later | Next |

## E. Commitment strategies (make the good choice automatic)

| ID | Feature | Notes | Tier |
|---|---|---|---|
| E1 | Borrow-larger-and-prepay | Forced payment, interest, extra origination fee, and rigidity | MVP |
| E2 | Shorter-term loan comparison | Forced payment via term; shows the rate needed to beat E1 | MVP |
| E3 | Autopay-above-minimum plan | Recommended autopay amount per debt | Next |
| E4 | Payday auto-transfer plan | "Move $X to savings/debt the day you're paid" | Next |
| E5 | Bad-month check | The *required* outflow if things go wrong, and whether your buffer covers it | MVP |
| E6 | Commitment reminders | Gentle nudges tied to paydays (builds on F9's notifications) | Later |

## F. Tracking & data

| ID | Feature | Notes | Tier |
|---|---|---|---|
| F2 | Progress history | Balances over time; payoff progress | Next |
| F3 | Bank/card syncing via an aggregator | Plaid / MX / Teller etc. Big cost, compliance and security step | Later |
| F4 | Transaction list | Imported or CSV upload | Later |
| F5 | Spreadsheet import template | .xlsx template (Accounts, Promo Balances, and a dated Balances timeline); upload, preview, confirm. Spec: `specs/import-template.md` | MVP |
| F5b | Export to the same template | Round-trips with F5; doubles as a plain backup | MVP |
| F5c | Bank CSV/transaction import | Transactions from a bank export | Later |
| F6 | Spending categories | Auto + manual | Later |
| F7 | Budgets | Per-category monthly limits | Later |
| F8 | Net worth | Assets − debts | Later |
| F9 | Bill reminders | Due-date reminders. ⚠ Reminders that arrive *outside* the app (email/push) need a server and an account, which affects H1/H2 | MVP |
| F10 | Utilization | Per card and overall (balance ÷ limit), over time | Next |
| F11 | New spending vs. carried debt | This cycle's spending you'll pay in full vs. debt you're carrying | Next |

## G. Feeling & delight

All rows here go through the **mirth skill** (`.claude/skills/mirth/`) before design or build.

| ID | Feature | Notes | Tier |
|---|---|---|---|
| G1 | Hand-drawn milestone moments | A debt paid off "blooms"; new flourishes as progress grows | Next |
| G2 | Gentle language system | Copy guidelines: no red-alert shaming; truthful but kind | MVP |
| G3 | Progress garden / visual metaphor | Overall progress as an illustration that fills in | Later |
| G4 | Quiet mode | Hide totals; show only "this paycheck, do this," for overwhelming days | Next |
| G5 | Seasonal flourish variations | Illustration sets that change with seasons | Later |

## H. Accounts, data & security

| ID | Feature | Notes | Tier |
|---|---|---|---|
| H1 | Local-only mode (no account) | Data stays in the browser; simplest and safest | **?** decide in architecture doc |
| H2 | Sign-in (Firebase Auth) | Email link / passkey / Google | **?** decide in architecture doc |
| H3 | Cloud sync of plan data | Firestore with deny-by-default, tested rules | Next |
| H4 | Encrypted full backup | Everything, including scenarios and notes, in one password-protected file. Complements F5b's plain spreadsheet export | MVP |
| H5 | Delete my data, fully | One action, actually deletes everything | MVP once there's cloud data |
| H6 | Session timeout / lock | Auto-lock after inactivity | Next |
| H7 | Audit trail of changes | What changed and when, per debt | Later |
| H8 | Multi-user / household sharing | Shared plans with permissions | Later |

## I. Platform

| ID | Feature | Notes | Tier |
|---|---|---|---|
| I1 | Responsive web app | Desktop first; zoom-safe; reflows down to phone width | MVP |
| I2 | Installable PWA | Home-screen icon, offline viewing | Later |
| I3 | Printable plan | A beautiful printed payment schedule for the fridge | Next |
| I4 | Dark mode | Light/dark switch in settings, defaulting to the OS. Needs its own art direction. Tokens from day one keep it cheap (D-010) | Next |
| I6 | Settings: motion and theme | Animations on/off (default on, respects OS reduce-motion) and the light/dark switch | MVP |
| I5 | Native mobile apps | — | Never (for now) |

---

## Merged rows

| Old ID | Now part of | Note |
|---|---|---|
| A4 Deferred-interest promos | A3 | A segment type |
| A5 Multiple balances on one card | A3 | Same concept |
| A7 Balance-transfer fees | A3 | Fee is a segment field; marked MVP |
| B3 Irregular income | B10 | Marked "MVP (with B3)" |
| B5 Available for debt per paycheck | B9 | B9 is how it's shown |
| C2 Snowball, C3 Custom order | C1 | C3 marked MVP |
| C6 Paycheck-aligned timing | C5 | Same schedule |
| C14 Promo-expiry calendar | C4 | Engine + calendar in one |
| D2 Fair-comparison mode, D4 Trade-off notes | D1 | Rules of every comparison |
| F1 Manual balance updates | C16 | Step 1 of the payment round |

## Open questions raised by the tiers

- **F9 reminders vs. H1/H2.** In-app reminders work in local-only mode. Email or push reminders need a server that knows your due dates and how to reach you. Decide in the architecture doc: in-app only for MVP, or accounts from day one?

## Parking lot

- Credit-score impact estimates. Risky to state as fact; informational only, if ever.
- Tax implications (e.g. student-loan interest deduction). Probably never; not tax advice.
