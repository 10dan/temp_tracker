from flask import Flask, render_template
from db_connect import DatabaseConnection
import plotly.graph_objects as go
import plotly.utils
import json

app = Flask(__name__)


@app.route('/')
def home():
    db = DatabaseConnection()
    temps = db.get_all_temps()
    db.close()

    # Create a Plotly figure
    fig = go.Figure(data=go.Scatter(x=[temp[0] for temp in temps], y=[temp[1] for temp in temps]))

    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('home.html', temperatures=temps, fig_json=fig_json)



def start_webserver():
    app.run(debug=True, host="0.0.0.0",port=5001, use_reloader=False)
