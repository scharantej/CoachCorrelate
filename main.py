
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create a Flask application instance
app = Flask(__name__)

# Database configuration
DATABASE = 'nba.db'

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Close the database connection
def close_connection(conn):
    if conn:
        conn.close()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Add a player
@app.route('/add_player', methods=['POST'])
def add_player():
    conn = get_db_connection()
    name = request.form['name']
    team = request.form['team']
    injury_history = request.form['injury_history']
    conn.execute('INSERT INTO players (name, team, injury_history) VALUES (?, ?, ?)', (name, team, injury_history))
    conn.commit()
    close_connection(conn)
    return redirect('/')

# Add a coach
@app.route('/add_coach', methods=['POST'])
def add_coach():
    conn = get_db_connection()
    name = request.form['name']
    coaching_style = request.form['coaching_style']
    team_history = request.form['team_history']
    conn.execute('INSERT INTO coaches (name, coaching_style, team_history) VALUES (?, ?, ?)', (name, coaching_style, team_history))
    conn.commit()
    close_connection(conn)
    return redirect('/')

# Add a coaching action
@app.route('/add_coaching_action', methods=['POST'])
def add_coaching_action():
    conn = get_db_connection()
    coach_name = request.form['coach_name']
    action = request.form['action']
    date = request.form['date']
    conn.execute('INSERT INTO coaching_actions (coach_name, action, date) VALUES (?, ?, ?)', (coach_name, action, date))
    conn.commit()
    close_connection(conn)
    return redirect('/')

# Add a game result
@app.route('/add_game_result', methods=['POST'])
def add_game_result():
    conn = get_db_connection()
    team1 = request.form['team1']
    team2 = request.form['team2']
    winner = request.form['winner']
    loser = request.form['loser']
    injuries = request.form['injuries']
    conn.execute('INSERT INTO game_results (team1, team2, winner, loser, injuries) VALUES (?, ?, ?, ?, ?)', (team1, team2, winner, loser, injuries))
    conn.commit()
    close_connection(conn)
    return redirect('/')

# Show all data
@app.route('/show_data')
def show_data():
    conn = get_db_connection()
    players = conn.execute('SELECT * FROM players').fetchall()
    coaches = conn.execute('SELECT * FROM coaches').fetchall()
    coaching_actions = conn.execute('SELECT * FROM coaching_actions').fetchall()
    game_results = conn.execute('SELECT * FROM game_results').fetchall()
    close_connection(conn)
    return render_template('index.html', players=players, coaches=coaches, coaching_actions=coaching_actions, game_results=game_results)

# Show charts
@app.route('/charts')
def charts():
    conn = get_db_connection()
    coaching_styles = conn.execute('SELECT DISTINCT coaching_style FROM coaches').fetchall()
    coaching_styles_injury_load = {}
    for coaching_style in coaching_styles:
        injury_load = conn.execute('SELECT AVG(injury_history) FROM players WHERE team IN (SELECT team FROM coaches WHERE coaching_style = ?)', (coaching_style['coaching_style'],)).fetchone()
        coaching_styles_injury_load[coaching_style['coaching_style']] = injury_load[0]
    team_success = conn.execute('SELECT team, AVG(winner) AS win_percentage FROM game_results GROUP BY team ORDER BY win_percentage DESC').fetchall()
    close_connection(conn)
    return render_template('index.html', coaching_styles_injury_load=coaching_styles_injury_load, team_success=team_success)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
