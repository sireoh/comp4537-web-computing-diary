from flask import Flask, render_template
import markdown
from pathlib import Path

app = Flask(__name__, static_folder="imgs", static_url_path="/imgs")


@app.route("/")
def __index():
    md_text = Path("markdown/index.md").read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    return render_template("layout.html", content=html)


@app.route("/midterm")
def __midterm():
    md_text = Path("markdown/content_midterm.md").read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    return render_template("layout.html", content=html)


@app.route("/final")
def __final():
    md_text = Path("markdown/content_final.md").read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    return render_template("layout.html", content=html)


if __name__ == "__main__":
    app.run(debug=True, port=6842)
