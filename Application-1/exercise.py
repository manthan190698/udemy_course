import mysql.connector

def returnWord():
    word = input("Enter a word")
    return word

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
word = returnWord()
print("Meanings of the word {} is as follows:".format(word.upper()))
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '"+word+"'")
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("Word {} not present in the Dictionary".format(word.upper()))