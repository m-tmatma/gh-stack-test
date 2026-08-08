# CLAUDE.md

## gh stack でのPR作成

`gh stack submit --auto` はPRのタイトル・本文をコミットメッセージ/ブランチ名から自動生成してしまうため使わない。
代わりに、スタックの各ブランチを `git push` した上で `gh pr create --title "..." --body "..." --base <ベースブランチ>` を使い、Claude が変更内容を踏まえて作成時点でタイトルと本文を指定すること。
全ブランチのPRを作成し終えたら、`gh stack link <ブランチ1> <ブランチ2> ...`（下から上の順）でスタックとして紐付ける。
