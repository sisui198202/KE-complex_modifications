# KE-complex_modifications 命名規則

## 目的

`src/json/*.json.erb` ファイルの命名を統一し、
ファイル名だけで内容・対象・種別が分かる状態を作る。

---

## 適用対象

```
src/json/*.json.erb
```

---

## 命名規則

### 基本原則

- **小文字のみ** を使用する
- **アンダースコア区切り**（`_`）を使用する
- **拡張子は `.json.erb`** とする
- **アプリ名は公式名を小文字化** する
- **英語のみ** を使用する

---

### ファイル名構造

| カテゴリ | 基本版 | summary版 |
|---------|--------|-----------|
| アプリ別 | `frontmost_{appname}.json.erb` | `frontmost_{appname}_summary.json.erb` |
| 機能系 | `{function}.json.erb` | `{function}_summary.json.erb` |
| テスト用 | `test_{purpose}.json.erb` | - |

---

### アプリ名の表記ルール

| 公式名 | ファイル名 |
|--------|-----------|
| Path Finder | `pathfinder` |
| Calendar | `calendar` |
| Safari | `safari` |
| VS Code | `vscode` |
| iTerm2 | `iterm` |
| IntelliJ IDEA | `intellij` |
| Discord | `discord` |
| LINE | `line` |
| Notion | `notion` |
| Obsidian | `obsidian` |

---

## カテゴリと並び順

### 並び順

```
1. 機能系（アルファベット順）
   - double_push_key
   - functionkey / functionkey_summary
   - hold
   - mouse_control
   - replacekey / replacekey_summary
   - shotcutkey / shotcutkey_summary
   - window_control

2. アプリ別（アルファベット順、基本版→summary版）
   - frontmost_band / frontmost_band_summary
   - frontmost_calendar / frontmost_calendar_summary
   - frontmost_chrome / frontmost_chrome_summary
   - ...

3. テスト用（末尾）
   - test_*.json.erb
```

---

## ペア構成ルール

- **基本版**: 詳細な設定
- **summary版**: 簡略化版

| 状況 | 対応 |
|------|------|
| 両方必要 | 両方作成 |
| 基本版のみで十分 | summary版は不要 |
| summary版のみ存在 | 基本版を追加、または単独ファイルにリネーム |

---

## 修飾キー命名規則

JSON内部の修飾キー名は macOS の公式名称に統一する。

| 使用しない | 使用する |
|-----------|----------|
| `left_alt` | `left_option` |
| `right_alt` | `right_option` |

理由：

- macOS では Option キーが公式名称
- Karabiner-Elements は両方認識するが、`option` で統一する
- Windows 由来の `alt` は使用しない

---

## 禁止事項

- 大文字の使用（`Calendar` → NG）
- キャメルケース（`pathFinder` → NG）
- スペルミス（`sarari` → NG）
- 日本語ローマ字（`tesuto` → NG）
- ハイフン区切り

---

## 修正履歴

| 修正前 | 修正後 | 理由 | 状態 |
|--------|--------|------|------|
| `frontmost_pathFinder.json.erb` | `frontmost_pathfinder.json.erb` | 小文字統一 | ✅ 完了 |
| `frontmost_pathFinder_summary.json.erb` | `frontmost_pathfinder_summary.json.erb` | 小文字統一 | ✅ 完了 |
| `frontmost_Calendar.json.erb` | `frontmost_calendar.json.erb` | 小文字統一 | ✅ 完了 |
| `frontmost_Calendar_summary.json.erb` | `frontmost_calendar_summary.json.erb` | 小文字統一 | ✅ 完了 |
| `frontmost_sarari_summary.json.erb` | `frontmost_safari_summary.json.erb` | スペル修正 | ✅ 完了 |
| `tesuto.json.erb` | - | 現状維持（テスト用） | - |
| `tesuto1.json.erb` | - | 現状維持（テスト用） | - |
| `*_alt` (JSON内部) | `*_option` | macOS公式名称統一 | ✅ 完了 |

---

## チェックリスト

### 新規追加時

- [ ] 全て小文字か
- [ ] アンダースコア区切りか
- [ ] アプリ名の表記が統一されているか
- [ ] JSON内部のtitleがファイル名と整合しているか

### 定期チェック

- [ ] 大文字小文字の不統一がないか
- [ ] スペルミスがないか
- [ ] 孤立したsummary版がないか
- [ ] テスト用ファイルが混入していないか
