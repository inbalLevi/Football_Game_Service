from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)
result_played = pd.read_csv("result_played.csv")
result_upcoming = pd.read_csv("result_upcoming.csv")


def get_by_team(result_played, team_name):
    # This method returns list of matched by team and converting it to JSON format
    return result_played.loc[
        (result_played['home_team'] == team_name) | (result_played['away_team'] == team_name)].to_json(
        orient="records", indent=4)


def get_by_tournament(df, tournament):
    # This method returns list of matched by tournament and converting it to JSON format
    return df.loc[(df['tournament'] == tournament)].to_json(orient="records", indent=4)


@app.route('/matchesByTeamAndStatus', methods=["GET"])
def matchesByTeamAndStatus():
    team_name = request.args.get('team')
    status = request.args.get('status')

    if (status == "played"):
        return get_by_team(result_played, team_name)
    if(status=="upcoming"):
        return get_by_team(result_upcoming, team_name)

@app.route('/matchesByTournamentAndStatus', methods=["GET"])
def matchesByTournamentAndStatus():
    tournament = request.args.get('tournament')
    status = request.args.get('status')

    if (status == "played"):
        return get_by_tournament(result_played, tournament)
    if(status=="upcoming"):
        return get_by_tournament(result_upcoming, tournament)

@app.route('/matchesByTeam', methods=["GET"])
def matchesByTeam():
    team_name = request.args.get('team')
    played_by_team_json = get_by_team(result_played, team_name)
    upcoming_by_team_json = get_by_team(result_upcoming, team_name)

    playedJson = json.loads(played_by_team_json)
    upcomingJson = json.loads(upcoming_by_team_json)
    merged = playedJson + upcomingJson
    return json.dumps(merged)


@app.route('/matchesByTournament', methods=["GET"])
def matchesByTournament():
    tournament = request.args.get('tournament')

    played_by_tournament_json = get_by_tournament(result_played, tournament)
    upcoming_by_tournament_json = get_by_tournament(result_upcoming, tournament)
    playedJson = json.loads(played_by_tournament_json)
    upcomingJson = json.loads(upcoming_by_tournament_json)
    merged = playedJson + upcomingJson
    return json.dumps(merged)

@app.errorhandler(404) # error handling, in case URL input isn't valid
def page_not_found(e):
    return "Page not found"

@app.errorhandler(500) # error handling, in case user URL params aren't valid
def page_not_found(e):
    return "Invalid parameters"


if __name__ == "__main__":
    app.run()


