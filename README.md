# KE-complex_modifications

rcmdnk による Karabiner-Elements 向けの complex_modifications 集です。

http://rcmdnk.com/KE-complex_modifications/

## 最短手順

1. `src/json` などを編集します。
2. `karm` または `make` で `docs/` 配下の公開ファイルを更新します。
3. `karg` でコミットして GitHub へ push します。
4. `karu` で GitHub Pages の公開結果を確認します。

## 開発手順

### ドキュメント更新

ターミナルで `make` を実行します。

```sh
make
```

### ルール追加

1. ファイルを [src/json](https://github.com/pqrs-org/KE-complex_modifications/tree/master/src/json) に置きます。
   もしくは [docs/json](https://github.com/pqrs-org/KE-complex_modifications/tree/master/docs/json) に直接配置します。
2. [src/index.html.erb](https://github.com/pqrs-org/KE-complex_modifications/tree/master/src/index.html.erb) に `file_import_panel` を追加します。
3. ターミナルで `make` を実行します。

キー名の定義は[こちら](https://github.com/tekezo/Karabiner-Elements/blob/master/src/apps/PreferencesWindow/PreferencesWindow/Resources/simple_modifications.json)です。

### ローカルテスト

1. JSON ファイルを `~/.config/karabiner/assets/complex_modifications` にコピーします。
2. Karabiner-Elements Preferences からルールを読み込みます。

### 例

```
$ cp docs/json/caps_lock.json ~/.config/karabiner/assets/complex_modifications
```

その後、`Karabiner-Elements Preferences > Complex Modifications > Rules > Add rule` を開きます。

## Karabiner-Elements での利用方法

### 別サイトからファイルを取り込む

1. JSON ファイルを自分のサイトに配置します。
2. `karabiner://karabiner/assets/complex_modifications/import?url=<JSON_URL>` というリンクを作成します。
3. そのリンクを Web ブラウザで開きます。

## GitHub Pages 連携

このリポジトリでは、生成した `docs/` 配下を GitHub Pages で公開します。

### 公開までの流れ

1. `pqrs-org/KE-complex_modifications` を Fork します。
2. Fork したリポジトリの `Settings > Pages` を開き、GitHub Pages を有効にします。
3. このリポジトリで `make` または `karm` を実行し、`docs/json/*.json` と `docs/index.html` を更新します。
4. `karg` でコミットと `push` を行います。
5. `karu` で公開ページを開き、反映内容を確認します。

公開ページ: `https://sisui198202.github.io/KE-complex_modifications/`

補足: `make` の生成物は主に `docs/` 配下です。GitHub Pages 側はこの公開用ファイル群を配信します。

## プロジェクト構造

### ディレクトリ構成

```
docs/
├── archive/        # 保留中のコード断片
├── debug/          # デバッグ・トラブルシュート記録
├── reference/      # 開発参照情報・設定チェックリスト
├── json/           # 生成された JSON ファイル
└── ...

scripts/            # ビルド・変換スクリプト
src/                # ソースファイル（erb テンプレート）
```

### 主要ドキュメント

| ファイル | 内容 |
|---------|------|
| `DEVELOPMENT.md` | ビルド手順・運用メモ |
| `docs/reference/development-notes.md` | 開発参照情報 |
| `docs/debug/` | デバッグ記録 |

## 補助コマンド

この環境では、Karabiner 設定リポジトリの運用用に以下のシェル関数・エイリアスを使っています。

### `karg`

Karabiner 設定リポジトリへ変更を `git add` し、コミットメッセージ入力後に `git commit` と `git push` を実行します。

```zsh
karg() {
  cd "$HOME/Work/dotfiles/KE-complex_modifications" || return 1
  git add . && git status
  echo "Type commit comment:"
  read -r comment
  if [[ -z "$comment" ]]; then
    echo "コミットメッセージが空です。キャンセルしました。"
    return 1
  fi
  git commit -m "$comment" && git push
}
```

### `karm`

Karabiner 設定リポジトリへ移動して `make` を実行します。

```zsh
karm() {
  cd "$HOME/Work/dotfiles/KE-complex_modifications" || return 1
  make
}
```

### `karu`

生成済みの公開ページをブラウザで開きます。

```zsh
alias karu='open https://sisui198202.github.io/KE-complex_modifications/'
```

### 補助コマンドの使い分け

- `karm`: 公開用ファイルを再生成します。
- `karg`: 変更をコミットして GitHub へ push します。
- `karu`: GitHub Pages の公開ページをブラウザで開きます。
