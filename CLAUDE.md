# 🎯 概要

本ファイルは、Claude Code および開発者が
**一貫した開発判断を行うための最上位原則（憲法）** を定義する。

---

## 共通ルール

本拡張機能は `chromeExtensions/CLAUDE.md` の共通ルールに従う。

クロス拡張タスク・共有リソース管理については親ディレクトリの CLAUDE.md を参照すること。

---

# 🗣 応答言語

- **常に日本語で応答すること**
- テンプレートやルールファイルが英語でも、出力・説明・コメントは日本語にする
- コード内のコメントも日本語を優先する

---

# 🚨 最重要原則（絶対）

```

.spec-workflow/steering > specs > code

```
```

requirements → design → tasks → 実装

```

---

## ❗ 基本思想

- 設計なき実装は禁止
- steering ドキュメントと矛盾する実装は禁止
- 未定義仕様を推測で決めてはいけない
- すべての変更は意図を持つ

---

# 🤖 AI行動原則

## 作業開始時

- 必ず steering ドキュメントを確認する
- 既存設計との整合性を確認する
- 影響範囲を把握する

---

## 実装前

- 必ず specs を作成する
- requirements → design → tasks の順で整理する
- 各段階でユーザー承認を得る

---

## Spec Workflow MCP 使用ルール

タスク・仕様作成時は **必ず Spec Workflow MCP を使用する**。

| ツール | 用途 |
|--------|------|
| `spec-workflow-guide` | ワークフロー全体のガイド取得 |
| `steering-guide` | steering ドキュメント操作ガイド |
| `spec-status` | 仕様ステータス確認 |
| `approvals` | 承認状態の管理 |
| `log-implementation` | 実装ログの記録 |

**禁止**: MCP を使用せずに手動で specs ファイルを作成すること

---

## 実装時

- tasks に基づいてのみ実装する
- 未承認・未確定状態で実装してはならない
- 不明点がある場合は実装を停止する
- 設定追加時は保存先が `sync` か `local` かを明確にする
- DOM セレクタ変更時は対象サイト / 対象画面で再確認する
- 自動処理は誤爆防止を優先し、条件を緩めすぎない

---

## 実装後

- steering ドキュメントへの影響を確認する
- 必要に応じて steering ドキュメント更新を提案する
- 知見は再利用可能な形で残す

---

# 🚫 禁止思想

- 設計未確定での実装
- steering / specs に存在しない内容の実装
- ユーザー未承認の設計変更
- 推測による仕様確定
- 状態不一致（tasks と実装のズレ）

---

# ⚡ 例外原則

以下は「本実装ではない」場合のみ許可する：

- 技術検証（PoC）
- DOM調査 / セレクタ検証
- バグ再現
- 簡易動作確認

## 条件

- 本実装に含めない
- 結果を design または decisions に反映する

---

# 🧭 開発の基本フロー

```
Branch（分岐）
→ Explore（理解）
→ Plan（設計）
→ Code（実装）
→ Review（確認）
→ Merge（統合）
```

---

## Branch

**新タスク開始時は必ずブランチを切る。**

```bash
git checkout main
git pull origin main
git checkout -b feature/{task-name}
```

### 必須ルール

- specs 作成前にブランチを切る
- main への直接 specs 作成は禁止
- spec + 実装を同一ブランチで管理する

### 例外（main 直接 OK）

- 単独の調査メモ追加
- 既存 spec の軽微修正（typo 等）
- docs/ideas/ への検討メモ追加

---

## Explore

- steering ドキュメント確認
- 既存コード確認
- 影響範囲把握

❗ 不明点がある場合は Plan に進んではならない

---

## Plan

- spec-workflow MCP で specs を作成
- requirements：何をやるか
- design：どうやるか
- tasks：どう進めるか
- 各段階でユーザー承認を得る

---

## Code

- tasks に基づいて実装
- Phase単位で進める

---

## Review

- 動作確認
- 設計との整合性確認
- steering ドキュメントへの影響確認

---

## Merge

- PR 作成（specs + 実装をセットで）
- レビュー後 main へマージ
- 作業ブランチ削除

---

# 📁 ドキュメント構造

## .spec-workflow/

プロジェクト全体の設計・要件・機能仕様を管理する。

```
.spec-workflow/
├── steering/                  # プロジェクト全体のガイダンス
│   ├── product.md             # プロダクト概要
│   ├── tech.md                # 技術スタック
│   └── structure.md           # プロジェクト構造
├── specs/                     # 機能別仕様
│   └── {feature-name}/
│       ├── requirements.md
│       ├── design.md
│       └── tasks.md
├── templates/                 # デフォルトテンプレート
└── user-templates/            # カスタムテンプレート
```

---

## .spec-workflow/archive/steering/ (旧タスク)

過去のタスク管理文書。今後は `.spec-workflow/specs/` を使用する。

---

## docs/

補助ドキュメントを管理する。

```
docs/
├── debug/                     # デバッグ記録
└── ideas/                     # アイデア・検討事項
```

---

## plan/

計画・改善を管理する。

```
plan/
├── README.md              # 構成ルール
├── todo.md                # 実行タスク
└── docs/                  # 改善計画
```

---

# 🧠 判断優先順位

迷った場合は必ず以下に従う：

```

1. .spec-workflow/steering
2. .spec-workflow/specs（requirements / design / tasks）
3. code

```

---

# 🔧 ECサイトセレクタ調査

セレクタ定義の根拠となる調査ファイル:

```
/Users/user/Work/buy/Target/{サイト名}/{サイト名:英数字}_site_structure/
```

**例:**
```
/Users/user/Work/buy/Target/日産オンラインショップ/nissanonlineshop_site_structure/
```

## 調査ファイルの内容

手動でサイト上の DevTools で調査した結果を格納:

- `yaml/` - 各フェーズのセレクタ定義（01_login.flow.yaml, 02_product.dom.yaml 等）
- `site_capture/` - 各画面の HTML/スクリーンショット
- `site_structure_definition.md` - 構造定義書

## 運用ルール

1. **新サイト追加時**: site_structure を先に作成してからセレクタを定義する
2. **セレクタ変更時**: yaml を更新してから ec-sites.json を修正する
3. **動作不具合時**: yaml と実サイトの差分を確認する

---

# 📝 更新トリガー

以下の変更時は steering ドキュメント更新要否を確認する:

- 新機能追加
- 既存仕様変更
- ストレージ項目追加 / 変更
- 外部サイト DOM 前提の変更
- セキュリティ制約の変更

---

# 🎯 このファイルの役割

- AIの判断基準を統一する
- 開発の一貫性を維持する
- 設計崩壊を防ぐ
- 再現性を確保する

---

# 🚀 最終原則

👉 設計なき実装は禁止
👉 steering ドキュメントが常に正
👉 不明点は止まる（進めない）
👉 変更は必ず意図を持つ
