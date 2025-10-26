from flask import Flask, render_template
import markdown
from pathlib import Path

app = Flask(__name__, static_folder="imgs", static_url_path="/imgs")


@app.route("/")
def index():
    md_text = Path("app/content.md").read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    return render_template("layout.html", content=html)


if __name__ == "__main__":
    app.run(debug=True, port=6842)
