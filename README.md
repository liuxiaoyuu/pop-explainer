# pop-explainer（梗讲师）

**Teach any concept with a misconception-reversal story.** An agent skill for Claude Code, Codex and other tools that support the Agent Skills format.

Ask "explain X" and you get one short, complete story: the hero believes the most common wrong idea about X, acts on it, and then *works out* why it's wrong. Then the concept's name, one warning, and a quiz set in a different world — answer withheld until you try.

> **The twist must come from figuring it out, never from a lucky reveal.** No culprit is caught, no result is announced: the turn is a question, a comparison or a count you can follow. You learn the reasoning, not the ending.

```
🎬 Story            300–500 Chinese characters (≈200–400 English words), no jargon
💡 This is called   the name, once, tied back to the story
⚠️ Don't mix it up  the one thing most likely to mislead
📌 One-liner        only when you mention an interview, exam, thesis or report
🤔 Your turn        a quiz in a different setting — answer withheld
```

Follow-ups: `/answer` `/deeper` `/retell` `/simpler` `/quiz` `/comic` `/compare` (Chinese: `/答案` `/深挖` `/换故事` `/更简单` `/考我` `/漫画` `/对比`), or just say "still don't get it" / "quiz me".

## Install

```bash
git clone https://github.com/liuxiaoyuu/pop-explainer.git
cp -R pop-explainer/skills/pop-explainer ~/.claude/skills/   # Claude Code
cp -R pop-explainer/skills/pop-explainer ~/.codex/skills/    # Codex
```

Other tools that support Agent Skills: copy `skills/pop-explainer/` into that tool's skills directory (check its docs). With the open-source `skills` CLI: `npx skills add liuxiaoyuu/pop-explainer`. Start a new session afterwards.

## Example

A full English answer (survivorship bias: a would-be shop owner copies the wood-fired stoves of three surviving shops, until a neighbour counts how many shops with wood stoves closed) is in `skills/pop-explainer/references/examples.en.md`; the Chinese original is `skills/pop-explainer/examples/golden-survivorship.zh.md`.

More on the design, the learning research behind it, and the accuracy guardrails: [`skills/pop-explainer/README.md`](skills/pop-explainer/README.md).

## Test it

`evals/prompts.md` lists five prompts (including one that must *not* get a story — a personal medication question). `evals/expected.md` says what a good answer must do; `evals/check_story.py` checks the structure:

```bash
python3 evals/check_story.py out/P2.md --terms "p-value,null hypothesis,significance"
```

## Languages

The instructions are written in Chinese; the skill answers in whatever language you write in.

## Companion skills

Reading research papers? See [**scholar-screen-skills**](https://github.com/liuxiaoyuu/scholar-screen-skills): `paper-triage` (is this paper worth reading?) and `methods-decomposer` (what does this paper's design actually identify?). pop-explainer works on its own; it just points you there when your question is about a specific paper.

## License

MIT — see `LICENSE`. Citation: `CITATION.cff`. Provenance: `PROVENANCE.md`.
