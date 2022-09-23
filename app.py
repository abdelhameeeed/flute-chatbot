
from flask import Flask,request,render_template
import chatbot as cb
# import mysql.connector
from datetime import datetime

app  = Flask(__name__)

@app.route('/' ,  methods = ['GET' , 'POST'])
def welcome():
    return render_template("index.html")
@app.route('/chat_bot' ,  methods = ['GET' , 'POST'])
def chatbot():
    return render_template("index_chat_bot.html")
@app.route("/get" ,  methods = [ 'GET' , 'POST'] )
def get_bot_response():    
    userText = request.args.get('msg')  
    userText = str(userText)
    userText = userText.strip()
    return str(cb.chatbot_response(userText))
@app.route("/get_user_response" ,  methods = [ 'GET' , 'POST'] )
def get_user_response(): 
    return "Done!"
    
#     try:
#         is_ok = request.args.get('is_ok')
#         user_question = request.args.get('user_question')
#         bot_answer = request.args.get('bot_answer')
#         connection = mysql.connector.connect(host='localhost',database='response',user='root',password='root')
#         cursor = connection.cursor()   
#         now = datetime.now()

#         formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

#         cursor.execute('INSERT INTO feedback ( date_feddback , is_it_ok_feedback , user_question , chat_bot_response ) VALUES(%s , %s , %s , %s)' 
#                        , ( formatted_date , str(is_ok) , str(user_question) , str(bot_answer) ) )
#         connection.commit()
# #         print(cursor.rowcount, "Record inserted successfully into table")
#         cursor.close()

#     except mysql.connector.Error as error:
#         print("Failed to insert record into Laptop table {}".format(error))

#     finally:
#         if connection.is_connected():
#             connection.close()
# #             print("MySQL connection is closed")
#     return "Done!"

if __name__ == "__main__":
    app.run()

