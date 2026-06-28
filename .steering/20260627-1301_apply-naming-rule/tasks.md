# Tasks: manipulators 並び替え

## 完了済み

- [x] 修飾キー統一（gui → command）
- [x] rules/naming-rule.md 更新
- [x] window_control.json.erb 並び替え
- [x] GitHub Pages 反映

---

## Phase 1: 大型ファイル

- [x] replacekey_summary.json.erb (1020行)
- [x] functionkey_summary.json.erb (772行) ※重複F4削除、順序OK
- [x] double_push_key.json.erb (407行) ※順序OK

---

## Phase 2: 中型ファイル

- [x] shotcutkey.json.erb ※ERBインクルードのみ
- [x] shotcutkey_summary.json.erb ※並び替え完了
- [x] hold.json.erb ※機能グループ化、現状維持
- [x] mouse_control.json.erb ※順序OK
- [x] functionkey.json.erb ※ERBインクルードのみ
- [x] replacekey.json.erb ※全てleft_option、順序OK

---

## Phase 3: 小型ファイル（frontmost_*.json.erb）

### 非summaryファイル（テンプレートのみ、15行）- スキップ

- [x] frontmost_band.json.erb ※ERBインクルードのみ
- [x] frontmost_calendar.json.erb ※ERBインクルードのみ
- [x] frontmost_chrome.json.erb ※ERBインクルードのみ
- [x] frontmost_discord.json.erb ※ERBインクルードのみ
- [x] frontmost_eagle.json.erb ※ERBインクルードのみ
- [x] frontmost_excel.json.erb ※ERBインクルードのみ
- [x] frontmost_finder.json.erb ※ERBインクルードのみ
- [x] frontmost_firefox.json.erb ※ERBインクルードのみ
- [x] frontmost_intellij.json.erb ※ERBインクルードのみ
- [x] frontmost_iterm.json.erb ※ERBインクルードのみ
- [x] frontmost_kindle.json.erb ※ERBインクルードのみ
- [x] frontmost_line.json.erb ※ERBインクルードのみ
- [x] frontmost_mail.json.erb ※ERBインクルードのみ
- [x] frontmost_mi.json.erb ※ERBインクルードのみ
- [x] frontmost_notion.json.erb ※ERBインクルードのみ
- [x] frontmost_pathfinder.json.erb ※ERBインクルードのみ
- [x] frontmost_photos.json.erb ※ERBインクルードのみ
- [x] frontmost_preview.json.erb ※ERBインクルードのみ
- [x] frontmost_virtualbox.json.erb ※ERBインクルードのみ
- [x] frontmost_vivaldi.json.erb ※ERBインクルードのみ
- [x] frontmost_vscode.json.erb ※ERBインクルードのみ

### summaryファイル - 確認済み/修正済み

- [x] frontmost_antigravity_summary.json.erb ※順序OK
- [x] frontmost_band_summary.json.erb ※順序OK
- [x] frontmost_browser_summary.json.erb ※順序OK
- [x] frontmost_calendar_summary.json.erb ※順序OK
- [x] frontmost_chrome_summary.json.erb ※順序OK
- [x] frontmost_cursor_summary.json.erb ※順序OK
- [x] frontmost_discord_summary.json.erb ※順序OK
- [x] frontmost_eagle_summary.json.erb ※順序OK
- [x] frontmost_excel_summary.json.erb ※順序OK
- [x] frontmost_finder_summary.json.erb ※並び替え完了
- [x] frontmost_firefox_summary.json.erb ※並び替え完了
- [x] frontmost_intellij_summary.json.erb ※並び替え完了
- [x] frontmost_iterm_summary.json.erb ※順序OK
- [x] frontmost_kindle_summary.json.erb ※順序OK
- [x] frontmost_line_summary.json.erb ※順序OK
- [x] frontmost_mail_summary.json.erb ※順序OK
- [x] frontmost_mi_summary.json.erb ※順序OK
- [x] frontmost_notion_summary.json.erb ※順序OK
- [x] frontmost_obsidian_summary.json.erb ※順序OK
- [x] frontmost_pathfinder_summary.json.erb ※順序OK
- [x] frontmost_photos_summary.json.erb ※順序OK
- [x] frontmost_preview_summary.json.erb ※left_option並び替え完了
- [x] frontmost_safari_summary.json.erb ※順序OK
- [x] frontmost_virtualbox_summary.json.erb ※left_control並び替え完了
- [x] frontmost_vivaldi_summary.json.erb ※順序OK
- [x] frontmost_vscode_summary.json.erb ※right_command,left_option並び替え完了

---

## Phase 4: 検証・完了

- [x] make ビルド確認
- [ ] コミット
- [ ] push

---

## 並び順ルール

```
1. 単独キー（アルファベット順）
2. left_command + キー
3. right_command + キー
4. left_option + キー
5. right_option + キー
6. left_control + キー
7. right_control + キー
8. fn + キー
```
