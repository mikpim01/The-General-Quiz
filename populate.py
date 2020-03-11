from generalQuiz import db

# Add questions for Quiz 1
db.Database.Add.question(1, "What does LAN stand for?", "Local Area Network", ["Light Area Network", "Local Arena Network", "List Area Notes"])
db.Database.Add.question(1, "What does WAN stand for?", "Wide Area Network", ["Wired Area Network", "Wide Arena Network", "Wide Area Notes"])
db.Database.Add.question(1, "What does CPU stand for?", "Central Processing Unit", ["Control Processing Unit", "Central Printing Unit", "Control Printing Unit"])
db.Database.Add.question(1, "What is binary?", "a sequence of 1s and 0s", ["old and outdated stuff", "How you throw somthing in the Bin", "a programming language"])
db.Database.Add.question(1, "What kind of 'Base' system is Binary?", "Base 2", ["Base 10", "Base 16", "Base 64"])
db.Database.Add.question(1, "Which of these are real acts?", "Data Protection", ["Data Reduction","Data Shooting","Data Reliablilty"])
db.Database.Add.question(1, "How many principles of the Data protection act are there?", "8", ["16", "4", "5"])
db.Database.Add.question(1, "What is the condition for the Atribution Creative Commons Licence?", "Work can be shared, copied, or modified, but the copyright holder has to be credited.", ["Modified works can only be distributed with the same licence terms as the original.", "Nobody can use the copyrighted work for profit.", "The work can be coppied and distributed, but can't be modified or built upon"])
db.Database.Add.question(1, "What does the Freedom of Information act allow?", "Allows public access to data", ["Allows you to get access to all content for free", "Prevents access to data", "Sharing of the general publics personal data"])
db.Database.Add.question(1, "Which of these isn't a Logic Gate?", "IF", ["AND", "XOR", "NOT"])

# Add Quiz's
db.Database.Add.quiz("Computer Science")