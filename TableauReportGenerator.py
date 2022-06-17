#Author: Brian Busco
#Date: 6/2/2022

# Imports library needed to run the powershell commands from python
import subprocess

# This is the filepath where your tabcmd utility tool needs to be installed on your computer
tabcmdFilePath = "C:\\Program Files\\Tableau\\Tableau Server\\2022.1\\extras\\Command Line Utility"

# Here you can change the username, password, server needed to connect, and site on the server 
server = "https://online.tableau.com"
site = ""
username = ""
password = ""

# This is the command that establishes the connection to the tableau server
subprocess.run('tabcmd login -s ' + server + ' -t '+ site + ' -u '+ username +' -p '+ password +'', cwd=tabcmdFilePath, shell=True)

# These are the variables that will be used to create the file name
# Change the month and the year below to the month and year you wish to generate the reports for
# The month variable here will not change the filter in Tableau
month = ""
year = ""

# This is the filepath where you will save all the reports 
# Note: You will need to create a directory for every Primary Filter before you can run the program otherwise you will receive an error message based off current saving logic
rootFilePath = "C:\\Reports"

# Path to where this script is pulling data from Tableau
# Find this path on your tableau online sheet location
pathToSheet = ""

# The code below creates a list of Secondary Filters for each Primary Filter
primaryFilter1List = ["secondaryFilter1 secondaryFilter2"]
primaryFilter2List = ["secondaryFilter2 secondaryFilter4 secondaryFilter5"]

# Creates a dictionary where the key = the Primary Filter and the value = the list of Secondary Filters the respective Primary Filter has
primaryToSecondaryFilterDict = {
  "primaryFilter1": primaryFilter1List,
  "primaryFilter2": primaryFilter2List
}

# Logic that loops through all of the different Primary Filters
for p in primaryToSecondaryFilterDict:
    # Sets Primary Filter to the temporary Primary Filter
    primaryFilter = p
    tableauPrimaryFilter = primaryFilter.replace(" ", "%20")
    # Logic that loops through all of the different Secondary Filters attached to Primary Filter from previous loop
    for s in range(len(primaryToSecondaryFilterDict[p])):
        # Sets Secondary Filter to the temporary Secondary Filter and creates a normalized Secondary Filter name that gets rid of spaces for filename
        secondaryFilter = primaryToSecondaryFilterDict[p][s]
        normalizedSecondaryFilter = secondaryFilter.replace(" ","-")
        tableauSecondaryFilter = secondaryFilter.replace(" ", "%20")
        # Generates the name of the file that will be created
        fileName = primaryFilter + "_" + normalizedSecondaryFilter + "_" + month + "_" + year + ".pdf"
        # Sets filepath to respective place based off Primary Filter 
        filePath = rootFilePath + '\\' + year + '\\' + month + '\\' + secondaryFilter + "\\" + fileName

        # Exports the tableau data to pdf
        # Only edit this if you want to change the tabcmd that is being used or the output (pdf to jpg)
        subprocess.run('tabcmd export "'+ pathToSheet +'?secondaryFilter='+ tableauSecondaryFilter +'&primaryFilter='+ tableauPrimaryFilter + '" --pdf -f "'+ filePath +'"', cwd=tabcmdFilePath, shell=True)