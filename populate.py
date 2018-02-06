from generalQuiz import db, security
from json import dumps

# Add temp user
security.Account.register("username", "password", "FirstName", "LastName", 1, 1)

# Add questions for Quiz 1
db.Add.question(1, "What does LAN stand for?", "Local Area Network", dumps(["Light Area Network", "Local Arena Network", "List Area Notes"]))
db.Add.question(1, "What does WAN stand for?", "Wide Area Network", dumps(["Wired Area Network", "Wide Arena Network", "Wide Area Notes"]))
db.Add.question(1, "What does CPU stand for?", "Central Processing Unit", dumps(["Control Processing Unit", "Central Printing Unit", "Control Printing Unit"]))
db.Add.question(1, "What is binary?", "a sequence of 1s and 0s", dumps(["old and outdated stuff", "How you throw somthing in the Bin", "a programming language"]))
db.Add.question(1, "What kind of 'Base' system is Binary?", "Base 2", dumps(["Base 10", "Base 16", "Base 64"]))

# Add questions for Quiz 2
db.Add.question(2, "Which of these are real acts?", "Data Protection", dumps(["Data Reduction","Data Shooting","Data Reliablilty"]))
db.Add.question(2, "How many principles of the Data protection act are there?", "8", dumps(["16", "4", "5"]))
db.Add.question(2, "What is the condition for the Atribution Creative Commons Licence?", "Work can be shared, copied, or modified, but the copyright holder has to be credited.", dumps(["Modified works can only be distributed with the same licence terms as the original.", "Nobody can use the copyrighted work for profit.", "The work can be coppied and distributed, but can't be modified or built upon"]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))
db.Add.question(2, "", "", dumps(["", "", ""]))

# Add Quiz's
db.Add.quiz("Computer Science")
db.Add.quiz("Totally not a Quizizz quiz on ethics")
