# Decision Log

> Every meaningful decision goes here: what we decided, why, and what would change it. Newest at the top.
> **Rule for AI assistants:** don't contradict a decision in this log. If something here seems wrong, raise it and ask before acting on a different choice.

---

### D-008 · Oct 8, 2026 · Spreadsheet template is an MVP data-entry path
**Decision:** The MVP includes a downloadable .xlsx import template (Accounts, Promo Balances, and a Balances timeline with one column per date) and a matching export. Files are parsed in the browser and previewed before saving. Full card numbers are refused. See `specs/import-template.md`.
**Why:** Amanda has managed her money in a spreadsheet for years. Uploading a filled template is faster than form entry for 30+ accounts, and it keeps a familiar workflow.

### D-007 · Oct 8, 2026 · Promo rates apply to part of a balance (segments) in the MVP
**Decision:** A card's balance is modeled as segments: a standard-APR portion plus any number of promo portions, each with its own amount, APR, type and end date. Payment allocation follows the US rule (above-minimum payments go to the highest-APR segment first).
**Why:** Balance transfers and partial promos are central to how Amanda manages debt. A single APR per card would produce wrong interest numbers.

### D-006 · Oct 8, 2026 · Security: structural, not scattered
**Decision:** Security comes from a few strong structural choices: minimal data held, one data-access module, server-enforced deny-by-default rules, schema validation at boundaries, integer-cent money, emulator-only development, fail-safe calculations.
**Why:** The app will hold other people's financial data eventually. Scattered checks clutter the code and still miss things; structure is easier to verify.

### D-005 · Oct 8, 2026 · MVP = the planner, with manual entry
**Decision (proposed, confirm via feature inventory):** The MVP is the payoff planner with manually entered debts and income. Bank syncing and Mint-style tracking come later.
**Why:** The planner is the unique, high-value part. Bank syncing carries the largest security, compliance and cost burden and should wait until the core is trustworthy.

### D-004 · Oct 8, 2026 · "Months of calm" and debt-free date are headline metrics
**Decision:** Every plan and scenario shows the debt-free date and months of calm (payment-free months gained) with the same prominence as total interest.
**Why:** Five fewer months of payments is something people feel. Total interest alone undersells it.

### D-003 · Oct 8, 2026 · Commitment devices are a first-class feature
**Decision:** The app models commitment strategies (borrow-larger-and-prepay, shorter terms, autopay above minimum, payday transfers) and shows each one's cost *and* rigidity.
**Why:** People pay more reliably when the choice is removed. Example: $80k at 12% over 20 years, prepaying $20k immediately, forces an $881/month payment and costs $41,188 in interest over 9y 7m. That beats a 10-year $60k loan at the same rate ($861/mo, ~$43,300, 10y), unless the shorter loan gets a rate below roughly 11.5% or the extra origination fee exceeds ~$2,100.
**Fair-comparison rule:** Scenarios are always comparable at equal monthly payments, so the true driver of savings is visible.

### D-002 · Oct 8, 2026 · Dense and delicate at 100%; zoom is the accessibility path
**Decision:** Default scale is intentionally compact and intricate, deliberately the opposite of bulky template UI. All sizing uses relative units, and layouts must reflow cleanly at 120–200% browser zoom with no horizontal scrolling.
**Why:** The design is meant to be a work of art. People who need larger text can zoom, and the build guarantees zoom works perfectly.
**Not up for re-litigation by AI assistants:** don't "fix" small type or tight spacing unless asked.

### D-001 · Oct 8, 2026 · Start over from a clean scaffold; keep Firebase as an option
**Decision:** Rebuild from the current GitHub `main` (a fresh Vite + React + TypeScript template). The earlier local code isn't carried over by default. Firebase stays the likely backend, but development runs against the Emulator Suite, and production stays on the free Spark plan until a paid feature is needed.
**Why:** The previous build accumulated unplanned AI-suggested code. Keeping Firebase is cheap; the traffic-spike risk comes from runaway reads, which are prevented by the one-data-door rule (D-006) and emulator-only development.
