"""
Exercise #1: Top movies
"""

from flask import Flask, render_template, g
import mysql.connector
app = Flask(__name__)

app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "dat310"
app.config["DATABASE_HOST"] = "localhost"
app.debug = True  # only for development!

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                       password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database

@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()




@app.route("/")
def index():
    db = get_db()
    cur = db.cursor()
    try:
        sql = ("SELECT imdb_id, title, year, rating, synopsis FROM movies")
        cur.execute(sql)
        print(cur)
        MOVIES=[]
        for (imdb_id, title, year, rating, synopsis) in cur:
            MOVIES.append({ "title":title,
                            "year": year,
                            "url": "http://www.imdb.com/title/"+imdb_id,
                            "rating": rating,
                            "synopsis": synopsis})
        render_template("movies.html", movies=MOVIES)
    except mysql.connector.Error as e:
        print("Error: {}".format(e.msg))
    finally:
        cur.close()
    return render_template("movies.html", movies=MOVIES)


if __name__ == "__main__":
    app.run()
