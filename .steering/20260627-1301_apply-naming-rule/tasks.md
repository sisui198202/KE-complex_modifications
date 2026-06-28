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
- [ ] double_push_key.json.erb (407行)

---

## Phase 2: 中型ファイル

- [ ] shotcutkey.json.erb
- [ ] shotcutkey_summary.json.erb
- [ ] hold.json.erb
- [ ] mouse_control.json.erb
- [ ] functionkey.json.erb
- [ ] replacekey.json.erb

---

## Phase 3: 小型ファイル（frontmost_*.json.erb）

- [ ] frontmost_antigravity_summary.json.erb
- [ ] frontmost_band.json.erb
- [ ] frontmost_band_summary.json.erb
- [ ] frontmost_browser_summary.json.erb
- [ ] frontmost_calendar.json.erb
- [ ] frontmost_calendar_summary.json.erb
- [ ] frontmost_chrome.json.erb
- [ ] frontmost_chrome_summary.json.erb
- [ ] frontmost_cursor_summary.json.erb
- [ ] frontmost_discord.json.erb
- [ ] frontmost_discord_summary.json.erb
- [ ] frontmost_eagle.json.erb
- [ ] frontmost_eagle_summary.json.erb
- [ ] frontmost_excel.json.erb
- [ ] frontmost_excel_summary.json.erb
- [ ] frontmost_finder.json.erb
- [ ] frontmost_finder_summary.json.erb
- [ ] frontmost_firefox.json.erb
- [ ] frontmost_firefox_summary.json.erb
- [ ] frontmost_intellij.json.erb
- [ ] frontmost_intellij_summary.json.erb
- [ ] frontmost_iterm.json.erb
- [ ] frontmost_iterm_summary.json.erb
- [ ] frontmost_kindle.json.erb
- [ ] frontmost_kindle_summary.json.erb
- [ ] frontmost_line.json.erb
- [ ] frontmost_line_summary.json.erb
- [ ] frontmost_mail.json.erb
- [ ] frontmost_mail_summary.json.erb
- [ ] frontmost_mi.json.erb
- [ ] frontmost_mi_summary.json.erb
- [ ] frontmost_notion.json.erb
- [ ] frontmost_notion_summary.json.erb
- [ ] frontmost_obsidian_summary.json.erb
- [ ] frontmost_pathfinder.json.erb
- [ ] frontmost_pathfinder_summary.json.erb
- [ ] frontmost_photos.json.erb
- [ ] frontmost_photos_summary.json.erb
- [ ] frontmost_preview.json.erb
- [ ] frontmost_preview_summary.json.erb
- [ ] frontmost_safari_summary.json.erb
- [ ] frontmost_virtualbox.json.erb
- [ ] frontmost_virtualbox_summary.json.erb
- [ ] frontmost_vivaldi.json.erb
- [ ] frontmost_vivaldi_summary.json.erb
- [ ] frontmost_vscode.json.erb
- [ ] frontmost_vscode_summary.json.erb

---

## Phase 4: 検証・完了

- [ ] make ビルド確認
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
