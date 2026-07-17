---
name: translate
description: Triggers when the user runs /translate to translate the currently selected Korean text into English and insert it directly below in this vault's notes, highlighted with a dark gray background.
---

# Translate

Translates a Korean passage into English and inserts the translation right below it in the same markdown file, styled with a dark gray-background span so it visually stands out as a translation.

## How to execute

When the user enters `/translate`, follow these instructions:

1. Determine the source text and its location:
   - If the user has an active IDE selection (see the `<ide_selection>` context), use that file path, line range, and selected Korean text.
   - Otherwise, if arguments were passed after `/translate`, translate that text and ask the user which file/location to insert it into if not obvious from conversation context.
2. Read the target file to get exact current content and confirm the selected line(s) verbatim.
3. Translate the selected Korean text into natural, concise English.
4. Using Edit, insert the translation immediately after the original Korean line(s), separated by exactly one blank line, wrapped like this:

   ```
   <원문 한글 텍스트>

   <span style="background-color:#333333; color:#ffffff">번역된 영어 텍스트</span>
   ```

   - Keep the background color `#333333` and text color `#ffffff` so the translation stays readable regardless of the editor's theme.
   - Do not alter the original Korean text or any other part of the file.
   - If the section already has a translation span directly below it, replace that span's text instead of adding a duplicate.
5. Briefly confirm what was translated and where it was inserted.
