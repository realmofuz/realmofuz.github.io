import mistune
import os
# This python file is responsible for transforming Xyraith's Markdown documentation
# into UZB website styled HTML files.


def processFile(file_name: str) -> str:
    file_text = open(file_name).read()
    processed_text = file_text
    raw_html = (mistune.html(processed_text)
            .replace("<code>", "<pre><code>")
            .replace("</code>", "</pre></code>"))
    return (open(f"{os.getcwd()}/xyraith/docs/template.html").read()
                .replace("%{{contents}}%", raw_html))

def processAllFiles():
    for index in range(1, 100000):
        try:
            html = processFile(f"{os.getcwd()}/xyraith/md/{index}.md")
            open(f"{os.getcwd()}/xyraith/docs/{index}.html", "w+").write(html)
        except FileNotFoundError:
            print(f"Reached end at index {index}")
            return

processAllFiles()