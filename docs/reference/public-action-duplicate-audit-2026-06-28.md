# Public Action重複調査メモ

作成日: 2026-06-28

## 概要

この調査は、`target/KeyManageList_Mac.xlsm` の `M_キー定義マスタ` シートに登録されているキー定義のうち、`App=Public` として扱うべき共通操作が、個別アプリ行にも重複して登録されていないかを確認するために実施した。

今回のポイントは、「キーの押し方が同じか」ではなく、「同じ `Action` が Public と他 App にまたがって存在しているか」を基準に見た点にある。  
そのため、`Key` や `Modifiers` が異なっていても、`Action` 名が同一であれば重複候補として抽出している。

## 目的

`target/KeyManageList_Mac.xlsm` の `M_キー定義マスタ` シートについて、`App=Public` のうち指定した原本JSONに由来する `Action` が、他 `App` にも重複登録されているかを確認し、削除候補を整理する。

## 対象ファイル

### Public扱いで集計した原本

- `src/json/functionkey_summary.json.erb`
- `src/json/replacekey_summary.json.erb`
- `src/json/shotcutkey_summary.json.erb`
- `src/json/replacekey.json.erb`
- `src/json/shotcutkey.json.erb`
- `src/json/tesuto1.json.erb`

### 対象外

- `src/json/hold.json.erb`
- `src/json/mouse_control.json.erb`
- `src/json/tesuto.json.erb`
- `src/json/functionkey.json.erb`

## 調査条件

- 判定単位は `Action`
- `App=Public` の行のうち、上記原本に対応する `Action` を抽出
- 同じ `Action` が `App!=Public` に存在するものを重複として扱う
- 途中で `Cursor` を除外した削除候補一覧も別途作成

### 今回の判定で見ていないもの

- `Key` の一致、不一致
- `Modifiers` の一致、不一致
- `Trigger` の一致、不一致
- 実際にそのアプリで残すべき例外かどうかの最終判断

つまり今回の出力は、削除を自動決定するものではなく、「Public に寄せられる可能性がある候補を洗い出した一覧」である。

## 確認対象Excel

- [target/KeyManageList_Mac.xlsm](/Users/user/Work/dotfiles/KE-complex_modifications/target/KeyManageList_Mac.xlsm)

## 実施手順

### 1. Public原本の範囲を確定

ユーザー指定に基づき、`Public` として扱う原本JSONを限定した。  
この条件により、`hold` や `mouse_control` などの別用途定義は調査対象から除外した。

### 2. 原本JSONから Action 名を抽出

`src/json/*.erb` を直接評価せず、生成済みの `docs/json/*.json` を参照し、各 `description` から `Action` 相当の文字列を抽出した。  
例:

- `LeftCommand + B_PageDown` → `PageDown`
- `RightCommand + L_NextTab` → `NextTab`
- `Fn + G_WindowLeftOneThird` → `WindowLeftOneThird`

### 3. Excelの Public 行と対応付け

Excel `M_キー定義マスタ` のうち `App=Public` である行から、抽出済み `Action` と一致するものを対象にした。

### 4. 他 App に同じ Action があるか確認

対象となった `Public` 行について、`App!=Public` 側に同一 `Action` を持つ行を検索し、重複一覧として整理した。

### 5. 削除候補CSVを作成

重複一覧をそのまま使うと `Public` 1件に対して複数行に展開されるため、実際に見直す単位である `OtherRow` ごとにまとめた削除候補CSVを作成した。

### 6. Cursor 除外版を作成

`Cursor` は別意図で保持したい可能性があるため、レビューしやすいよう除外版CSVも作成した。

### 7. Excelの Notes 列へ削除候補メモを追記

`Cursor` 除外版CSVをもとに、`M_キー定義マスタ` の `Notes` 列へ削除候補メモを追記した。

## 集計結果

- 原本由来の `Action` 候補数: `132`
- Excel上で対応した `App=Public` 行数: `76`
- 他 `App` に同じ `Action` がある `Public Action` 数: `65`
- 重複一覧の総行数: `203`
- `Cursor` 除外後の削除候補数: `111`

### 削除候補のアプリ別件数

`Cursor` を含む削除候補CSVの件数上位:

- `Cursor`: `78`
- `Vscode`: `16`
- `Intellij`: `13`
- `PathFinder`: `13`
- `Excel`: `13`
- `firefox`: `12`
- `単独_Capslockオフ時`: `12`
- `Finder`: `12`
- `Discord`: `4`
- `Band`: `4`

`Cursor` 除外版の件数上位:

- `Vscode`: `16`
- `Intellij`: `13`
- `PathFinder`: `13`
- `Excel`: `13`
- `firefox`: `12`
- `単独_Capslockオフ時`: `12`
- `Finder`: `12`
- `Discord`: `4`
- `Band`: `4`
- `Eagle`: `3`

この結果から、`Cursor` が重複候補の大半を占めていることが分かる。

## 代表例

### PageDown

- Public元行: `3行目`
- `App=Public`
- `Key=B`
- `Trigger=Single`
- `Modifiers=LCmd`
- `Action=PageDown`
- 原本: `src/json/shotcutkey_summary.json.erb`

重複先:

- `189行目` `Vscode`
- `367行目` `Cursor`
- `416行目` `Cursor`
- `1089行目` `Discord`
- `1150行目` `Band`

このケースでは、`Public` 側の操作は `LeftCommand + B_PageDown` として `shotcutkey_summary` に存在し、同じ `Action=PageDown` がアプリ別にも散在している。  
今回の削除候補では、まず `Cursor` を除外したため、`Vscode / Discord / Band` が優先確認対象になっている。

### PageUp

- Public元行: `30行目`
- 重複先: `Vscode / Cursor / Discord / Band`

### NextTab

- Public元行: `44行目`
- 重複先: `Vscode / Cursor / Excel`

### MaxWindow

- Public元行: `54行目`
- 重複先: `Vscode / Cursor / Intellij / Chrome / firefox / PathFinder / Finder / Excel` など多数

この `Action` は重複先が多く、個別最適化の名残が残っている可能性が高い。  
一方で、アプリ個別ショートカットとの競合回避として残している可能性もあるため、削除前の確認優先度は高い。

## 作成した出力ファイル

- [target/public_action_duplicates.csv](/Users/user/Work/dotfiles/KE-complex_modifications/target/public_action_duplicates.csv)
  - `Public` 行と重複先行を1対多で並べた一覧
- [target/public_action_delete_candidates.csv](/Users/user/Work/dotfiles/KE-complex_modifications/target/public_action_delete_candidates.csv)
  - `OtherRow` 単位にまとめた削除候補一覧
- [target/public_action_delete_candidates_excluding_cursor.csv](/Users/user/Work/dotfiles/KE-complex_modifications/target/public_action_delete_candidates_excluding_cursor.csv)
  - `Cursor` を除外した削除候補一覧

### 各CSVの使い分け

`public_action_duplicates.csv`

- もっとも詳細な元データ
- `Public` 1行に対して、重複先が複数あれば複数行に展開される
- 「どの Public 行が、どの他 App 行と対応しているか」を確認するのに向いている

`public_action_delete_candidates.csv`

- 重複先の `OtherRow` 単位に整理した一覧
- 実際に見直す行番号ベースで確認しやすい
- 削除候補の母集団として使いやすい

`public_action_delete_candidates_excluding_cursor.csv`

- `Cursor` をいったん除外したレビュー用
- 優先確認対象を絞りたいときに使う

## CSV列の見方

### `public_action_duplicates.csv`

- `PublicRow`: Public 側の行番号
- `PublicAction`: Public 側の Action
- `PublicSourceJson`: 参照した生成済みJSON
- `PublicSourceDescription`: 元 description
- `OtherRow`: 重複先の行番号
- `OtherApp`: 重複先 App

### `public_action_delete_candidates.csv`

- `DeleteCandidateRow`: 見直し候補の行番号
- `DeleteCandidateApp`: 見直し候補の App
- `DeleteCandidateAction`: 見直し候補の Action
- `MatchedPublicRows`: 対応する Public 行番号
- `MatchedPublicSourceJson`: Public 原本として参照した JSON
- `DuplicateCount`: 対応する Public 件数

今回の集計では `DuplicateCount` はほぼ `1` だが、将来 `Public` 側に同一 `Action` が複数ある場合に備えて残している。

## Excelへの反映内容

`M_キー定義マスタ` シートの `Notes` 列へ、`Cursor` 除外版の削除候補 `111` 行に対して以下形式のメモを追記した。

```text
削除候補: Public Action重複 | PublicRow=... | Action=... | Source=...
```

例:

- `189行目` `Vscode` `PageDown`
- `1089行目` `Discord` `PageDown`
- `1150行目` `Band` `PageDown`

### Notes 追記の意図

専用の管理列がなかったため、既存構造を壊さずに確認印を残す方法として `Notes` 列を使った。  
このため、Excelを開いたときに行単位で削除候補を直接確認できる。

追記例:

```text
旧summaryから移行 (App=(Vscode))
削除候補: Public Action重複 | PublicRow=3 | Action=PageDown | Source=docs/json/shotcutkey_summary.json
```

## バックアップ

- [target/KeyManageList_Mac.before_public_dedupe_20260628.xlsm](/Users/user/Work/dotfiles/KE-complex_modifications/target/KeyManageList_Mac.before_public_dedupe_20260628.xlsm)
  - 作業途中の誤更新バックアップ
- [target/KeyManageList_Mac.before_delete_candidate_flag_20260628.xlsm](/Users/user/Work/dotfiles/KE-complex_modifications/target/KeyManageList_Mac.before_delete_candidate_flag_20260628.xlsm)
  - `Notes` 追記前バックアップ

## 今回の作業で行った補足対応

作業途中で、最初の重複判定を「完全一致」に寄せて解釈してしまい、意図と異なる更新を一度行った。  
その後、バックアップから `target/KeyManageList_Mac.xlsm` を元に戻し、今回の `Action` ベース判定で再実施している。

そのため、最終成果物としては以下を正とする。

- `target/KeyManageList_Mac.xlsm`
- `target/public_action_duplicates.csv`
- `target/public_action_delete_candidates.csv`
- `target/public_action_delete_candidates_excluding_cursor.csv`

## 注意点

- 今回の重複判定は `Action` ベースであり、`Key` や `Modifiers` の完全一致判定ではない
- `Action` 名が同じでも、意図的にアプリ別で残すべきケースはあり得る
- そのため、CSVは即削除リストではなく、目視確認用の削除候補一覧として扱う
- `docs/json/*.json` の description から `Action` を抽出しているため、description 命名が揺れている場合は見落としや過抽出の可能性がある

## 今後の進め方

次に実施するなら、以下の順で進めるのが安全。

1. `target/public_action_delete_candidates_excluding_cursor.csv` を優先確認する
2. `Vscode / Excel / PathFinder / Intellij / Finder` など、利用頻度の高いAppから削除可否を判断する
3. 問題なければ Excel 上で該当行を整理する
4. 最後に `Cursor` を含む候補を別枠で再確認する

もし次回も同様の棚卸しを行う場合は、このドキュメントと CSV 一式を起点にすれば再現しやすい。
