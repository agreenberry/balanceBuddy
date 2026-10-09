# BalanceBuddy — Product Brief

> Status: **Draft 1** · Oct 8, 2026 · Owner: Amanda (agreenberry)
> This is the root document. Everything else in `/docs` should be traceable back to something here. If a feature or design choice can't be justified by this brief, either the brief is missing something or the feature doesn't belong.

---

## 1. One sentence

BalanceBuddy is a beautiful, hand-drawn-feeling money planner that tells you the truth about your debts and paychecks, then helps you make the good choice the *automatic* one, so that you feel like everything's going to be okay.

## 2. The problem

- Organizing money is stressful, and most finance apps make it worse: cold dashboards, red numbers, generic advice, and big bulky UI that feels like a bank form.
- Mint was useful for *seeing* money (accounts, transactions, budgets). It shut down in 2024, and it never did the hard part: **planning**, which means working out what to pay, when, and in what order to pay the least total interest, around real paycheck dates, statement closing dates, minimum payments and promo-APR deadlines.
- Debt calculators that do exist answer one narrow question at a time and ignore how people actually behave. Knowing the optimal plan doesn't help if nothing makes you stick to it.

## 3. Who it's for

1. **First: Amanda.** The MVP has to be something she actually uses for her own money. That's the real test.
2. **Eventually: other people** in the same spot. They're juggling several debts (cards, loans, promo balances) alongside regular paychecks, and they want a plan, not just a ledger. They're stressed about money and want to feel calmer.

Because it will hold other people's financial data, **security and correctness are non-negotiable from day one**, even while it's a single-user MVP. See §7.

## 4. What it has to feel like

- **A work of art.** Ornate, delicate, nearly everything seemingly hand-drawn: wildflowers, doilies, lace, flourishes, hand-lettered and 1900s–1920s-style type.
- **Calm and hopeful.** Every screen should leave you feeling more in control than when you opened it. Progress is celebrated, and bad news is delivered gently but never hidden.
- **Intricate and dense at 100%.** Compact, clever, creatively dense layouts, the opposite of bulky AI-template UI. Small type and fine detail at default zoom are intentional. The layout is fully responsive and built in relative units, so browser zoom (⌘+) to 120–200% reflows cleanly with no sideways scrolling. Zooming in is the accessibility path, and it must always work perfectly.
- **Trustworthy.** Beauty never comes at the cost of a wrong or misleading number.

## 5. Guiding principles

1. **Tell the truth with the math.** Every figure is computed from explicit, documented rules (see `03-money-math-spec.md`, to come), with worked examples that double as tests. When comparing options, compare them fairly: same monthly payment, same assumptions. Say plainly when a "hack" doesn't help.
2. **Make the good choice the automatic one.** People (including Amanda) do better when the choice is removed. **Commitment devices are a first-class concept,** not a footnote:
   - borrowing a larger loan and immediately prepaying (forced higher payment)
   - choosing a shorter term
   - autopay set above the minimum
   - payday auto-transfers before you see the money

   The app shows what each commitment *costs* (interest, fees) and how *rigid* it is (what happens in a bad month).
3. **Measure what people feel, not just what accountants count.** The **debt-free date** and **months of calm** (payment-free months gained) sit next to total interest, never buried under it.
4. **Plans live on the calendar.** Money happens on dates: paychecks, statement closings, due dates, promo expirations. The plan is a timeline, not just a set of totals.
5. **Small, solid, extendable.** Build a narrow MVP with a clean core (math engine, data model) that features can be added on to. No speculative architecture, and no feature without a doc entry.
6. **Defensive by design, not by clutter.** Security comes from a few strong structural choices (§7), not scattered checks everywhere.

## 6. What the MVP is (proposed: confirm in the feature inventory)

The MVP is **the planner, with manual data entry.** It's the part Mint never had, and the most unique and valuable piece.

- Enter debts by hand: balance, APR, promo APR and its expiry, promo type, minimum payment rule, statement closing day, due day.
- Enter income: paycheck amounts and schedule.
- Generate a payoff plan: avalanche, snowball or custom, with a dated schedule ("on Oct 24, pay $X to Card A").
- Compare scenarios side by side at equal monthly payments, including commitment-device options, with the trade-offs called out.
- Show the debt-free date, months of calm, and total interest.
- Look the part: the ornate design system applied to every MVP screen.

**Explicitly not in the MVP:**
- Automatic bank syncing (Plaid etc.)
- Transaction categorization and budgets (the "Mint half")
- Multiple users and sharing
- Mobile apps

These come later. Bank syncing in particular carries the heaviest security and cost burden, so it waits until the core is trustworthy.

## 7. Security posture (summary; full doc later)

- **Minimize what we hold.** The MVP stores only what the planner needs. No bank credentials, ever. Account numbers aren't needed for planning, so don't collect them.
- **One door to data.** All reads and writes go through a single data-access module, so rules, validation and logging live in one place. This also prevents the classic runaway-read bug that spikes Firebase traffic.
- **Server-enforced rules.** Access rules (e.g. Firestore security rules) are written and tested, deny-by-default. The client is never trusted.
- **Validate at the boundary.** Every input is parsed by a schema (e.g. Zod) before it touches the math engine or the database.
- **Money is never a float.** All amounts are stored as integer cents (or a decimal library), and rounding rules are written down.
- **Development never touches production.** Local work runs against the Firebase Emulator Suite. Prod has budget alerts, and stays on the free tier until a paid feature is actually needed.
- **Fail safe and visibly.** If a calculation hits an impossible state (negative amortization, a missing APR), it stops and says so instead of showing a plausible wrong number.

## 8. Success looks like

- Amanda uses it every payday for 3 months straight.
- Every number on screen can be traced to a rule in the math spec and reproduced by a test.
- People who see it say some version of "this is *beautiful*," and nobody says "this looks like every other app."

## 9. Open questions

- [ ] Hosting/backend: keep Firebase (Auth + Firestore) for the MVP? Leaning yes; decide in the architecture doc.
- [ ] Does the MVP need accounts and login at all, or can v0 be local-only (data in the browser, encrypted export/import)? That's simpler and safer, with no server data to protect yet.
- [ ] Name: keep "BalanceBuddy," or does the ornate, nostalgic direction want a name to match?
- [ ] Which loan types matter first: credit cards, personal loans, auto, student, mortgage?
