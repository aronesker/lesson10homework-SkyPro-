import utils
from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    page_content = ""
    candidates = utils.load_candidates()
    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"
    return "<pre>"+page_content+"</pre>"

@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = utils.get_candidate_by_id(uid)
    page_content = f"<img src={candidate['picture']}" + "\n"
    page_content += "<pre>"
    page_content += f"{ candidate['name']}" + "\n"
    page_content += f"{ candidate['position']}" + "\n"
    page_content += f"{ candidate['skills']}" + "\n"
    page_content += "</pre>"
    return page_content

@app.route("/skill/<skill>")
def page_skill(skill):
    candidates = utils.get_candidates_by_skill(skill)
    page_content = ""

    for candidate in candidates:
        page_content += f"{candidate['name']}" + "\n"
        page_content += f"{candidate['position']}" + "\n"
        page_content += f"{candidate['skills']}" + "\n"

   return "<pre>" + page_content + "</pre>"

app.run()