[Exploer]
com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717

[Sublime]
com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717

[Vscode]
com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717

[Excel]
com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717

[Access]
com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717

[ファイル名を指定して実行]
com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs

[Uws2Exe_uwscのExe化をするツール]
com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717

[メモ帳]
com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717

---------------------
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