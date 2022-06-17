# TableauReportGenerator

This python script executes command prompt commands to run tabcmd commands in the terminal

Generates pdf reports of your tableau sheet

The Current logic creates reports based off a primary filter and respective secondary filter for each year and month run and is set up where your primary filter contains a list of secondary filters.

## <em>Example Use:</em> 

Generate player stats for the list of sports teams in a league. In this example, a sheet is set up in Tableau that contains the stats of all the players for each team. Only one player is shown on the view at a time. The Primary Filter is the teams in the database and the Secondary Filter is the players in the database. A list of players on each team needs to be added into the script for each team before use.

<em>Note: Must install Tabcmd prior to running the script</em> https://help.tableau.com/current/server/en-us/tabcmd.htm 
<em>Fill in account information to connect to your online Tableau account</em>
