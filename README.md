# pop-explainer（梗讲师）

**English** | [中文](README.zh-CN.md)

**Teach any concept with a misconception-reversal story.** An agent skill for Claude Code, Codex and other tools that support the Agent Skills format.

Ask "explain X" and you get one short, complete story: the hero believes the most common wrong idea about X, acts on it, and then *works out* why it's wrong. Then the concept's name, one warning, and a quiz set in a different world — answer withheld until you try.

> **The twist must come from figuring it out, never from a lucky reveal.** No culprit is caught, no result is announced: the turn is a question, a comparison or a count you can follow. You learn the reasoning, not the ending.

## See it in action

**You:** explain survivorship bias like a story

> 🎬 **The Story**
>
> Ming wanted to open a dumpling shop on the old high street. He walked the whole street and noticed that the three shops that had survived for thirty years all cooked over big wood-fired stoves.
>
> "That's the secret!" He spent 20,000 building a wood-fired stove of his own (all numbers made up).
>
> Three months in, customers hadn't increased, but his firewood bill had gone up 2,000 a month.
>
> Old Xu, the cobbler next door, asked him one question: "Thirty years ago, how many dumpling shops were on this street?"
>
> Ming had no idea. Xu counted on his fingers: at least twenty — and every one of them cooked with wood, because nobody had gas back then. One by one they closed, until only these three were left.
>
> "The dozen-plus shops that closed had wood stoves too. You can only see the ones still open, so of course wood looks like the secret."
>
> … Ming took the photo of his stove off the wall. "I copied what every shop had, not what made these ones survive."
>
> 💡 **This is called: Survivorship bias**
> When you only look at the winners still in front of you, you treat what they have in common as the secret of success — but the ones who disappeared may have had the same thing.
>
> ⚠️ **Don't Mix It Up**
> The useful comparison is between the ones that survived and the ones that didn't. Staring only at the survivors can't tell you anything.
>
> 🤔 **Your Turn**
> A friend says: "Look at the seniors who got into top universities — they all slept five hours a night in their final year. If you want to do well, sleep less." What is he missing?
>
> *Tell me what you think and I'll pick it up from there. Want the answer straight away? Reply /answer*

What to notice: Ming acts on the misconception (he spends the money); the twist is a question and a count, not a reveal; the term appears only once, after the story; the quiz moves from shops to exams. Full example: [`examples.en.md`](skills/pop-explainer/references/examples.en.md).

<details>
<summary><b>What happens when you answer the quiz</b></summary>

- **Right:** it names the key point you caught and ties it back: "same idea as the story: you only saw the survivors."
- **Right verdict, wrong reason** (the most common case): it confirms the verdict, then uses a moment from the story to lead you to the real mechanism.
- **Not there yet:** it never says "wrong" — it replays one beat of the story as a hint and lets you try again. After a second miss it gives the answer kindly and moves on.

</details>

### More examples: sociology and philosophy (in Chinese)

- **Self-fulfilling prophecy** (Merton) — someone posts "the ribs will run out today" in the dorm chat; everyone buys extra and the ribs do run out. The turn is two questions and a count (same 300 portions as last week, when they lasted until 1pm; 40-odd extra bought on one floor alone). Overturns "it came true, so the predictor saw it coming". → [`self-fulfilling-prophecy.zh.md`](skills/pop-explainer/examples/self-fulfilling-prophecy.zh.md)
- **Veil of ignorance** (Rawls) — four roommates agree how to split a sweet-potato stall's takings *before* drawing lots for the worst job. The turn is one question: "if I draw the worst job, which split leaves me better off?" Overturns "fair means equal shares", and ⚠️ notes it's a thought experiment whose conclusion is contested. → [`veil-of-ignorance.zh.md`](skills/pop-explainer/examples/veil-of-ignorance.zh.md)

## Output shape

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
