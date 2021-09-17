# football_game_service


This project provides a football game service which allows the client to get the fixtures (upcoming matches) and the results of football matches from 2 csv files:

result_played.csv
result_upcoming.csv
The restful api service is running on port 5000.
The system provides 4 different methods:
• Get a list of matches by team
• Get a list of matches by team & status (played/upcoming)
• Get a list of matches by tournament
• Get a list of matches by tournament filtered by status


Instructions:
1.Open cmd
2.Navigate to project directory
3ץ Run: python football_server.py
4.Open browser and navigate to http://localhost:5000


To get list of matches by team enter url: http://localhost:5000/matchesByTeam?team=<team_name> 

To get list of matches by team filtered by status enter url: http://localhost:5000/matchesByTeamAndStatus?team=<team_name>&status=<status>

To get list of matches by tournament enter url: http://localhost:5000/matchesByTournament?tournament=<tournament> 

To get list of matches by tournament filtered by status enter url: http://localhost:5000/matchesByTournamentAndStatus?tournament=<tournament>&status=<status>


Running examples:
To get list of matches of "Barnsley" team: http://localhost:5000/matchesByTeam?team=Barnsley
To get list of matches of "Burnley" team filtered by status "upcoming": http://localhost:5000/matchesByTeamAndStatus?team=Burnley&status=upcoming
To get list of matches of "premier-league" tournament http://localhost:5000/matchesByTournament?tournament=premier-league
To get list of matches of "premier-league" tournament filtered by status "played": http://localhost:8080/matchesByTournamentAndStatus?tournament=premier-league&status=played


Result:
Please see result on the web browser which contains the response for the "get" request in json format.

