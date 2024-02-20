## frontmost_finder.json.erb　でショットカットキー登録できない

correct formatとエラー表示

代用として、「tesuto.json.erb」でショットカットキー登録すること

---------------------
## 一括設定

replacekeysummary.json

shotcutkeysummary.json

window_control.json

(注)
"_comment": "",を入れていると、うまく設定が反映されない。

---------------------
## 個別設定

frontmost_~.json

replacekey.json

shotcutkey.json

double_push_key.json

---------------------
## 1つ説明で複数の設定を入力するパターン
{
  "title": "WindowControl123",
  "rules": [
              {
                "description": "Fn + ~_WindowsControl(WindowControl)",
                "manipulators": [
                  {
                    "description": "Fn + U_WindowLeftUp",
                    "type": "basic",
                    "from": <%= from("u", ["fn"], ["caps_lock"]) %>,
                    "to": <%= to([["6", "right_alt"]]) %>
                  },
                  {
                    "description": "Fn + H_LeftWindowMove",
                    "type": "basic",
                    "from": <%= from("h", ["fn"], ["caps_lock"]) %>,
                    "to": <%= to([["2", ["right_alt"]]]) %>
                  }
              ]
              }
          ]
}

---------------------
## 1つ説明で1つの設定を入力するパターン

{
    "title": "FrontmostIfPararel",
    "rules": [
      {
        "description": "LeftCommand + W_CurrentCursol-EndRowSelect(Pararell)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("w", ["left_control"], ["caps_lock"]) %>,
            "to": <%= to([["equal_sign", "left_option"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %>]
          }
        ]
      },
      {
        "description": "RightCommand + ._MaxWindows(Pararell)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("period", ["right_gui"], ["caps_lock"]) %>,
            "to": <%= to([["1", "left_option"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %>]
          }
        ]
      }
    ]
}

---------------------
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

[SSMS]
com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717

[Chrome_Windows]
com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717

[PowerShell]
com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717

[qdir]
com.parallels.winapp.cc097fe29f445d49eb74bd5993a02853.b9dc48efd5094ca8a69c0e98f2ecf717

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
## capslockがオンの時、f7で起動し、capslockがオフの時はpublicで指定したf7の挙動

```
{
  "description": "F7_ステップアウト(intellij)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("f7", ["caps_lock"]) %>,
      "to": <%= to([["2", ["right_gui","right_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("intellij") %> ]
    }
  ]
}
```

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
## backup FrontmostIfPararel

{
    "title": "FrontmostIfPararel",
    "rules": [
      {
        "description": "LeftCommand + W_CurrentCursol-EndRowSelect(Pararell)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("w", ["left_control"], ["caps_lock"]) %>,
            "to": <%= to([["equal_sign", "left_option"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %>]
          }
        ]
      },
      {
        "description": "RightCommand + ._MaxWindows(Pararell)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("period", ["right_gui"], ["caps_lock"]) %>,
            "to": <%= to([["1", "left_option"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %>]
          }
        ]
      },
      {
      "description": "RightCommand + A_NewFileCreate(Pararell)",
      "_comment": "Windowsのvscodeで新規ファイルを作成するショットカットキーの為にこの設定が必要",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("a", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["n", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %>]
        }
      ]
    },
    {
      "description": "LeftCommand + Quote_Single Column Editor Layout(Pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("quote", ["left_control"], ["caps_lock"]) %>,
          "to": <%= to([["h", ["right_control"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
    {
      "description": "RightCommand + i_Neight bour(Pararell)",
      "_comment": "WindowsSublimeの右のエディターにカーソル移動",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("i", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["i", ["right_control"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
{
                        "description": "コマンドキーを単体で押したときに、英数・かなキーを送信する。（左コマンドキーは英数、右コマンドキーはかな）(Pararell)",
                        "_comment": "下記にKaravinerツール「frontmostApplicationで日本語_英語キー切り替えをLeftCommandとRightCommandでしたい場合、ウィンドウコード確認し、下記に入力、Vscode_d51,Sublime_7d5,Excel通常画面_VBE_c1d",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "left_control",
                                    "modifiers": {
                                      "optional": [
                                        "caps_lock"
                                      ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "left_control",
                                        "lazy": true
                                    }
                                ],
                                "to_if_alone": [
            {
              "key_code": "f12",
              "modifiers": [
                "left_control"
              ]
            }
          ],
"conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.parallels.desktop.console$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.cc097fe29f445d49eb74bd5993a02853.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ],
                                "type": "basic"
                            },
                            {
                                "from": {
                                    "key_code": "right_command",
                                    "modifiers": {
                                      "optional": [
                                        "caps_lock"
                                      ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "right_command",
                                        "lazy": true
                                    }
                                ],
                                "to_if_alone": [
            {
              "key_code": "f9",
              "modifiers": [
                "left_control"
              ]
            }
          ],
"conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.parallels.desktop.console$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.cc097fe29f445d49eb74bd5993a02853.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ],
                                "type": "basic"
                            }
                        ]
},
{
  "description": "LeftCommand + Comma_AppsSelect-previous(Pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "modifiers": {
          "mandatory": [
            "left_control"
          ]
        },
        "key_code": "comma"
      },
      "to": [
        {
          "repeat": true,
          "key_code": "tab",
          "modifiers": [
            "left_alt",
            "right_shift"
          ],
          "halt": true
        }
      ],
      "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.parallels.desktop.console$",
               "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.cc097fe29f445d49eb74bd5993a02853.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ]
    }
  ]
},
{
  "description": "LeftCommand + Period_AppsSelect-next(Pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "modifiers": {
          "mandatory": [
            "left_control"
          ]
        },
        "key_code": "period"
      },
      "to": [
        {
          "repeat": true,
          "key_code": "tab",
          "modifiers": [
            "right_alt"
          ],
          "halt": true
        }
      ],
      "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.parallels.desktop.console$",
               "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.cc097fe29f445d49eb74bd5993a02853.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ]
    }
  ]
},
   {
      "description": "rightcommand + K_CopyCurrentRowCut(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("k", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["5", ["right_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
{
  "description": "RightCommand + O(オー)_SameWordExpandSelection(pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("o", ["right_gui"], ["caps_lock"]) %>,
      "to": <%= to([["4", ["right_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
    }
  ]
},
{
  "description": "LeftCommand + O(オー)_Column2SplitEditerScreen(pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("o", ["left_control"], ["caps_lock"]) %>,
      "to": <%= to([["1", ["right_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
    }
  ]
},
  {
      "description": "RightCommand + Semicolon_LatestTabToggle(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("semicolon", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["6", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
  {
      "description": "RightCommand + L_NextTab(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("l", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["7", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
  {
      "description": "RightCommand + U_ColumnSelection(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("u", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["8", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
  {
      "description": "LeftCommand + D_AllSelect(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("d", ["left_control"], ["caps_lock"]) %>,
          "to": <%= to([["9", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
      {
      "description": "RightCommand + J_1RowSelect(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("j", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["1", ["left_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
      {
      "description": "RightCommand + Z_0[ゼロ](pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("z", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["2", ["left_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
    {
      "description": "Rightoption + Leftoption_anbasado(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("left_alt", ["right_alt"], ["caps_lock"]) %>,
          "to": <%= to([["3", ["left_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
{
  "description": "LeftCommand + X_iterm2ActiveWindow(pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("x", ["left_control"], ["caps_lock"]) %>,
      "to": <%= to([["5", ["left_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
    }
  ]
},
   {
      "description": "LeftContorl_CellEdit(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("fn") %>,
          "to": <%= to([["f2"]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
   {
      "description": "アクセスキーできない_fn_alt(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("right_control") %>,
          "to": <%= to([["left_option"]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
    {
      "description": "検討中_LeftAlt_Copy(Pararell)",
      "_comment": "エクスプローラー_bf73",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "left_alt"
          },
          "to": [
            {
              "key_code": "left_alt"
            }
          ],
          "to_if_alone": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "c",
              "modifiers": "right_gui"
            }
          ],
"conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^org.virtualbox.app.VirtualBoxVM$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.76868ae832f6c6bd26cadc7d7c269986.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.bf448b76d11422f4a518bec20eb47937.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ]
        }
      ]
    },
{
  "description": "使用していない_LeftOption + J_ChromeActiveWindow(pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("j", ["left_alt"], ["caps_lock"]) %>,
      "to": <%= to([["4", ["left_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
    }
  ]
},
{
  "description": "LeftCommand + U_Undo(pararell)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("u", ["left_gui"], ["caps_lock"]) %>,
      "to": <%= to([["6", ["left_option"]]]) %>,
      "conditions": [ <%= frontmost_application_if("pararell") %> ]
    }
  ]
},
  {
      "description": "うまくいかないF8_StepIn(pararell)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("f8", ["caps_lock"]) %>,
          "to": <%= to([["9", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pararell") %> ]
        }
      ]
    },
      {
        "description": "うまくいかないfn_Rename(Pararell)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("fn", ["caps_lock"]) %>,
            "to": <%= to([["f2"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %>]
          }
        ]
      },
{
        "description": "AccessのVBEで反応しない_RightAlt + V_Paste(Access)VBE",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("v", ["right_alt"], ["caps_lock"]) %>,
            "to": <%= to([["v", "right_control"]]) %>,
            "conditions": [ <%= frontmost_application_if("pararell") %> ]
          }
        ]
  }
    ]
}

---------------------
## WindowsのChromeでインストールする必要があるのにMacのChromeでインストールしてしまうのを防ぐ為に下記の2を使用していたが、インストールする頻度が少ない為、MacChromeで統一させる

    {
      "description": "LeftOption + J_ChromeActiveWindow1(WindowControl)",
      "_comment": "WindowsのChromeでインストールする必要があるのにMacのChromeでインストールしてしまうのを防ぐ為に下記の2を使用していたが、インストールする頻度が少ない為、MacChromeで統一させる",
      "type": "basic",
      "from": <%= from("j", ["left_alt"], ["caps_lock"]) %>,
      "to": <%= set_shell_command(["open -a 'Google Chrome.app'"]) %>
    },
---------------------
## コメント入力だと反応しない為、ここにメモ

        {
	"description": "RightCommand + A_NewFileCreate(VirtualMachine)",
	"_comment": "Windowsのvscodeで新規ファイルを作成するショットカットキーの為にこの設定が必要",
          "type": "basic",
          "from": <%= from("a", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["n", ["right_option"]]]) %>,
          "conditions": [ <%= frontmost_application_if("virtual_machine") %>]
        },

---------------------
## コメント入力だと反応しない為、ここにメモ

        {
	"description": "RightCommand + i_Neight bour(VirtualMachine)",
	"_comment": "WindowsSublimeの右のエディターにカーソル移動",
          "type": "basic",
          "from": <%= from("i", ["right_gui"], ["caps_lock"]) %>,
          "to": <%= to([["i", ["right_control"]]]) %>,
          "conditions": [ <%= frontmost_application_if("virtual_machine") %> ]
        },
---------------------
## "LeftCommand + J_DownArrow_X1(Chrome)"が"LeftCommand + J_DownArrow_X3(Chrome)"に上書きされる仕様

      {
        "description": "LeftCommand + J_DownArrow_X1(Chrome)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("j",["left_control"]) %>,
            "to": <%= to([["down_arrow"]]) %>,
            "conditions": [ <%= frontmost_application_if("chrome") %> ]

          }
        ]
      },
      {
        "description": "LeftCommand + J_DownArrow_X3(Chrome)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("j",["left_control"],["caps_lock"]) %>,
            "to": <%= to([["down_arrow"],["down_arrow"],["down_arrow"]]) %>,
            "conditions": [ <%= frontmost_application_if("chrome") %> ]

          }
        ]
      },
---------------------
## CapsLockがオンになってしまう

    {
      "description": "S_検索(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("s", ["caps_lock"]) %>,
          "to": <%= to([["l", ["right_gui"]],["caps_lock"]]) %>,
          "conditions": [ <%= frontmost_application_if("chrome") %> ]
        }
      ]
    },
---------------------
## Pararell　Rename一旦保留

{
          "description": "LeftControl_Rename(VirtualMachine)",
          "type": "basic",
          "from": {
            "apple_vendor_top_case_key_code":"keyboard_fn"
          },
          "to": [
            {
              "key_code": "return_or_enter"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.vmware.fusion$",
                "^com.vmware.horizon$",
                "^com.vmware.view$",
                "^com.parallels.desktop$",
                "^com.parallels.vm$",
                "^com.parallels.desktop.console$",
                "^org.virtualbox.app.VirtualBoxVM$",
                "^com.vmware.proxyApp.",
                "^com.parallels.winapp."
              ]
            }
          ]
        }
---------------------
## spacebar + j でDownArrow3回

      {
        "description": "使用できない-LeftCommand + J_DownArrow_X3(Chrome)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("j",["spacebar"],["caps_lock"]) %>,
            "to": <%= to([["down_arrow"],["down_arrow"],["down_arrow"]]) %>,
            "conditions": [ <%= frontmost_application_if("chrome") %> ]
          }
        ]
      },

---------------------
##  使用しない_LeftCommand + K_UpArrow_X3(Chrome)

      {
        "description": "使用しない-LeftCommand + K_UpArrow_X3(Chrome)",
        "manipulators": [
          {
            "type": "basic",
            "from": <%= from("k",["left_control"],["caps_lock"]) %>,
            "to": <%= to([["up_arrow"],["up_arrow"],["up_arrow"]]) %>,
            "conditions": [ <%= frontmost_application_if("chrome") %> ]
          }
        ]
      },

---------------------
## 使用しない-LeftCommand + h_LeftArrow-X3(kindle)

    {
      "description": "LeftCommand + h_LeftArrow-X3(kindle)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "h",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "left_arrow"
            },
            {
              "key_code": "left_arrow"
            },
            {
              "key_code": "left_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.amazon.Kindle$"
              ]
            }
          ]
        }
      ]
    },
    {
      "description": "LeftCommand + L_RigthArrow-X3(kindle)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "l",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "right_arrow"
            },
            {
              "key_code": "right_arrow"
            },
            {
              "key_code": "right_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com.amazon.Kindle$"
              ]
            }
          ]
        }
      ]
    }

---------------------
## Kindleアクティブキー、Macで設定しWindowsからよびだせるようにする。
---------------------
## 使用しない

{
      "description": "使用しない(予測変換で2度押しが必要になるため)_Spacebar(mi)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "spacebar",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "spacebar"
            }
],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^net.mimikaki.mi$"
              ]
            }
          ]
        }
      ]
},
{
      "description": "使用しない_Dainari_OpenCloseInput(mi)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("comma", ["left_shift"], ["caps_lock"]) %>,
          "to": <%= to([["japanese_eisuu"], ["comma", ["left_shift"]], ["period", ["left_shift"]], ["left_arrow"]]) %>,
          "conditions": [ <%= frontmost_application_if("mi") %> ]
        }
      ]
    },
    {
      "description": "RightCommand + J_1RowSelection_LeftArrow(mi)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("j", ["right_gui"]) %>,
          "to": <%= to([["a", ["left_control"]], ["down_arrow", "left_shift"], ["left_arrow", "left_shift"]]) %>,
          "conditions": [ <%= frontmost_application_if("mi") %> ]
        }
      ]
    }

---------------------
## 使用しない

    {
      "description": "使用しない_LeftCommand + J_DownArrow-X3(Chrome)",
      "manipulators": [
        {
          "type": "basic",
           "from": {
            "key_code": "j",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "down_arrow"
            },
            {
              "key_code": "down_arrow"
            },
            {
              "key_code": "down_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
    {
      "description": "使用しない_LeftCommand + k_UpArrow-X3(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "k",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "up_arrow"
            },
            {
              "key_code": "up_arrow"
            },
            {
              "key_code": "up_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
    {
      "description": "使用しない_LeftCommand + h_LeftArrow-X3(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "h",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "left_arrow"
            },
            {
              "key_code": "left_arrow"
            },
            {
              "key_code": "left_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
              "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
{
      "description": "使用しない_LeftCommand + L_RigthArrow-X3(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "l",
            "modifiers": {
              "mandatory": [
                "left_control"
              ],
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "right_arrow"
            },
            {
              "key_code": "right_arrow"
            },
            {
              "key_code": "right_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
              "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
{
  "description": "使用しない_英語モード:j_DownArrow(Chrome)",
  "_comment": "Chrome上で、検索窓に日本語入力ができなくなる欠点有り",
"manipulators": [
        {
          "type": "basic",
           "from": {
            "key_code": "j",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
      "to": [
            {
              "key_code": "down_arrow"
            }
      ],
      "conditions": [
        {
          "type": "input_source_if",
          "input_sources": [
            { "language": "en" }
          ]
        },
        {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
      ]
    }
  ]
},
{
  "description": "使用しない_英語モード:k_UpArrow(Chrome)",
  "_comment": "Chrome上で、検索窓に日本語入力ができなくなる欠点有り",
"manipulators": [
        {
          "type": "basic",
           "from": {
            "key_code": "k",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
      "to": [
            {
              "key_code": "up_arrow"
            }
      ],
      "conditions": [
        {
          "type": "input_source_if",
          "input_sources": [
            { "language": "en" }
          ]
        },
        {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
      ]
    }
  ]
},
{
  "description": "使用しない_英語モード:h_LeftArrow(Chrome)",
  "_comment": "Chrome上で、検索窓に日本語入力ができなくなる欠点有り",
"manipulators": [
        {
          "type": "basic",
           "from": {
            "key_code": "h",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
      "to": [
            {
              "key_code": "left_arrow"
            }
      ],
      "conditions": [
        {
          "type": "input_source_if",
          "input_sources": [
            { "language": "en" }
          ]
        },
        {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
      ]
    }
  ]
},
{
  "description": "使用しない_英語モード:L_LeftArrow(Chrome)",
  "_comment": "Chrome上で、検索窓に日本語入力ができなくなる欠点有り",
"manipulators": [
        {
          "type": "basic",
           "from": {
            "key_code": "l",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
      "to": [
            {
              "key_code": "right_arrow"
            }
      ],
      "conditions": [
        {
          "type": "input_source_if",
          "input_sources": [
            { "language": "en" }
          ]
        },
        {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
      ]
    }
  ]
}

---------------------
## 今は使わない

    {
        "description": "今は使わない_Double F1_tmp.py(Single)_tmp.md[Double](FunctionKey)",
        "_comment": "ダブル押しコードでの、「frontmost_application_unless(pararell)」の書き方が分からないので、Single押しでの処理を使うことにする。",
        "manipulators": [
            {
                "type": "basic",
                "from": {
                    "key_code": "f1",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "shell_command": "open '/Users/user/Desktop/iCollections/Folder2/Verification/tmp.md'"
                    }
                ],
                "conditions": [
                    {
                        "type": "variable_if",
                        "name": "f1 pressed",
                        "value": 1
                    }
                ]
            },
            {
                "type": "basic",
                "from": {
                    "key_code": "f1",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "set_variable": {
                            "name": "f1 pressed",
                            "value": 1
                        }
                    },
                    {
                        "shell_command": "open '/Users/user/Desktop/iCollections/Folder2/Verification/tmp.py'"
                    }
                ],
                "to_delayed_action": {
                    "to_if_invoked": [
                        {
                            "set_variable": {
                                "name": "f1 pressed",
                                "value": 0
                            }
                        }
                    ],
                    "to_if_canceled": [
                        {
                            "set_variable": {
                                "name": "f1 pressed",
                                "value": 0
                            }
                        }
                    ]
                }
            }
        ]
    },

---------------------
## 今は使わない

{
  "description": "F3_KeyManageList.xlsxOpen(FunctionKey)",
  "manipulators": [
    {
      "type": "basic",
      "from": <%= from("f3") %>,
      "to": <%= set_shell_command(["open '/Users/user/Dropbox/KeyCustomization/KeyManageList.xlsm'"]) %>
    }
  ]
},

---------------------
## うまくいかない

    {
        "description": "うまくいかない、Double F1_tmp.py(Single)_tmp.md[Double](FunctionKey)",
        "manipulators": [
            {
                "type": "basic",
                "from": {
                    "key_code": "f1",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "shell_command": "open '/Users/user/Desktop/iCollections/Folder2/Verification/tmp.md'"
                    }
                ],
                "conditions": [
                    {
                        "type": "variable_if",
                        "name": "f1 pressed",
                        "value": 1
                    },
                                {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^com.vmware.fusion$",
                "^com.vmware.horizon$",
                "^com.vmware.view$",
                "^com.parallels.desktop$",
                "^com.parallels.vm$",
                "^com.parallels.desktop.console$",
                "^org.virtualbox.app.VirtualBoxVM$",
                "^com.vmware.proxyApp.",
                "^com.parallels.winapp."
              ]
            }
                ]
            },
            {
                "type": "basic",
                "from": {
                    "key_code": "f1",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "set_variable": {
                            "name": "f1 pressed",
                            "value": 1
                        }
                    },
                    {
                        "shell_command": "open '/Users/user/Desktop/iCollections/Folder2/Verification/tmp.py'"
                    }
                ],
                "to_delayed_action": {
                    "to_if_invoked": [
                        {
                            "set_variable": {
                                "name": "f1 pressed",
                                "value": 0
                            }
                        }
                    ],
                    "to_if_canceled": [
                        {
                            "set_variable": {
                                "name": "f1 pressed",
                                "value": 0
                            }
                        }
                    ]
                }
            }
        ]
    }
---------------------
## 使用しない

{
      "description": "使用しないEnter_OpenFile(pathfinder)",
      "_comment": "ファイル名変更でエンターで確定できない為",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("return_or_enter") %>,
          "to": <%= to([["o", ["right_gui"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pathfinder") %> ]
        }
      ]
    },
    {
      "description": "使用しない_delete_FileDelete(pathfinder)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("delete_or_backspace") %>,
          "to": <%= to([["delete_or_backspace", ["right_gui"]]]) %>,
          "conditions": [ <%= frontmost_application_if("pathfinder") %> ]
        }
      ]
    }

---------------------
## 使用しない


{
      "description": "使用しない_LeftAlt + F11_VBAeditor(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("f11", ["left_alt"]) %>,
          "to": <%= to([["f11", ["left_alt"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
{
      "description": "使用しない_Marukako_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("9", ["left_shift"]) %>,
          "to": <%= to([["9", ["left_shift"]], ["0", ["left_shift"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
   {
      "description": "使用しない_Namikako_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("open_bracket", ["left_shift"]) %>,
          "to": <%= to([["open_bracket", ["left_shift"]], ["close_bracket", ["left_shift"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
   {
      "description": "使用しない_Kakukako_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("open_bracket") %>,
          "to": <%= to([["open_bracket"], ["close_bracket"]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
   {
      "description": "使用しない_Dainari_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("comma", ["left_shift"]) %>,
          "to": <%= to([["comma", ["left_shift"]], ["period", ["left_shift"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
   {
      "description": "使用しない_DoubleQuote_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("quote", ["left_shift"]) %>,
          "to": <%= to([["quote", ["left_shift"]], ["quote", ["left_shift"]]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
   {
      "description": "使用しない_SingleQuote_OpenCloseInput(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("quote") %>,
          "to": <%= to([["quote"], ["quote"]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    },
    {
      "description": "使用しないLeftAlt_Copy(Excel)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "left_alt",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "left_alt"
            }
          ],
          "to_if_alone": [
            {
              "key_code": "left_alt",
              "modifiers": "left_gui"
            }
          ],
	  "conditions": [
		{
		  "type": "frontmost_application_if",
		  "bundle_identifiers": [
		    "^com\\.microsoft\\.Excel$"
		  ]
		}
	      ]
        }
      ]
    },
	 {
      "description": "使用しない_RightCommand + J_Select1Row(Excel)VBEでのみ使用可能",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("j", ["right_gui"]) %>,
          "to": <%= to([["left_arrow", ["fn"]], ["down_arrow", "left_shift"]]) %>,
          "conditions": [ <%= frontmost_application_if("excel") %> ]
        }
      ]
    }
 ---------------------
## 使用しない

    {
      "description": "適用しない_Delete_NoteDelete(Evernote)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("delete_or_backspace") %>,
          "to": <%= to([["delete_or_backspace", ["right_gui"]]]) %>,
          "conditions": [ <%= frontmost_application_if("evernote") %> ]
        }
      ]
    }
---------------------
## 「frontmost_chrome.json.erb_L」キー、RightArrow設定、

    {
      "description": "L_RightArrow(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": <%= from("l", ["caps_lock"]) %>,
          "to": <%= to([["right_arrow"]]) %>,
          "conditions": [ <%= frontmost_application_if("chrome") %> ]
        }
      ]
    },
---------------------
## mandatoryを無しで「key_code」単独で、「caps_lock」を設定したい場合

下記のような書き方はできない。
"from": <%= from("a", ["left_control"]) %>,


下記のような書き方が必要。
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "fn",
            "modifiers": {
              "optional": [
                "caps_lock"
              ]
            }
          },

---------------------
## CapsLocker、起動時にChrome上でCapsLockオン時に「j」キーを押すごとに、CapsLockerのアイコンが表示されることの対策検討

結果:うまくいかなかった。
Capslockオン時に、「j」キーで、CapsLockerのアイコンが表示されてしまう。

```
    {
      "description": "J_DownArrow_改良1_1(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "j"
          },
          "to": [
            {
              "key_code": "down_arrow"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
    {
      "description": "J_DownArrow改良1_2(Chrome)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "j",
            "modifiers": {
              "mandatory": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "j"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.google\\.Chrome$"
              ]
            }
          ]
        }
      ]
    },
```

---------------------
## replacekey.json.erb

    {
      "description": "RightCommand + Z,X,C,V,S,D,F,W,E,R_Number0~9_簡易版(Replacekey)",
      "manipulators":
      <%= each_key(
            source_keys_list: ["z", "x", "c", "v", "s", "d", "f", "w", "e", "r"],
            from_mandatory_modifiers: ["right_gui"],
            from_optional_modifiers: ["caps_lock"],
            dest_keys_list: [["japanese_eisuu", "0"], ["japanese_eisuu", "1"], ["japanese_eisuu", "2"], ["japanese_eisuu", "3"], ["japanese_eisuu", "4"], ["japanese_eisuu", "5"], ["japanese_eisuu", "6"], ["japanese_eisuu", "7"], ["japanese_eisuu", "8"], ["japanese_eisuu", "9"]],
            as_json: true,
          ) %>
    },
        {
      "description": "RightCommand + Z,X,C,V,S,D,F,W,E,R_Number0~9_詳細版(Replacekey)",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "z",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "0"
            }
          ],
                    "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^com.parallels.desktop.console$",
                "^com.parallels.winapp.b06b57f82d7f519cdfa3013b29968f3d.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.7d56d4002964a683f165ae699d4ad1ba.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.d51a768a01445deddc409dc4b3c07517.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.c1d81af5835844b4e9d936910ded8fdc.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.2d457b859f61df5cdc0ae605436482d3.b9dc48efd5094ca8a69c0e98f2ecf717.fs$",
                "^com.parallels.winapp.bf733d8a933c1601697f364223fc7ecb.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.f900d466e8ca2c668fa8844e6e5205f3.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.ee162c85923f5664be0dcc14062cc904.b9dc48efd5094ca8a69c0e98f2ecf717$",
                "^com.parallels.winapp.5f30debe0c2949158e0cff8dc0684bbb.b9dc48efd5094ca8a69c0e98f2ecf717$"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "x",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "1"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "c",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "2"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "v",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "3"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "s",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "4"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "d",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "5"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "f",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "6"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "w",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "7"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "e",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "8"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "r",
            "modifiers": {
              "mandatory": [
                "right_gui"
              ],
              "optional": [
                "caps_lock"
              ]
            }
          },
          "to": [
            {
              "key_code": "japanese_eisuu"
            },
            {
              "key_code": "9"
            }
          ]
        }
      ]
    },

---------------------
## replacekey.json.erb

        {
      "description": "LeftCommand + H/J/K/L_Arrows(Replacekey)",
      "manipulators":
      <%= each_key(
            source_keys_list: ["h", "j", "k", "l"],
            from_mandatory_modifiers: ["left_control"],
            from_optional_modifiers: ["any"],
            dest_keys_list: ["left_arrow", "down_arrow", "up_arrow", "right_arrow"],
            as_json: true,
          ) %>
        },

---------------------
ConstScrollDown,ConstScrollUp(保留)

{
  "description": "RightAlt + J_ConstScrollDown",
  "type": "basic",
  "from": <%= from("j", ["right_alt"], ["caps_lock"]) %>,
  "to": <%= to([["e", ["left_control"]]]) %>,
  "conditions": [ <%= frontmost_application_unless("virtual_machine") %> ]
},
{
  "description": "RightAlt + K_ConstScrollUp",
  "type": "basic",
  "from": <%= from("k", ["right_alt"], ["caps_lock"]) %>,
  "to": <%= to([["y", ["left_control"]]]) %>,
  "conditions": [ <%= frontmost_application_unless("virtual_machine") %> ]
},

---------------------