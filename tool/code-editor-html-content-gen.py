#!/usr/bin/python
import sys
import os

JS_KEY_WORDS = set(["await", "break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function", "if", "implements", "import", "in", "instanceof", "interface", "let", "new", "null", "package", "private", "protected", "public", "return", "super", "switch", "static", "this", "throw", "try", "True", "typeof", "var", "void", "while", "with", "yield"])

def genSpaceItem():
    return

def genWeirdValItem():
    return

def genKeywordItem():
    return

def genNumberItem():
    return

def addLine(line_indx):
    return """
        <div class="code-editor-line">
            <span class="code-editor-line-index">{indx}</span>
        </div> 
    """.format(indx = line_indx + 1)

def genCodeEditor(code_lines_html, online_editor_link):
    return """
        <div id="code-container">
            <div id="code-editor">
                <div id="code-editor-top-button-container">
                    <a href='./'>
                        <div class="code-editor-top-button" id="code-editor-close-button"></div>
                    </a>
                    <a href='./'>
                        <div class="code-editor-top-button" id="code-editor-minimize-button"></div>
                    </a>
                    <a target="_blank" href="{online_editor_link}">
                        <div class="code-editor-top-button" id="code-editor-expand-button"> </div>
                    </a>
                </div>
                <div id="code-editor-content">
                    {code_lines_html}
                </div>
            </div>
        </div>
    """.format(code_lines_html = " ".join(code_lines_html), online_editor_link = online_editor_link)

def main():
    if(len(sys.argv) != 2):
        raise Exception("Need file name")
    file_name = sys.argv[1]
    file = open(os.path.abspath("examples/" + file_name))
    lines = file.read().split("\n")

    code_lines = []
    for i in range(len(lines)):
        _line = lines[i]
        code_lines.append(addLine(i))
    print(genCodeEditor(code_lines, "#"))
    file.close()

if __name__ == "__main__":
    main()