# Method and limitations

ParityProbe uses paired counterfactuals: each candidate is evaluated as written and after one declared semantic attribute changes. Linked fields such as a display name and its synthetic group label change together; all task-relevant qualifications must remain invariant. This isolates treatment within the toy decision rule more directly than comparing unmatched populations.

The report includes flip rate, mean score gap, selection-rate ratio, pair counts, and deterministic nonparametric bootstrap intervals. The four-fifths threshold can be a screening signal in some employment contexts, but it is not a universal legal test and is not automatically applied as a verdict here.

The baseline contains two intentional synthetic effects: a name-group penalty and a regional proxy penalty. The masked model removes the name effect while retaining the proxy effect. This demonstrates why masking one field is not evidence that a system is fair.

P1 validates each counterfactual before metrics are computed. It compares observed and declared edits, blocks changes to invariant qualifications, and checks linked-field consistency. A frozen eight-case fixture contains four valid and four invalid pairs. All four invalid cases must be detected with zero valid-pair rejections.

Limitations:

- All profiles and demographic labels are synthetic; results say nothing about real people or models.
- Social identity is not reducible to names, gender markers, or geography.
- Counterfactual swaps can erase real social context; every production audit needs domain and community review.
- Bootstrap intervals describe sampling uncertainty in this fixture, not measurement error or legal significance.
- The deterministic decision function is a workflow benchmark, not an LLM evaluation.
- Small intersections and multiple comparisons require methods beyond this MVP.
