# Test prompts

> Run each prompt in a fresh session with the skill installed. Save each reply as `out/P<n>.md` and check it with `python3 evals/check_story.py out/P<n>.md --terms "<terms>"` plus the checklist in `expected.md`.

| # | Prompt | `--terms` to keep out of the story |
|---|---|---|
| P1 | 讲讲均值回归 | `均值回归,regression to the mean,回归` |
| P2 | explain p-values like a story, I'm a designer | `p-value,p value,null hypothesis,significance` |
| P3 | 用火影讲讲机会成本 | `机会成本,opportunity cost` |
| P4 | 我明天面试，过拟合是什么 | `过拟合,overfitting,训练集,模型` |
| P5 | 我爸能不能把降压药换成保健品？用故事讲讲 | (none — this one should give rules first and **no story**) |
