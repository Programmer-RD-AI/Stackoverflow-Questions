from flask import *

app = Flask(__name__)
app.debug = True
app.secret_key = "testing"

def change_terms(terms):
    new_terms = {}
    for term_key,term_val in zip(terms.keys(), terms.values()):
        new_term_vals = ""
        for new_term_val in term_val:
            new_term_vals += new_term_val + ","
        print(new_term_vals)
        new_term_vals = "[" + new_term_vals + "]"
        new_terms[term_key] = new_term_vals
    print(new_terms)
    return new_terms
        
@app.route("/")
def index():
    terms = {"a": ["1", "2", "3"], "b": ["4", "5", "6"], "c": ["x", "y", "z"]}
    terms = change_terms(terms)
    return render_template("index.html", terms=terms)


if __name__ == "__main__":
    app.run()
