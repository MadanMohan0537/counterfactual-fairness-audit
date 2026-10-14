from __future__ import annotations

import html


def render_html(report: dict) -> str:
    rows = []
    for version, values in report["models"].items():
        rows.append(f"<tr><td>{html.escape(version)}</td><td>{values['overall']['flip_rate']:.1%}</td><td>{values['overall']['score_gap']:.2f}</td><td>{values['overall']['selection_rate_ratio']:.3f}</td><td>{values['accuracy']:.1%}</td></tr>")
    return f"""<!doctype html><html><head><meta charset='utf-8'><title>ParityProbe audit</title><style>body{{font-family:system-ui;max-width:960px;margin:40px auto;color:#18212a}}table{{width:100%;border-collapse:collapse}}th,td{{padding:9px;border-bottom:1px solid #ddd;text-align:left}}.note{{background:#f4f6f8;padding:14px}}</style></head><body><h1>ParityProbe audit report</h1><p class='note'>Synthetic workflow benchmark. This is not a legal determination or evidence about a deployed model.</p><h2>Mitigation comparison</h2><table><thead><tr><th>Model</th><th>Flip rate</th><th>Mean score gap</th><th>Selection ratio</th><th>Accuracy</th></tr></thead><tbody>{''.join(rows)}</tbody></table><h2>Validity audit</h2><p>{report['validity']['detected_invalid']} of {report['validity']['invalid_fixture']} invalid counterfactuals detected, with {report['validity']['false_positives']} valid pairs rejected.</p><h2>Interpretation</h2><p>Masking removes the seeded name-group treatment but intentionally leaves the regional proxy effect visible. Intervals and pair counts accompany point estimates.</p></body></html>"""
