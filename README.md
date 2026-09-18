# Claim Short-Pay Flagger

The best product in claims is not another adjuster dashboard. It is the thing that shows the short-pay before the shop or the homeowner closes the file.

Three surfaces, one failure mode: Texas SB 458 added binding appraisal for amount-of-loss disputes on policies renewing into 2026. Washington's WAC 284-30-390 tightened minimum claims-handling duties. Vertical agents got cheap. Nobody owns the photo set or the estimate map, so nobody demands the appraisal or the supplement in time.

## How it works

1. Upload the carrier estimate PDF — or the set of damage photos taken the same day.
2. Thirty seconds later: missing line items, density patterns that usually support higher repair hours, scale problems virtual adjusters systematically under-count, and the specific points that justify an appraisal demand or supplement under the new state rules.
3. The product keeps the map: which carriers short-pay which procedures in which ZIPs, and which photo sets correlate with successful appraisal outcomes. That dataset is the moat — not another dashboard.

## The gate

Appraisal demands, supplements, and formal disputes are irreversible steps. The model drafts the demand letter, the photo index, and the line-item comparison. A named human owns the send.

## Quickstart

```bash
pip install -r requirements.txt
python src/checker.py --estimate path/to/estimate.pdf
```

## Build order

Pick one surface — collision or residential storm. Free photo/estimate upload → numbered flags, each with the specific statutory hook that makes the flag matter. Keep every outcome. After a few hundred files the checklist stops being generic and starts being local.

---

Part of the [idea-mill series](https://tygartmedia.com/the-best-claim-product-flags-the-short-pay-before-the-job-closes/). MIT licensed.
