#!/usr/bin/python
import sys
import os

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