## ExcelのleftOptionやrightOptionキー単独押しアクセシビリティキーが表示されるようになった改善方法(2026/04/06)

### 結論

to_if_alone" を削除すれば良い

```
                {
                    "description": "LeftAlt_Copy(Replacekey)",
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
                              "^com\\.microsoft\\.Excel$"
                            ]
                        }
                    ]
                },
```

↓

```
                {
                    "description": "LeftAlt_Copy(Replacekey)",
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
                            "key_code": "c",
                            "modifiers": "right_gui"
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
                },
```