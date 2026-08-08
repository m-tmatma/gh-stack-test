# CLAUDE.md

## gh stack でのPR作成

`gh stack submit --auto` はPRのタイトル・本文をコミットメッセージ/ブランチ名から自動生成してしまうため使わない。
代わりに、スタックの各ブランチを `git push` した上で `gh pr create --title "..." --body "..." --base <ベースブランチ>` を使い、Claude が変更内容を踏まえて作成時点でタイトルと本文を指定すること。
全ブランチのPRを作成し終えたら、`gh stack link <ブランチ1> <ブランチ2> ...`（下から上の順）でスタックとして紐付ける。
最後に `gh stack submit --auto` を一度実行しておくこと。`gh stack link` はGitHub上でPR・スタックを作成するだけで、ローカルの追跡ファイル（`.git/gh-stack`）にそのスタックのGitHub ID・番号を書き戻さない。そのままだと `gh stack merge`（引数無し）など「現在のスタック」を暗黙参照するコマンドが「まだsubmitされていない」と失敗する。`submit --auto` は既存PRのタイトル・本文を上書きせず"up to date"の同期のみ行うため、安全に実行してよい。

## 統合ブランチが main 以外の場合の注意

スタックの統合先（trunk）が `main` 以外（例: `release/next`）の場合、`gh stack link` には必ず `--base <統合ブランチ>` を明示すること。省略するとリポジトリのデフォルトブランチ（`main`）が使われ、既存PRのbaseが勝手に上書きされる（`Updated base branch for PR #N to main` と表示される）。
一度スタックに組み込まれたPRは `gh pr edit --base` でbase変更ができない（`Cannot change the base branch because the pull request is part of a stack.`）。誤って上書きした場合は、`gh stack unstack <スタック番号>`（PRは削除されない）でグルーピングを解除してから `gh pr edit <PR番号> --base <正しいブランチ>` で修正し、`--base` を明示して `gh stack link` をやり直すこと。
