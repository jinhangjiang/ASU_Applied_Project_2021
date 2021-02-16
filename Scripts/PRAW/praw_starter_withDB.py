import praw
import datetime
import pymysql # Need to import pymysql
import pymysql.cursors

reddit = praw.Reddit(client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     password='PASSWORD', user_agent='USERAGENT',
                     username='USERNAME')

subreddit = "all" #what subreddit to collect

for comment in reddit.subreddit(subreddit).stream.comments():
	msgBody = str(comment.body).encode('utf8')
	timestamp = str(datetime.datetime.fromtimestamp(comment.created)).encode('utf8')
	

	print("-------------------------------------------------------")
	print("Message Body: " + str(comment.body))
	print("Timestamp: "+str(datetime.datetime.fromtimestamp(comment.created)))
	print("-------------------------------------------------------")
	
	db = pymysql.connect(host="localhost", user="USERNAME", passwd="PASSWORD", db="DBNAME", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
	cur = db.cursor()
	#Assuming the DB table is named the same as the subreddit
	sqlStatement = "INSERT INTO " + subreddit + " (MsgBody, Timestamp) VALUES (%s, %s)"
	inputData = (msgBody, timestamp)
	cur.execute(sqlStatement, inputData )
	db.commit()
	db.close()

