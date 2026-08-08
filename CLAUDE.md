# CLAUDE.md

## gh stack でのPR作成

`gh stack submit --auto` はPRのタイトル・本文をコミットメッセージ/ブランチ名から自動生成してしまうため使わない。
代わりに、スタックの各ブランチを `git push` した上で `gh pr create --title "..." --body "..." --base <ベースブランチ>` を使い、Claude が変更内容を踏まえて作成時点でタイトルと本文を指定すること。
全ブランチのPRを作成し終えたら、`gh stack link <ブランチ1> <ブランチ2> ...`（下から上の順）でスタックとして紐付ける。
最後に `gh stack submit --auto` を一度実行しておくこと。`gh stack link` はGitHub上でPR・スタックを作成するだけで、ローカルの追跡ファイル（`.git/gh-stack`）にそのスタックのGitHub ID・番号を書き戻さない。そのままだと `gh stack merge`（引数無し）など「現在のスタック」を暗黙参照するコマンドが「まだsubmitされていない」と失敗する。`submit --auto` は既存PRのタイトル・本文を上書きせず"up to date"の同期のみ行うため、安全に実行してよい。
