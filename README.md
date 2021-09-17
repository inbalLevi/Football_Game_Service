# football_game_service


This project provides a football game service which allows the client to get the fixtures (upcoming matches) and the results of football matches from 2 csv files:</br>
result_played.csv </br>
result_upcoming.csv </br>
The restful api service is running on port 5000. </br>
The system provides 4 different methods: </br>
• Get a list of matches by team </br>
• Get a list of matches by team & status (played/upcoming) </br>
• Get a list of matches by tournament </br>
• Get a list of matches by tournament filtered by status </br>


## Instructions: </br>
1.Open cmd </br>
2.Navigate to project directory </br>
3ץ Run: python football_server.py </br>
4.Open browser and navigate to http://localhost:5000 </br> 


To get list of matches by team enter url:
http://localhost:5000/matchesByTeam?team=<team_name> </br> 

To get list of matches by team filtered by status enter url:
http://localhost:5000/matchesByTeamAndStatus?team=<team_name>&status=<status> 

To get list of matches by tournament enter url:
http://localhost:5000/matchesByTournament?tournament=<tournament>  </br>

To get list of matches by tournament filtered by status enter url:
http://localhost:5000/matchesByTournamentAndStatus?tournament=<tournament>&status=<status> 


## Running examples: </br>
To get list of matches of "Barnsley" team: http://localhost:5000/matchesByTeam?team=Barnsley </br>
To get list of matches of "Burnley" team filtered by status "upcoming": http://localhost:5000/matchesByTeamAndStatus?team=Burnley&status=upcoming </br>
To get list of matches of "premier-league" tournament: http://localhost:5000/matchesByTournament?tournament=premier-league </br>
To get list of matches of "premier-league" tournament filtered by status "played": http://localhost:8080/matchesByTournamentAndStatus?tournament=premier-league&status=played </br>


## Result: </br>
Please see result on the web browser which contains the response for the "get" request in json format. </br>

