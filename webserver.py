from flask import Flask, render_template
from db_connect import DatabaseConnection
import plotly.graph_objects as go
import plotly.utils
import json

app = Flask(__name__)


@app.route("/")
def home():
    db = DatabaseConnection()
    body_temps = db.get_all_body_temps()
    room_temps = db.get_all_room_temps()
    db.close()

    # Create a Plotly figure
    fig1 = go.Figure(
        data=go.Scatter(
            x=[temp[0] for temp in body_temps], y=[temp[1] for temp in body_temps]
        )
    )
    fig2 = go.Figure(
        data=go.Scatter(
            x=[temp[0] for temp in room_temps], y=[temp[1] for temp in room_temps]
        )
    )

    figs = {
        "body_temp": json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder),
        "room_temp": json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder),
    }

    return render_template("home.html", figures=figs)


def start_webserver():
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=False)
