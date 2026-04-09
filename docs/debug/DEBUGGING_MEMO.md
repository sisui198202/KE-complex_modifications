## ExcelのleftOptionやrightOptionキー単独押しアクセシビリティキーが表示されるようになった改善方法(2026/04/09)

### 結論

"lazy": true

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

↓ ## Excelのleftalt単独押しで、コピーできない_解決策:"lazy": true

```
                {
                    "description": "LeftAlt_Copy_1回押しOK_lazy-true(Excel)",
                    "type": "basic",
                    "from": {
                        "key_code": "left_alt"
                    },
                    "to": [
                        {
                        "key_code": "left_alt",
                        "lazy": true
                        }
                    ],
                    "to_if_alone": [
                        {
                        "key_code": "c",
                        "modifiers": ["right_gui"]
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
```