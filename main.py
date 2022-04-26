from flask import Flask, render_template, abort
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страница"""
    candidates = utils.load_candidates_from_json("candidates.json")
    print(candidates)
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id):
    """Страница кандидата"""
    candidates = utils.load_candidates_from_json("candidates.json")
    candidate = utils.get_candidate(candidates, candidate_id)
    if candidate is None:
        abort(404)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def candidate_name_page(candidate_name):
    """Страница найденных кандидатов по имени"""
    candidates = utils.load_candidates_from_json("candidates.json")
    candidates_founded = utils.get_candidates_by_name(candidates, candidate_name)
    return render_template("search.html", candidates=candidates_founded, count=len(candidates_founded))


@app.route("/skill/<skill_name>")
def candidate_skill_page(skill_name):
    """Страница найденных кандидатов по навыкам"""
    candidates = utils.load_candidates_from_json("candidates.json")
    candidates_founded = utils.get_candidates_by_skill(candidates, skill_name)
    return render_template("skill.html", candidates=candidates_founded, skill_name=skill_name)


app.run()
