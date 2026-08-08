# CLAUDE.md

## gh stack でのPR作成

`gh stack submit --auto` はPRのタイトル・本文をコミットメッセージ/ブランチ名から自動生成するが、この内容は使わない。
PR作成後、Claude が変更内容を踏まえてタイトルと本文を作成し、`gh pr edit <番号> --title "..." --body "..."` で上書きすること。
