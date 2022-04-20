#!/usr/bin/env python3


import json
import os.path


if __name__ == "__main__":
    print("Generating grammar configuration...")

    grammars = {
        "html": "text.html.basic",
        "css": "source.css",
        "less": "source.css.less",
        "vue": "text.html.vue-html",
        "json": "source.json",
        "yaml": "source.yaml",
        "xml": "text.xml",
        "xsl": "text.xml.xsl",
        "ini": "source.ini",
        "handlebars": "text.html.handlebars",
        "md": "text.html.markdown",
        "pug": "text.pug",
        "scss": "source.css.scss",
        "sql": "source.sql"
    }

    grammar = {
        "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",

        "name": "Javascript Embeded Block",
        "scopeName": "source.javascript.embeded-block",

        "injectionSelector": ", ".join([
            "L:source.js -comment -string",
            "L:source.jsx -comment -string",
            "L:source.ts -comment -string",
            "L:source.tsx -comment -string"
        ]),

        "patterns": [
            {
                "begin": "(\\${)",
                "end": "(})",
                "beginCaptures": {
                    "1": {
                        "name": "entity.name.tag"
                    }
                },
                "endCaptures": {
                    "1": {
                        "name": "entity.name.tag"
                    }
                },
                "patterns": [
                    {
                        "include": "source.js"
                    }
                ]
            }
        ]
    }

    for name, scope in grammars.items():
        print(f" - {name}: {scope}")

        grammar["patterns"].append({
            "begin": "([^*](" + name + ")|(\\/\\*" + name + "\\*\\/))(\\`(?:[^`\\\\]|\\\\.)*)",
            "beginCaptures": {
                "1": {
                    "name": "string.quoted.other.template.js"
                },
                "2": {
                    "name": "support.function"
                },
                "3": {
                    "name": "comment.block"
                },
                "4": {
                    "patterns": [
                        {
                            "include": scope
                        }
                    ]
                }
            },
            "end": "(\\`)",
            "endCaptures": {
                "1": {
                    "name": "string.quoted.other.template.js"
                }
            },
            "patterns": [
                {
                    "include": scope
                },
                {
                    "include": "string.quoted.other.template.js"
                }
            ]
        })

    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "grammars", "embeded.json")

    with open(path, "w") as file:
        json.dump(grammar, file, indent=2)

    print("Done!")
