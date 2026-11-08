# 漫画卡模式（/漫画，/comic）

把**最近一次讲的那个故事**（没讲过就先在心里按主流程想好故事）做成一张 1080×1440 的 HTML 漫画卡：标题、"常见误解 / 其实是"对照、6 格火柴人漫画。用户可以直接截图发社交平台。

## 步骤

1. 读 `assets/comic-template.html`。**只改文件里的 `DATA` 对象**，渲染代码一行都不要动——这样每张卡风格一致，火柴人不会画崩。
2. 把故事压成 6 格：
   - 第 1–2 格：主角信了误解、照着做（可以三翻四抖压缩成两格）；
   - 第 3–4 格：对比 / 提问 / 算账；
   - 第 5 格：转折——想通的那一刻，设 `turn: true`（会加黄色高亮框）；
   - 第 6 格：一句大白话收尾。
3. 填字段：
   - `concept`：概念名；`subtitle`：英文名（没有就留空字符串）；`tag`：学科（"统计学""经济学""社会学"……）。
   - `wrong`：常见误解，一句话，≤ 24 字（英文 ≤ 45 字符）；`right`：其实是，一句话，≤ 40 字（英文 ≤ 80 字符）。
   - 每格 `caption`：旁白，≤ 22 字（英文 ≤ 45 字符），最多两行，超出部分会被裁掉；`characters`：1–2 个人物。
   - 人物字段：`name`（≤ 4 字）、`x`（0–100，两人时一左一右，比如 30 和 70）、`pose`、`face`、可选 `say`（≤ 14 字，英文 ≤ 24 字符，越短越好）、可选 `prop`。
   - 可用的 `pose`：stand / point / think / shock / happy / sad / shrug / facepalm / walk / sit。`face`：neutral / smile / grin / frown / surprised / thinking。`prop`：phone / money / bowl / sign / book / bucket / chart / none。只用这些值，别自造。
   - `footer`：有编造数字时写"故事与数字均为虚构"（英文 "Story and numbers are made up"）；这就是全卡唯一的虚构标注，格子里不用再标。
   - 道具会画在"没放在头上的那只手"上；举着道具或双手举高时，气泡会自动让到上方。一格里最好只有一个人说话。
   - `subtitle`：概念的另一种语言名称（中文卡写英文名，英文卡可以留空）。
4. 另存为当前工作目录下的 `<概念名>-comic.html`（英文名用小写加连字符，如 `regression-to-the-mean-comic.html`），不要覆盖模板。
5. **如果你能运行命令**，渲染成 PNG 并自己看一眼（文字有没有溢出、气泡有没有挡住脸）：
   ```bash
   "<Chrome 或 Chromium 路径>" --headless=new --hide-scrollbars --window-size=1080,1440 \
     --screenshot=<概念名>-comic.png "file://<HTML 的绝对路径>"
   ```
   macOS 上 Chrome 通常在 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`。有溢出就缩短文字重新渲染。不能运行命令时，只给 HTML，并告诉用户用浏览器打开后截图。
6. 回复里给出文件路径，加一句"这一格是转折"的说明，不再重复整个故事。

## 规则

- 准确性规则不变：误解和正解要和 `accuracy-pitfalls.md` 一致；故事里不出现术语（标题和对照框除外）。
- 文字一律短：漫画是给人扫一眼的，任何一格的旁白或对白超过限制就改写，不要缩小字号硬塞。
- 不画真实人物，不用真实作品的角色名。
- 英文用户：所有文字换成英文，`tag` 用 "Statistics" 等，并在 `DATA` 里加 `labels: { wrong: "✗ Common myth", right: "✓ Actually", brand: "pop-explainer" }`。
