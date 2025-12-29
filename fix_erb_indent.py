#!/usr/bin/env python3
"""
ERBファイルのインデント整理スクリプト
ERBタグ（<%= ... %>）を保護しながら、JSON構造を4スペースインデントに統一する
"""

import re
import glob
import os
from pathlib import Path

def protect_erb_tags(content):
    """ERBタグを一時的にプレースホルダーに置換"""
    placeholders = {}
    counter = 0

    def replace_erb(match):
        nonlocal counter
        placeholder = f"___ERB_PLACEHOLDER_{counter}___"
        placeholders[placeholder] = match.group(0)
        counter += 1
        return placeholder

    # <%= ... %> を保護
    protected = re.sub(r'<%=.*?%>', replace_erb, content)
    return protected, placeholders

def restore_erb_tags(content, placeholders):
    """プレースホルダーを元のERBタグに戻す"""
    for placeholder, erb_tag in placeholders.items():
        content = content.replace(placeholder, erb_tag)
    return content

def fix_indent_line(line, current_indent):
    """1行のインデントを修正"""
    stripped = line.lstrip()
    if not stripped:
        return line

    # インデント計算
    indent_change = 0

    # 閉じ括弧の前にインデントを減らす
    if stripped.startswith('}') or stripped.startswith(']'):
        indent_change = -1

    # 新しいインデントレベルを計算
    new_indent_level = max(0, current_indent + indent_change)
    new_line = ' ' * (new_indent_level * 4) + stripped

    # 開き括弧の後にインデントを増やす
    if stripped.rstrip().endswith('{') or stripped.rstrip().endswith('['):
        return new_line, new_indent_level + 1
    elif stripped.startswith('}') or stripped.startswith(']'):
        return new_line, new_indent_level
    else:
        return new_line, new_indent_level

def fix_json_indent(content):
    """JSON部分のインデントを修正"""
    lines = content.split('\n')
    fixed_lines = []
    current_indent = 0

    for line in lines:
        if line.strip():
            fixed_line, current_indent = fix_indent_line(line, current_indent)
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append('')

    return '\n'.join(fixed_lines)

def process_erb_file(filepath):
    """ERBファイルのインデントを整理"""
    print(f"Processing: {filepath}")

    # ファイル読み込み
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # ERBタグを保護
    protected_content, placeholders = protect_erb_tags(content)

    # JSONインデント修正
    fixed_content = fix_json_indent(protected_content)

    # ERBタグを復元
    final_content = restore_erb_tags(fixed_content, placeholders)

    # ファイル書き込み
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"  ✓ Completed: {filepath}")

def main():
    """メイン処理"""
    # src/json/*.erbファイルをすべて取得
    script_dir = Path(__file__).parent
    json_dir = script_dir / 'src' / 'json'
    erb_files = list(json_dir.glob('*.erb'))

    print(f"Found {len(erb_files)} ERB files")
    print("=" * 60)

    # 各ファイルを処理
    for filepath in erb_files:
        try:
            process_erb_file(filepath)
        except Exception as e:
            print(f"  ✗ Error processing {filepath}: {e}")

    print("=" * 60)
    print(f"Completed processing {len(erb_files)} files")
    print("\n次のステップ:")
    print("1. makeコマンドを手動で実行してください")
    print("2. エラーが発生した場合は 'git checkout src/json/*.erb' で復元してください")

if __name__ == '__main__':
    main()
