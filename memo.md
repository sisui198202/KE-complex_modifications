# 固定アプリとパブリックのキーバインド設定の適用順位について

(上に、パブリックキーバインド設定があるため、固定アプリキーバインド設定は適用できない)
1. パブリックキーバインド設定

2. 固定アプリキーバインド設定


(上に、固定アプリキーバインド設定があるため、固定アプリキーバインド設定も適用できるし、パブリックキーバインド設定も適用される)

1. 固定アプリキーバインド設定

2. パブリックキーバインド設定


* パブリックキーバインド設定を一番下に配置するようにした方が良い。

---------------------
# Profilesについて

JupyterLabを使用する。

tesutoは、テスト用のプロファイルとして使用する。理由は、Complex modificationsのEnable rulesで新規のルールを追加して、追加したルールが適用できているかを検証する場合にUpで一番上にのっていかないと適用できないケースがあるため。
---------------------
# [replace_vim.json.erb]

ハイフンは、["japanese_eisuu"]を使用しない理由: 日本語での文章入力では、-ではなく、ーを使うため。

    {
      "description": "Leftoption + Rightcommand_hypen(Replacekey)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("right_gui", ["left_alt"], ["caps_lock"]) %>,
          "to": <%= to([["hyphen"]]) %>
        }
      ]
    },
---------------------
# frontmost_application_if("excel")とmiをまとめたい

toで指定するキーが違うため、できない

{
      "description": "RightCommand + semicolon_NextTab(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("semicolon", ["right_gui"]) %>,
          "to": <%= to([["right_arrow", ["left_alt"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },

    {
      "description": "RightCommand + Semicolon_LatestTabToggle(mi)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("semicolon", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["close_bracket", ["left_shift", "right_gui"]]]) %>,
          "conditions": [ <%= frontmost_application_if("mi") %> ]
        }
      ]
    },

---------------------