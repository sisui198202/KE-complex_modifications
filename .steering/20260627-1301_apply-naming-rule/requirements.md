# Requirements: 命名規則の適用

## 目的

`rules/naming-rule.md` に定義された命名規則を `src/json/` 内の既存ファイルに適用し、
ファイル名の統一を図る。

## 背景

- `src/json/` 内に大文字混在、スペルミスなど命名の不統一がある
- `rules/naming-rule.md` で命名規則を定義済み
- 規則に従ってファイルをリネームする必要がある

## スコープ

- [x] `src/json/` 内のファイルリネーム（5ファイル）
- [x] `src/index.html.erb` の参照更新
- [x] `right_alt` → `right_option` 一括置換（250箇所）
- [x] `left_alt` → `left_option` 一括置換（174箇所）
- [x] `rules/naming-rule.md` に修飾キー命名規則を追加

## 受け入れ条件

- [x] 大文字混在ファイルが小文字に統一されている
- [x] スペルミス（sarari → safari）が修正されている
- [x] `src/index.html.erb` の参照が更新されている
- [x] 修飾キー名が `option` に統一されている
- [x] ビルドが成功する
- [x] コミット完了

## 制約

- tesuto, tesuto1 は現状維持（リネームしない）
- JSON内部の `title` は今回修正しない

## 対象ファイル

| 現在 | 修正後 |
|------|--------|
| `frontmost_pathFinder.json.erb` | `frontmost_pathfinder.json.erb` |
| `frontmost_pathFinder_summary.json.erb` | `frontmost_pathfinder_summary.json.erb` |
| `frontmost_Calendar.json.erb` | `frontmost_calendar.json.erb` |
| `frontmost_Calendar_summary.json.erb` | `frontmost_calendar_summary.json.erb` |
| `frontmost_sarari_summary.json.erb` | `frontmost_safari_summary.json.erb` |
