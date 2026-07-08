# ローカルビルドと運用メモ

このリポジトリで `make` が失敗していた問題の原因と対応、以後のビルド手順をまとめます。

## 背景（問題の原因）

- 既存の `Makefile` が存在しない `core` ディレクトリへ処理を委譲していたため、`make` 実行時に `core: No such file or directory` で停止していました。

## 対応（概要）

- `Makefile` をローカルのスクリプトに基づく構成へ置き換えました。
  - `scripts/update-json.sh`（`src/json/*.erb` → `docs/json/*.json`）
  - `scripts/erb2html.rb` と `scripts/json2exhtml.rb`（`src/index.html.erb` → `docs/index.html`、追記事項の自動生成）
- 主要ターゲットを用意し、開発フローを簡潔化しました。

## 前提（必要な環境）

- macOS / Linux 相当のシェル環境
- Ruby（標準添付の `erb` が使えればOK）
- Python 3（プレビュー用、任意。Ruby の簡易サーバーでも可）

## 主要ターゲット（Make）

- `make`（= `make all`）: JSON と `docs/index.html` を更新
- `make update-json`: `src/json/*.erb` から `docs/json/*.json` を生成
- `make rebuild`: 生成物のクリーン後に `make all`
- `make update-dist`: 互換ターゲット（`make all` と同義）
- `make preview-server`: `docs` をルートにローカルサーバー（ポート 8000）を起動

## 使い方（基本フロー）

1. 生成（ビルド）

   ```sh
   make
   ```

   - 変更のある `src/json/*.erb` が `docs/json/*.json` に出力され、`src/index.html.erb` から `docs/index.html` が生成されます。

2. プレビュー（任意）

   ```sh
   make preview-server
   # ブラウザで http://localhost:8000 を開く
   ```

3. Karabiner-Elements への反映（任意）

   - `docs/json/*.json` を `~/.config/karabiner/assets/complex_modifications` へコピーし、
     Karabiner-Elements の Preferences から Import します。

   例:

   ```sh
   cp docs/json/window_control.json ~/.config/karabiner/assets/complex_modifications/
   ```

## トラブルシュート

- `make` が何も更新しない / 生成物が古いまま
  - まず `make rebuild` を実行して、生成物をクリーン後に再生成してください。

- Ruby が見つからない / 実行エラー
  - `ruby -v` で Ruby が使えるか確認してください。macOS ではプリインストールされていることが多いです。

- プレビューサーバーが起動しない
  - Python 3 がない場合は Ruby の簡易サーバーが自動フォールバックします。どちらもない場合は別途インストールしてください。

## 備考

- 上流の構成が `core` ディレクトリ（またはサブモジュール）に依存している場合、本リポジトリはその依存を排したローカル完結のビルド手順に変更しています。
  - `core` を導入する必要が出た場合は、`Makefile` を再度見直してください。

