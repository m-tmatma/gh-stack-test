# CLAUDE.md

## gh stack でのPR作成

`gh stack submit --auto` はPRのタイトル・本文をコミットメッセージ/ブランチ名から自動生成してしまうため使わない。
代わりに、スタックの各ブランチを `git push` した上で `gh pr create --title "..." --body "..." --base <統合ブランチ>` を使い、Claude が変更内容を踏まえて作成時点でタイトルと本文を指定すること。
全ブランチのPRを作成し終えたら、`gh stack link --base <統合ブランチ> <ブランチ1> <ブランチ2> ...`（下から上の順）でスタックとして紐付ける。統合ブランチ（trunk）がリポジトリのデフォルトブランチと一致する場合でも `--base` は省略せず常に明示すること。省略すると `gh stack link` はリポジトリのデフォルトブランチを使うため、デフォルトブランチと統合ブランチが異なるリポジトリでは既存PRのbaseが意図せず上書きされる（`Updated base branch for PR #N to <デフォルトブランチ>` と表示される）。
最後に `gh stack submit --auto` を一度実行しておくこと。`gh stack link` はGitHub上でPR・スタックを作成するだけで、ローカルの追跡ファイル（`.git/gh-stack`）にそのスタックのGitHub ID・番号を書き戻さない。そのままだと `gh stack merge`（引数無し）など「現在のスタック」を暗黙参照するコマンドが「まだsubmitされていない」と失敗する。`submit --auto` は既存PRのタイトル・本文を上書きせず"up to date"の同期のみ行うため、安全に実行してよい。

## gh stack unstack は必ずスタック番号を指定する

引数無しの `gh stack unstack` は、ローカル追跡ファイル（`.git/gh-stack`）にGitHub側のスタックIDが記録されていない場合（`gh stack link` 後に `gh stack submit --auto` を実行し忘れた場合など）、`⚠ Stack has no remote ID — skipping server-side unstack` と表示され、**ローカル追跡を削除するだけでGitHub側のスタックは解除されない**。成功メッセージ（`✓ Stack removed from local tracking`）が出るため一見成功したように見えるが、`gh api repos/<owner>/<repo>/stacks` で確認するとスタックが残っている。
確実に解除するには、**スタック番号を明示して `gh stack unstack <スタック番号>` を使うこと**。ローカル追跡の状態に関わらずGitHub API経由で直接動作するため、この問題を回避できる。

## base branch を誤って上書きした場合の復旧

一度スタックに組み込まれたPRは `gh pr edit --base` でbase変更ができない（`Cannot change the base branch because the pull request is part of a stack.`）。`--base` の指定漏れなどで誤って上書きした場合は、`gh stack unstack <スタック番号>`（PRは削除されない）でグルーピングを解除してから `gh pr edit <PR番号> --base <正しいブランチ>` で修正し、`--base` を明示して `gh stack link` をやり直すこと。
