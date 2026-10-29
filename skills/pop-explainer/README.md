# pop-explainer（梗讲师）

**Teach with a misconception-reversal story.** Ask about any concept and get one short, complete story in which the main character believes the most common wrong idea, acts on it, and then *works out* why it's wrong — followed by the concept's name, one warning, and a quiz set in a different world.

## Headline principle

> **The twist must come from figuring it out, never from a lucky reveal.**

Most "explain like I'm five" prompts end with the answer handed over. Here the turn is always a question, a comparison or a count the reader can follow — no culprit is caught, no result is announced. Readers learn the reasoning, not the ending.

## Output shape

```
🎬 Story            300–500 Chinese characters (≈200–400 English words), no jargon
💡 This is called   the name, once, tied back to the story
⚠️ Don't mix it up  the one thing most likely to mislead
📌 One-liner        only when you mention an interview, exam, thesis or report
🤔 Your turn        a short quiz in a different setting — answer withheld
```

Follow-ups: `/答案` `/answer` · `/深挖` `/deeper` · `/换故事` `/retell` · `/更简单` `/simpler` · `/考我` `/quiz` · `/漫画` `/comic` · `/对比` `/compare`. Plain-language follow-ups ("still don't get it", "quiz me") work too.

## Example

A complete English output is in `references/examples.en.md` (survivorship bias: a would-be shop owner copies the wood-fired stoves of three surviving shops — until a neighbour counts how many shops with wood stoves closed). The same example in Chinese: `examples/golden-survivorship.zh.md`.

## Why this format

The structure follows well-established findings from learning research. Look these up by name; the skill itself never cites them to users:

- **Structure-mapping in analogy** (Gentner and colleagues): good analogies map *relations*, not surface features.
- **Refutation / misconception-first instruction**: stating and then overturning a common misconception tends to produce more durable learning than a clean explanation alone.
- **Concreteness fading**: concrete scene first, formal name last.
- **Comparing cases**: a second, different example helps people extract the shared structure.
- **Retrieval practice** (e.g. Roediger & Karpicke): trying to recall or apply before seeing the answer beats rereading.

## Accuracy guardrails

`references/accuracy-pitfalls.md` lists the right core idea and the common wrong versions for 30+ frequently mangled concepts (p-values, confidence intervals, regression to the mean, Simpson's paradox, entropy, overfitting…). The story must land on the right core; the self-check asks whether the story's turning reason would hold up in a textbook.

## Language

The instructions (`SKILL.md`) are written in Chinese; the skill answers in whatever language you write in, with headings and closing line translated.

## When to use something else

- "Is this paper worth reading?" → `paper-triage`
- "What does this paper's Methods actually identify?" → `methods-decomposer`

Both live in [scholar-screen-skills](https://github.com/liuxiaoyuu/scholar-screen-skills).
- A personal medical, legal or investment decision → it gives the general rules and when to see a professional first, and only offers a story afterwards.
