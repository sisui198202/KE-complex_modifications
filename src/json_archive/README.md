# アーカイブ済み設定ファイル

## 目的

このディレクトリには、現在使用していないKarabiner-Elements設定ファイルが保管されています。

ファイルは削除されておらず、必要になったら簡単に復元できます。

## アーカイブされたファイル一覧

### MySQL Workbench関連
- `frontmost_mysqlworkbench.json.erb`
- `frontmost_mysqlworkbench_summary.json.erb`

### Parallels Desktop関連
- `frontmost_pararelldesk.json.erb`
- `frontmost_pararelldesk_summary.json.erb`

### その他
- `frontmost_readgamen_summary.json.erb`
- `vim_emu.json.erb`

## 復元方法

必要になった場合は、以下のコマンドでファイルを復元できます：

```bash
# 例: vim_emu.json.erbを復元する場合
git mv src/json_archive/vim_emu.json.erb src/json/

# 復元後、makeコマンドでビルド
make
```

## 注意事項

- これらのファイルはgit履歴に残っているため、完全に失われることはありません
- `src/json/*.erb`のみがビルド対象のため、このディレクトリ内のファイルは自動的にビルドされません
- ファイルの移動は`git mv`で行われているため、履歴が保持されています

## アーカイブ日時

2025-12-29
