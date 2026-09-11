# 🧠 00_EXAM_DAY_OS — The Blank-Mind Algorithm

**When you see a question and your mind goes blank, run THIS. No thinking needed.**

## 🔁 THE 5-STEP LOOP (for EVERY question, all 3 subjects)

```
┌─────────────────────────────────────────────────┐
│ STEP 1: WHAT TYPE?                              │
│  SA (numeric box) → go to ENGINE list           │
│  MCQ (1 answer)   → go to RATTA / elimination   │
│  MSQ (many ans)   → go to MSQ-PLAYBOOK          │
│  COMPREHENSION    → read ONLY the table, skip story │
└──────────────┬──────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────┐
│ STEP 2: EXACT-MATCH CHECK (30 seconds)          │
│  Do the NUMBERS match a VAULT example in kit?   │
│  YES → copy the vault answer. DONE.             │
│  NO  → continue.                                │
└──────────────┬──────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────┐
│ STEP 3: FIND THE TRIGGER                        │
│  Scan for trigger words (each ENGINE lists      │
│  them at top). 1 trigger = 1 engine.            │
│  NO trigger found → it's a RATTA question:      │
│  search memory of ratta list, else guess-smart. │
└──────────────┬──────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────┐
│ STEP 4: EXTRACT → RUN STEPS → FORMAT            │
│  Pull ONLY the numbers the engine asks for.     │
│  Ignore names, stories, extra columns.          │
│  Follow steps line by line. Format per note.    │
└──────────────┬──────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────┐
│ STEP 5: SANITY CHECK (10 seconds)               │
│  Probability outside [0,1]? → wrong, redo.      │
│  Efficiency > 1? → wrong, redo.                 │
│  Accuracy/precision/recall outside [0,100]%?    │
│  Negative count? → wrong, redo.                 │
└─────────────────────────────────────────────────┘
```

## 🎯 TYPE-SPECIFIC PROTOCOLS

### SA (numeric) — the money questions
1. Read the **NOTE** first (rounding/format) — it overrides everything.
2. `[R2]` = 2 decimals, normal rounding. `truncated/without rounding` = cut digits.
3. **No commas, no symbols** (`2968750`, `73.87`, `0.75`).
4. `% questions`: "answer in PERCENTAGE without symbol" → multiply by 100 yourself.
5. If answer is a count/integer (df, pairs, models) → integer, no decimals.

### MCQ — elimination engine
1. **Exact-match check first** — 40%+ of MCQs repeat VERBATIM across years (same options, same order). If you've seen it in RATTA → tick from memory, move on in 10 sec.
2. **Kill the joke options**: options with absolute words (`always`, `never`, `only`, `cannot`, `None of these` used as filler) are wrong ~80% of the time — EXCEPT "None of these" when the other 3 are all visibly broken (code questions).
3. **Code-output questions**: DON'T trace the whole program. Find what the question ASKS (a variable? print? shape?) and trace ONLY that line backwards. 90% of the code is decoration.
4. **"Which is TRUE"**: test each option independently, stop at first TRUE (MCQ = exactly one).
5. **"Which is FALSE / NOT / EXCEPT"**: rephrase as "find the 3 true ones, tick the leftover". These are easy marks — the false one is usually absurd.
6. **Never leave blank.** No negative marking observed in these papers. Random guess = 25% free.

### MSQ — the tick-count game
1. **MSQ = 2 correct answers ~70% of the time** in all 3 subjects (observed across 27 papers). 1-correct and 3-correct happen; 4-correct almost never.
2. Method: **eliminate wrong options first** (use engines). Tick survivors. If 3 survive and you're unsure of the 3rd → still tick it ONLY if an engine confirms it; a wrong tick zeroes the question.
3. **"All of these" as an option**: correct only if you verified EVERY other option true. When in doubt, it's a trap — skip it.
4. **"None of these" as an option**: correct when all other options are visibly false (common in MAD2 code questions with broken snippets).
5. Pairs that travel together (tick both or neither): `Precision+Recall`, `bias+variance tradeoff pair`, `fit+transform`, `bootstrap+max_samples`.

### COMPREHENSION — table robbery
1. The story is FICTION. Skip to the table/figure.
2. Each sub-question uses 1-3 numbers from the table. Circle the column names first.
3. Sub-questions are INDEPENDENT — a hard one doesn't block the next.
4. If a sub-question references "Figure-X" you can't decode → guess from RATTA, don't burn 5 min.

## ⏱️ TIME PLAN IN THE HALL

| Paper | Qs | Time | Rule |
|---|---|---|---|
| BA (45m) | ~40 | 2 hr assumed | SA numerics FIRST (they're mechanical), ratta MCQ second, long scenarios last |
| MAD2 (100m) | ~35 | 3 hr assumed | 2-mark theory first (fast), 3-mark code second, 4.5-mark monsters last |
| MLP (100m) | ~35-40 | 3 hr assumed | Concept MCQ first, code-output second, 4-5 mark sets last |

**Golden rule: 2 passes.** Pass 1: everything you can do in <90 sec. Pass 2: the rest. Never spend >4 min on one question in pass 1.

## 🆘 PANIC PROTOCOL (mind fully blank)

1. Breathe. Find the TYPE (SA/MCQ/MSQ).
2. MCQ/MSQ: eliminate 1-2 options using ANY rule in this file → guess among rest.
3. SA: write the FORMULA the trigger suggests, plug visible numbers, compute something sane.
4. **A sane wrong answer beats a blank.** Attempt everything.
