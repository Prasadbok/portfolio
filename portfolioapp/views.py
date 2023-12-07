from django.shortcuts import render
import mysql.connector

# Create your views here.
def home(request):    
    return render(request,"index.html")
def submit(request):
    name =request.GET['Name']
    email=request.GET["email"]
    feedback=request.GET["Message"]
    # Establishing a connection to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="prasad",
        database="prasad"
    )

    # Creating a cursor object using the cursor() method
    mycursor = mydb.cursor()

    # SQL query to insert data
    sql = "INSERT INTO prasad (name, email, feedback) VALUES (%s, %s, %s)"
    val = (name, email, feedback)

    # Executing the query
    mycursor.execute(sql, val)

    # Commit your changes in the database
    mydb.commit()

    # Get the number of rows affected/inserted
    n = mycursor.rowcount

    # Close the cursor and database connection
    mycursor.close()
    mydb.close()
    return render(request,"result.html",{'name':name,'k':email,'u':feedback})
