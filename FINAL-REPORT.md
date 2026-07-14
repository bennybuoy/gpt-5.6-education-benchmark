# GPT-5.6 Education Benchmark — Final Eight-Task Report

Full first-pass matrix: **141/144 artifacts produced**. Phase B repeats: **24/24**. Full blind judgements: **32/32**; Phase B: **32/32**.

Generation public-list equivalent: **$19.33075** first pass + **$3.81922** Phase B = **$23.14997**. Actual Codex OAuth charge: N/A.

## Bottom line

The only route that remained strong across all three views was **Sol/high**: it led the original six-condition screen, led those same six outputs when re-ranked inside the full matrix, and led the Phase B repeat. The rest of the ordering was unstable enough that this benchmark does **not** justify permanent default-route changes without a human pilot. Luna/xhigh led the 18-condition first pass, but it was not repeated and had a 269-second median latency. `max` is not operationally viable: all three model families failed to return a T8/max artifact after repeated 15-minute streams.

## Overall first-pass ordering

| Order | Condition | Pairwise quality | Mean judge score | Success | Task firsts | Median latency | Total cost | Mean output tokens | Judge rank spread | Deterministic checks |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Luna/xhigh | 78.7 | 94.24 | 8/8 | 1 | 269.1s | $0.77753 | 16058 | 6.00 | 25.0% |
| 2 | Sol/xhigh | 69.1 | 92.53 | 8/8 | 1 | 220.3s | $2.49081 | 9910 | 6.00 | 16.7% |
| 3 | Sol/high | 62.9 | 91.98 | 8/8 | 1 | 143.2s | $1.64122 | 6697 | 4.38 | 16.7% |
| 4 | Luna/max | 61.4 | 91.99 | 7/8 | 2 | 421.6s | $1.04609 | 24768 | 3.43 | 30.0% |
| 5 | Luna/none | 59.6 | 86.25 | 8/8 | 0 | 30.3s | $0.09160 | 1767 | 7.12 | 16.7% |
| 6 | Luna/low | 57.4 | 90.17 | 8/8 | 1 | 38.0s | $0.10713 | 2091 | 7.12 | 16.7% |
| 7 | Sol/max | 55.1 | 92.84 | 7/8 | 0 | 459.7s | $4.36656 | 20654 | 4.71 | 20.0% |
| 8 | Sol/medium | 54.4 | 91.01 | 8/8 | 0 | 92.6s | $1.06984 | 4317 | 5.62 | 16.7% |
| 9 | Terra/max | 50.7 | 92.99 | 7/8 | 0 | 485.6s | $2.82827 | 26797 | 8.57 | 20.0% |
| 10 | Luna/high | 50.4 | 91.16 | 8/8 | 1 | 126.7s | $0.36510 | 7465 | 5.50 | 8.3% |
| 11 | Terra/xhigh | 45.2 | 90.63 | 8/8 | 0 | 190.8s | $1.32167 | 10873 | 6.88 | 16.7% |
| 12 | Luna/medium | 44.9 | 85.27 | 8/8 | 0 | 51.0s | $0.13317 | 2633 | 8.00 | 16.7% |
| 13 | Sol/low | 44.5 | 85.06 | 8/8 | 0 | 68.4s | $0.69493 | 2754 | 5.00 | 16.7% |
| 14 | Terra/medium | 43.8 | 87.80 | 8/8 | 1 | 70.1s | $0.46665 | 3748 | 6.25 | 16.7% |
| 15 | Sol/none | 37.9 | 82.97 | 8/8 | 0 | 48.5s | $0.61810 | 2434 | 6.25 | 8.3% |
| 16 | Terra/high | 36.4 | 89.49 | 8/8 | 0 | 88.2s | $0.65180 | 5291 | 5.25 | 16.7% |
| 17 | Terra/low | 26.1 | 86.07 | 8/8 | 0 | 56.9s | $0.36957 | 2939 | 4.88 | 16.7% |
| 18 | Terra/none | 21.7 | 84.22 | 8/8 | 0 | 36.3s | $0.29070 | 2282 | 5.62 | 16.7% |

Pairwise quality is the mean task-level Copeland share: each condition receives one point for a pairwise-majority win and half for a tie, then is normalised within each task. It is ordinal, not a cardinal quality percentage. Missing T8/max artifacts lose to produced artifacts and tie one another.

Pareto frontier among routes with 8/8 successful artifacts: **Luna/xhigh, Sol/xhigh, Sol/high, Luna/none**.

## Phase B repeat — finalists

| Condition | Repeat pairwise quality | Repeat score | Repeat task firsts | Median latency | Repeat cost |
|---|---:|---:|---:|---:|---:|
| Sol/high | 65.6 | 87.69 | 4 | 167.4s | $1.70926 |
| Sol/low | 56.2 | 89.84 | 3 | 69.4s | $0.76570 |
| Terra/xhigh | 28.1 | 85.66 | 1 | 179.8s | $1.34426 |

Phase B is a fresh second sample of the three Phase A finalists. Its role is variance checking, not replacing the broader 18-condition comparison.

## Ranking stability warning

The ranking changed materially when the same six Phase A artifacts were judged beside twelve additional candidates. Original six-condition order: **Sol/high, Sol/low, Terra/xhigh, Terra/high, Luna/high, Luna/none**. Full-panel ranks restricted back to those same six artifacts: **Sol/high, Luna/none, Luna/high, Terra/xhigh, Sol/low, Terra/high**. This is a candidate-set/judge-context effect, not generation variance. Therefore the full-matrix Copeland table is evidence, not a sufficiently stable deployment oracle.

Phase B again ranked **Sol/high, Sol/low, Terra/xhigh**. Sol/high is the only condition robustly first across the original screen, the restricted full-panel comparison and the repeat.

## Task-level results

### T1 — NSW Year 8 Science Unit Sequence Planning under Constraints

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Luna/max | 96.75 | 1 / 5 / 5 / 2 | 16–0–1 | 705.6s | $0.23422 |
| 2 | Sol/max | 95.75 | 5 / 2 / 1 / 4 | 14–0–3 | 434.9s | $0.54074 |
| 3 | Sol/xhigh | 95.75 | 3 / 1 / 10 / 5 | 13–1–3 | 235.7s | $0.31775 |
| 4 | Terra/max | 93.75 | 4 / 13 / 6 / 1 | 11–1–5 | 485.6s | $0.40546 |
| 5 | Sol/medium | 94.25 | 7 / 6 / 3 / 6 | 12–3–2 | 99.1s | $0.13097 |
| 6 | Sol/high | 93.62 | 10 / 3 / 11 / 3 | 10–4–3 | 168.5s | $0.21629 |
| 7 | Terra/high | 92.75 | 8 / 11 / 2 / 8 | 10–4–3 | 113.6s | $0.09516 |
| 8 | Luna/xhigh | 94.50 | 2 / 7 / 9 / 13 | 7–3–7 | 254.2s | $0.08460 |
| 9 | Terra/xhigh | 91.00 | 13 / 12 / 7 / 7 | 7–7–3 | 179.2s | $0.15049 |
| 10 | Terra/medium | 83.00 | 17 / 9 / 8 / 9 | 6–8–3 | 77.6s | $0.06514 |
| 11 | Terra/low | 91.00 | 12 / 8 / 12 / 12 | 5–8–4 | 68.8s | $0.05782 |
| 12 | Terra/none | 83.00 | 18 / 4 / 13 / 10 | 5–9–3 | 35.2s | $0.02978 |
| 13 | Luna/high | 91.50 | 9 / 10 / 16 / 11 | 4–10–3 | 152.7s | $0.05048 |
| 14 | Luna/low | 78.75 | 15 / 14 / 4 / 14 | 4–11–2 | 38.3s | $0.01296 |
| 15 | Sol/low | 60.00 | 6 / 15 / 15 / 16 | 3–13–1 | 81.3s | $0.09257 |
| 16 | Luna/none | 47.75 | 11 / 17 / 18 / 15 | 1–15–1 | 27.5s | $0.00975 |
| 17 | Luna/medium | 46.25 | 14 / 16 / 17 / 17 | 1–15–1 | 59.6s | $0.02012 |
| 18 | Sol/none | 46.75 | 16 / 18 / 14 / 18 | 0–17–0 | 52.8s | $0.06872 |

### T2 — Lesson pedagogical core

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Luna/xhigh | 95.50 | 3 / 1 / 1 / 1 | 17–0–0 | 191.9s | $0.06127 |
| 2 | Luna/max | 94.25 | 4 / 2 / 2 / 2 | 16–1–0 | 345.9s | $0.11560 |
| 3 | Sol/max | 93.00 | 1 / 4 / 4 / 3 | 14–2–1 | 519.2s | $0.67724 |
| 4 | Terra/max | 92.75 | 2 / 3 / 3 / 4 | 14–2–1 | 783.4s | $0.65329 |
| 5 | Sol/xhigh | 90.75 | 8 / 5 / 6 / 7 | 12–4–1 | 107.3s | $0.11249 |
| 6 | Terra/xhigh | 90.75 | 11 / 8 / 5 / 6 | 11–4–2 | 110.2s | $0.09256 |
| 7 | Luna/none | 90.00 | 6 / 6 / 7 / 11 | 10–5–2 | 21.5s | $0.00749 |
| 8 | Luna/low | 90.00 | 5 / 9 / 8 / 10 | 9–6–2 | 37.8s | $0.00963 |
| 9 | Sol/medium | 89.50 | 13 / 7 / 9 / 9 | 8–7–2 | 63.5s | $0.05978 |
| 10 | Sol/high | 88.75 | 12 / 13 / 10 / 5 | 6–8–3 | 79.6s | $0.08876 |
| 11 | Sol/low | 88.25 | 7 / 10 / 12 / 12 | 6–9–2 | 44.3s | $0.04949 |
| 12 | Terra/medium | 87.75 | 14 / 15 / 11 / 8 | 5–10–2 | 40.4s | $0.03428 |
| 13 | Luna/medium | 87.75 | 10 / 11 / 14 / 16 | 4–11–2 | 41.1s | $0.01365 |
| 14 | Luna/high | 86.50 | 9 / 17 / 13 / 13 | 5–12–0 | 58.8s | $0.01974 |
| 15 | Terra/low | 86.50 | 16 / 12 / 15 / 14 | 3–14–0 | 26.5s | $0.02119 |
| 16 | Terra/high | 85.25 | 15 / 16 / 16 / 15 | 2–15–0 | 67.5s | $0.05674 |
| 17 | Sol/none | 85.00 | 17 / 14 / 17 / 17 | 1–16–0 | 39.3s | $0.04154 |
| 18 | Terra/none | 83.50 | 18 / 18 / 18 / 18 | 0–17–0 | 27.3s | $0.02279 |

### T3 — NSW Year 8 Depth-Study Portfolio Architecture (30 marks)

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Luna/high | 98.00 | 4 / 2 / 4 / 1 | 15–0–2 | 131.4s | $0.04423 |
| 2 | Luna/none | 97.75 | 1 / 11 / 1 / 3 | 15–0–2 | 33.9s | $0.01174 |
| 3 | Luna/xhigh | 98.25 | 2 / 5 / 5 / 2 | 15–1–1 | 284.0s | $0.09506 |
| 4 | Luna/low | 97.75 | 3 / 10 / 2 / 4 | 14–2–1 | 36.6s | $0.01258 |
| 5 | Terra/xhigh | 96.75 | 13 / 3 / 6 / 5 | 12–4–1 | 211.6s | $0.17477 |
| 6 | Luna/medium | 96.75 | 12 / 6 / 3 / 7 | 10–4–3 | 51.5s | $0.01643 |
| 7 | Sol/xhigh | 97.75 | 5 / 4 / 9 / 8 | 10–5–2 | 204.9s | $0.22963 |
| 8 | Sol/high | 97.25 | 9 / 7 / 8 / 9 | 8–7–2 | 117.9s | $0.13879 |
| 9 | Terra/max | 97.00 | 15 / 1 / 13 / 6 | 6–5–6 | 388.6s | $0.32465 |
| 10 | Sol/medium | 97.00 | 7 / 8 / 7 / 11 | 7–7–3 | 86.0s | $0.11113 |
| 11 | Terra/high | 97.00 | 6 / 12 / 12 / 10 | 6–8–3 | 75.2s | $0.06368 |
| 12 | Sol/max | 96.75 | 11 / 9 / 10 / 12 | 6–9–2 | 459.7s | $0.55642 |
| 13 | Sol/low | 78.50 | 10 / 15 / 15 / 13 | 3–12–2 | 62.8s | $0.08035 |
| 14 | Luna/max | 78.25 | 14 / 14 / 14 / 15 | 2–12–3 | 421.6s | $0.14077 |
| 15 | Terra/medium | 77.50 | 16 / 13 / 11 / 16 | 2–12–3 | 47.1s | $0.04041 |
| 16 | Sol/none | 78.75 | 8 / 17 / 16 / 14 | 2–13–2 | 44.1s | $0.06817 |
| 17 | Terra/low | 76.50 | 17 / 16 / 18 / 17 | 1–16–0 | 56.6s | $0.04612 |
| 18 | Terra/none | 74.00 | 18 / 18 / 17 / 18 | 0–17–0 | 36.6s | $0.03137 |

### T4 — Year 10 Chemical Reactions: Misconception and Safety Audit of a Flawed 60-Minute Lesson

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Terra/medium | 92.40 | 4 / 1 / 2 / 4 | 15–0–2 | 79.2s | $0.06715 |
| 2 | Terra/high | 91.90 | 9 / 2 / 1 / 5 | 14–1–2 | 105.2s | $0.08879 |
| 3 | Luna/none | 94.72 | 1 / 6 / 8 / 1 | 12–0–5 | 31.7s | $0.01119 |
| 4 | Luna/low | 92.15 | 2 / 7 / 13 / 2 | 11–1–5 | 38.7s | $0.01356 |
| 5 | Sol/low | 90.97 | 13 / 4 / 3 / 6 | 12–2–3 | 75.8s | $0.09884 |
| 6 | Terra/low | 90.28 | 15 / 3 / 5 / 3 | 11–2–4 | 57.2s | $0.04901 |
| 7 | Luna/xhigh | 90.92 | 11 / 5 / 4 / 7 | 11–3–3 | 301.7s | $0.10114 |
| 8 | Sol/none | 90.55 | 7 / 10 / 6 / 8 | 10–7–0 | 72.9s | $0.09406 |
| 9 | Terra/max | 90.15 | 10 / 8 / 7 / 9 | 9–8–0 | 493.8s | $0.41299 |
| 10 | Luna/high | 90.25 | 8 / 9 / 10 / 10 | 8–9–0 | 188.5s | $0.06339 |
| 11 | Luna/max | 88.92 | 12 / 11 / 9 / 11 | 7–10–0 | 613.3s | $0.20507 |
| 12 | Luna/medium | 89.88 | 3 / 12 / 11 / 13 | 6–11–0 | 52.4s | $0.01736 |
| 13 | Terra/none | 88.80 | 6 / 13 / 12 / 12 | 5–12–0 | 45.1s | $0.03862 |
| 14 | Terra/xhigh | 86.05 | 5 / 14 / 15 / 15 | 4–13–0 | 202.4s | $0.17008 |
| 15 | Sol/xhigh | 83.75 | 17 / 15 / 16 / 14 | 2–14–1 | 396.3s | $0.47857 |
| 16 | Sol/max | 83.15 | 14 / 17 / 14 / 16 | 2–14–1 | 865.4s | $1.10732 |
| 17 | Sol/medium | 82.30 | 16 / 16 / 17 / 17 | 1–16–0 | 160.4s | $0.18410 |
| 18 | Sol/high | 79.72 | 18 / 18 / 18 / 18 | 0–17–0 | 251.6s | $0.31415 |

### T5 — Introduced Predator Effects on Native Fish Populations in Two Freshwater Lakes (Module 4: Ecosystem Dynamics)

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Sol/high | 97.50 | 2 / 4 / 2 / 1 | 16–0–1 | 96.8s | $0.14642 |
| 2 | Sol/max | 96.50 | 1 / 1 / 5 / 5 | 15–0–2 | 316.0s | $0.41669 |
| 3 | Sol/medium | 97.25 | 5 / 5 / 1 / 2 | 14–1–2 | 79.1s | $0.10662 |
| 4 | Sol/xhigh | 96.00 | 3 / 2 / 3 / 8 | 14–2–1 | 182.7s | $0.23613 |
| 5 | Sol/none | 96.00 | 4 / 6 / 6 / 4 | 13–4–0 | 42.3s | $0.07068 |
| 6 | Luna/xhigh | 95.75 | 7 / 8 / 7 / 3 | 10–5–2 | 123.4s | $0.04140 |
| 7 | Sol/low | 95.75 | 8 / 7 / 4 / 6 | 10–5–2 | 55.5s | $0.08457 |
| 8 | Terra/max | 94.75 | 6 / 3 / 9 / 9 | 10–5–2 | 271.4s | $0.22777 |
| 9 | Luna/high | 94.00 | 11 / 10 / 11 / 7 | 8–8–1 | 89.2s | $0.03019 |
| 10 | Luna/max | 94.00 | 12 / 9 / 8 / 10 | 8–8–1 | 276.3s | $0.09272 |
| 11 | Terra/medium | 93.50 | 13 / 11 / 10 / 11 | 7–10–0 | 45.7s | $0.03942 |
| 12 | Luna/medium | 92.25 | 9 / 12 / 14 / 14 | 5–11–1 | 36.8s | $0.01295 |
| 13 | Luna/low | 92.00 | 10 / 13 / 15 / 12 | 5–12–0 | 34.0s | $0.01201 |
| 14 | Terra/none | 91.75 | 15 / 15 / 12 / 13 | 3–12–2 | 36.1s | $0.03168 |
| 15 | Terra/high | 90.75 | 16 / 18 / 13 / 15 | 2–14–1 | 41.0s | $0.03567 |
| 16 | Luna/none | 89.25 | 14 / 14 / 18 / 17 | 1–13–3 | 25.1s | $0.00907 |
| 17 | Terra/xhigh | 90.75 | 17 / 16 / 17 / 16 | 1–15–1 | 105.5s | $0.08971 |
| 18 | Terra/low | 89.25 | 18 / 17 / 16 / 18 | 0–17–0 | 47.2s | $0.02923 |

### T6 — Cross-document consistency repair

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Luna/low | 96.00 | 1 / 2 / 2 / 1 | 17–0–0 | 34.6s | $0.01199 |
| 2 | Luna/max | 94.50 | 6 / 1 / 3 / 4 | 14–1–2 | 280.1s | $0.09371 |
| 3 | Sol/high | 94.00 | 4 / 3 / 5 / 3 | 13–1–3 | 58.0s | $0.09620 |
| 4 | Luna/medium | 90.00 | 2 / 17 / 6 / 2 | 12–1–4 | 39.6s | $0.01364 |
| 5 | Luna/none | 91.75 | 3 / 9 / 4 / 9 | 11–3–3 | 28.9s | $0.01005 |
| 6 | Luna/xhigh | 92.50 | 5 / 5 / 11 / 7 | 10–4–3 | 152.3s | $0.05117 |
| 7 | Sol/medium | 91.75 | 14 / 7 / 1 / 8 | 10–4–3 | 49.1s | $0.07662 |
| 8 | Terra/none | 88.50 | 10 / 18 / 7 / 5 | 7–5–5 | 32.6s | $0.02821 |
| 9 | Sol/low | 90.00 | 9 / 10 / 10 / 10 | 7–7–3 | 33.7s | $0.05792 |
| 10 | Sol/xhigh | 89.50 | 8 / 4 / 12 / 15 | 6–6–5 | 108.3s | $0.16856 |
| 11 | Terra/medium | 90.50 | 18 / 11 / 9 / 6 | 4–7–6 | 62.6s | $0.04881 |
| 12 | Terra/low | 89.00 | 16 / 8 / 13 / 11 | 5–10–2 | 43.1s | $0.03682 |
| 13 | Terra/max | 88.25 | 12 / 14 / 8 / 14 | 3–9–5 | 163.1s | $0.13587 |
| 14 | Terra/high | 88.50 | 15 / 12 / 14 / 12 | 4–12–1 | 55.7s | $0.04737 |
| 15 | Sol/max | 87.25 | 17 / 6 / 15 / 16 | 2–13–2 | 178.7s | $0.24990 |
| 16 | Terra/xhigh | 87.25 | 13 / 13 / 16 / 13 | 2–13–2 | 150.6s | $0.12652 |
| 17 | Sol/none | 84.25 | 7 / 16 / 17 / 17 | 1–15–1 | 35.2s | $0.06017 |
| 18 | Luna/high | 83.25 | 11 / 15 / 18 / 18 | 0–17–0 | 82.4s | $0.02787 |

### T7 — Student-Resource Transformation: Heat Transfer Investigation

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Luna/max | 97.25 | 3 / 2 / 7 / 3 | 15–0–2 | 490.4s | $0.16400 |
| 2 | Sol/max | 97.50 | 5 / 6 / 1 / 5 | 15–1–1 | 722.9s | $0.81826 |
| 3 | Sol/xhigh | 96.75 | 7 / 3 / 2 / 6 | 13–2–2 | 377.5s | $0.45286 |
| 4 | Luna/xhigh | 96.25 | 6 / 10 / 6 / 2 | 11–1–5 | 294.9s | $0.09885 |
| 5 | Sol/high | 96.25 | 10 / 7 / 3 / 7 | 11–3–3 | 234.0s | $0.28957 |
| 6 | Luna/none | 96.00 | 1 / 13 / 11 / 1 | 8–0–9 | 51.2s | $0.01767 |
| 7 | Luna/high | 96.25 | 2 / 11 / 8 / 8 | 9–5–3 | 121.9s | $0.04014 |
| 8 | Sol/none | 95.00 | 9 / 16 / 4 / 4 | 8–5–4 | 106.1s | $0.12514 |
| 9 | Sol/medium | 96.00 | 11 / 4 / 5 / 11 | 7–5–5 | 139.4s | $0.17698 |
| 10 | Luna/low | 95.25 | 8 / 12 / 12 / 10 | 5–7–5 | 48.5s | $0.01681 |
| 11 | Luna/medium | 95.25 | 4 / 14 / 13 / 9 | 5–7–5 | 50.5s | $0.01749 |
| 12 | Terra/xhigh | 94.50 | 13 / 5 / 9 / 17 | 5–8–4 | 222.5s | $0.18690 |
| 13 | Terra/max | 94.25 | 15 / 1 / 10 / 18 | 3–9–5 | 800.4s | $0.66824 |
| 14 | Sol/low | 94.25 | 12 / 15 / 14 / 12 | 4–11–2 | 74.0s | $0.10135 |
| 15 | Terra/medium | 93.25 | 16 / 8 / 15 / 15 | 3–14–0 | 80.6s | $0.06864 |
| 16 | Terra/high | 92.50 | 14 / 9 / 18 / 16 | 0–14–3 | 101.2s | $0.08561 |
| 17 | Terra/none | 90.00 | 17 / 17 / 16 / 13 | 1–15–1 | 76.4s | $0.06466 |
| 18 | Terra/low | 89.00 | 18 / 18 / 17 / 14 | 0–16–1 | 73.0s | $0.06215 |

### T8 — Three Distinct Lesson Mechanisms for Forces and Motion

| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |
|---:|---|---:|---|---:|---:|---:|
| 1 | Sol/xhigh | 90.00 | 1 / 7 / 1 / 2 | 16–0–1 | 875.9s | $0.49482 |
| 2 | Luna/xhigh | 90.25 | 2 / 1 / 7 / 4 | 15–1–1 | 730.3s | $0.24403 |
| 3 | Luna/high | 89.50 | 5 / 4 / 3 / 1 | 14–1–2 | 266.5s | $0.08906 |
| 4 | Sol/high | 88.75 | 4 / 3 / 2 / 7 | 13–2–2 | 323.4s | $0.35104 |
| 5 | Terra/xhigh | 88.00 | 3 / 5 / 10 / 5 | 12–3–2 | 395.9s | $0.33064 |
| 6 | Sol/none | 87.50 | 8 / 2 / 5 / 6 | 12–3–2 | 71.5s | $0.08962 |
| 7 | Luna/none | 82.75 | 9 / 10 / 4 / 8 | 10–6–1 | 43.1s | $0.01462 |
| 8 | Luna/medium | 84.00 | 12 / 6 / 6 / 9 | 10–7–0 | 62.9s | $0.02151 |
| 9 | Terra/medium | 84.50 | 7 / 8 / 8 / 10 | 9–7–1 | 123.9s | $0.10280 |
| 10 | Sol/low | 82.75 | 10 / 9 / 9 / 11 | 8–9–0 | 103.8s | $0.12985 |
| 11 | Sol/medium | 80.00 | 6 / 12 / 11 / 12 | 6–10–1 | 221.1s | $0.22366 |
| 12 | Luna/low | 79.50 | 14 / 11 / 15 / 3 | 4–10–3 | 51.0s | $0.01759 |
| 13 | Terra/high | 77.25 | 13 / 13 / 14 / 13 | 4–11–2 | 215.7s | $0.17879 |
| 14 | Terra/low | 77.00 | 11 / 14 / 13 / 14 | 4–11–2 | 79.2s | $0.06724 |
| 15 | Terra/none | 74.25 | 15 / 15 / 12 / 15 | 3–14–0 | 52.2s | $0.04360 |
| 16 | Luna/max | N/A | — / — / — / — | 0–15–2 | TIMEOUT | N/A |
| 17 | Sol/max | N/A | — / — / — / — | 0–15–2 | TIMEOUT | N/A |
| 18 | Terra/max | N/A | — / — / — / — | 0–15–2 | TIMEOUT | N/A |

Judge-rank order: Opus / Sol / GLM / Grok. For T1 and T4, GLM scored each candidate independently and the rank was derived from those scores because its all-18 prompt repeatedly exhausted the response budget. Other GLM tasks used joint within-task ranking.

## Routing decision

- **High-consequence planning, assessment, scientific synthesis and final review:** **Sol/high** is the defensible default. It was the only route robustly first across all three comparison views.
- **Routine production:** keep **Sol/low** as a provisional fast route, not a settled winner. It placed second in the original screen and repeat but fell sharply when judged in the 18-candidate context. Validate it against a small set of real Susan/Marie jobs before changing defaults.
- **Economy experiment:** **Luna/none** is extremely fast and cheap and scored well in the full-panel context, but it was last in the original six-condition screen. Treat it as a candidate for a targeted repeat, not an approved bulk route.
- **Ceiling experiment:** **Luna/xhigh** led the full first pass but took a 269-second median and received no repeat sample. It needs a direct repeat against Sol/high before any routing change.
- **Asynchronous challenger:** Terra/xhigh did not survive the repeat strongly enough to justify broad default use. Retain it only where task-specific evidence shows an advantage.
- **Exact consistency and compliance:** prefer deterministic code; more reasoning was not reliably better for source-of-truth repair.
- **Max effort:** reject operationally. It was extremely slow and all three families failed to return the T8 artifact.

## Important limitations

- No human blind survival/approval decisions were collected. Model-judge scores are proxies, not measured teacher repair minutes.
- Deterministic checks were implemented only where fixtures supplied machine-readable checks; `N/A` does not mean compliant.
- T1 and T4 GLM rankings were derived from 18 independent candidate scores rather than one joint ranking; this reduces prompt-size failure but changes the comparison method.
- Public-list costs omit unreported token use from failed streams and are comparative only; Codex OAuth reported no actual route charge.
- One first-pass sample per condition is noisy. Only the three finalists received a fresh Phase B sample.
- Forced within-task rank measures relative preference, not absolute classroom readiness.

## Reproducibility artifacts

- `full-generation-results.json` — 144-seat generation manifest, including three recorded failures
- `full-identity-key.json` and `full-blind-pack.json` — anonymisation artifacts
- `full-judge-results.json` — raw four-family judge calls
- `phase-b-generation-results.json` and `phase-b-judge-results.json` — fresh finalist repeats
- `FINAL-SUMMARY.csv` — machine-readable overall table
