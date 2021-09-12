#!/usr/bin/python
import sys
import os

JS_KEYWORDS = set(["await", "break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function", "if", "implements", "import", "in", "instanceof", "interface", "let", "new", "package", "private", "protected", "public", "return", "super", "switch", "static", "this", "throw", "try", "True", "typeof", "var", "void", "while", "with", "yield"])
JS_WEIRD_VALS = set(["null", "undefined", "NaN"])

############## Methods to get HTML tag for data type
def genCommentItem(word):
    return """
    <span class='code-editor-comment'>{comment}</span>
    """.format(comment = word)

def genSpaceItem():
    return """
    <span class='code-editor-space'> </span>
    """
def genBooleanItem(word):
    return """
    <span class='code-editor-bool'>{boolean}</span>
    """.format(boolean=word)

def genWeirdValItem(word):
    return """
    <span class='code-editor-weird-val'>{weird}</span>
    """.format(weird=word)

def genKeywordItem(word):
    return """
    <span class='code-editor-comment'>{keyword}</span>
    """.format(keyword=word)

def genNumberItem(word):
    return """
    <span class='code-editor-number'>{num}</span>
    """.format(num=word)

def genNormalItem(word):
    return """
    <span class='code-editor-normal'>{word}</span>
    """.format(word=word)
##############

############## Methods to check data type
def isJSString(word):
    starting_char = word[0]
    ending_char = word[len(word) - 1]

    return len(word) >= 2 and (
            (starting_char == "\"" and ending_char == "\"") or 
            (starting_char == "'" and ending_char == "'") or 
            (starting_char == "`" and ending_char == "`"))

def isJSBoolean(word):
    return word == "true" or word == "false"

def isJSNumber(word):
    # check for BigInt
    if(word[-1] == "n"):
        return word[0: len(word) - 1].isnumeric()
    return word.isnumeric()

def isJSKeyword(word):
    return word in JS_KEYWORDS

def isJSWeirdVal(word):
    return word in JS_WEIRD_VALS
##############

def addLineContent(line):
    # TODO add parsing. For now, just wrapping in normal tag
    rtr = ""

    for c in line:
        if(c != " "):
            break
        rtr += genSpaceItem()+"\n"
    return rtr + genNormalItem(line)
    
def addLine(line_indx, line):
    return """
        <div class="code-editor-line">
            <span class="code-editor-line-index">{indx}</span>
            {content}
        </div> 
    """.format(indx = line_indx + 1, content=addLineContent(line))

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
            <div id="console">
            <!--- TODO --->
            </div>
        </div>
    """.format(code_lines_html = " ".join(code_lines_html), online_editor_link = online_editor_link)

def saveToFile(raw, file_name):
    file = open(os.path.abspath("temp/" + file_name), "w+")
    file.write(raw)
    file.close()

def main():
    if(len(sys.argv) != 4):
        raise Exception("Missing args")
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    online_editor_uri = sys.argv[3]

    file = open(os.path.abspath("examples/" + input_file_name))
    lines = file.read().split("\n")

    code_lines = []
    for i in range(len(lines)):
        line = lines[i]
        code_lines.append(addLine(i,line))
    saveToFile(genCodeEditor(code_lines, online_editor_uri), output_file_name)
    file.close()

if __name__ == "__main__":
    main()