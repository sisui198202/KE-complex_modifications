# Import表記が更新されない問題の整理（原因と対応）

## 背景
- サイト上の表示（パネルのタイトル）は `src/json/window_control.json.erb` の `title` と一致。
- ただし、サイトから「Import」後に Karabiner-Elements の「Add rule」一覧で表示される名称が古いままになる事象が発生。

## 原因
- Karabiner-Elements の「Add rule」一覧は、JSON 内の `rules[].description` を名称として表示する。
  - `title` を更新しても `rules[].description` が古いままだと、Import 後の表記は変わらない。
- さらに Import リンクの URL が毎回同一だと、環境によってはキャッシュが効き、最新 JSON を取得しない可能性がある。

## 対応内容
1) ルール名の更新
- 対象ファイル: `src/json/window_control.json.erb`
- 変更点:
  - `title` を `WindowControlSummary987` に更新
  - 先頭ルール（最上位の） `rules[0].description` を `WindowsControlSummary987` に更新

2) Import リンクにキャッシュバスターを付与
- 対象ファイル: `docs/js/main.js`
- 変更点:
  - `karabiner://...import?url=<JSON_URL>` に埋め込む `JSON_URL` を生成する際、`?t=<timestamp>` を付けて毎回ユニークな URL にするよう修正
  - これによりブラウザ/アプリのキャッシュを回避し、最新の JSON を確実に取得

## 実施ファイル一覧（今回の修正）
- `src/json/window_control.json.erb`
- `docs/js/main.js`

## 確認手順
- 生成: `make`（必要に応じて `make rebuild`）
- ローカル確認: `make preview-server` → `http://localhost:8000` を開き、WindowControl の Import を押す
- Karabiner-Elements の「Add rule」に `WindowsControlSummary987` と表示されること
- 旧表記が残る場合:
  - Karabiner-Elements を終了
  - `~/.config/karabiner/assets/complex_modifications/` の古い `window_control.json` を削除
  - Karabiner-Elements を起動し直して再度 Import

## 備考
- サイト上のパネル名は JSON の `title` を、Import 後に Karabiner が表示する名称は `rules[].description` を参照するため、目的に応じて両方を整合させる必要がある。
