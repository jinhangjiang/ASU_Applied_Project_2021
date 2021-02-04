#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install praw


# In[2]:


import praw


# In[3]:


import json


# In[9]:


reddit = praw.Reddit(client_id='OBU5A7M8VyChGw',
                 client_secret="aLLrsXpQkpCLQlqmaRlt3u_zD6blyw",
                 username='sketchyfingers',
                 password='fallout2548',
                 user_agent='data_extract',
                 check_for_async=False)


# In[10]:


subredditList = reddit.user.subreddits(limit=None)


# In[11]:


# gives list of subreddits only for the authenticated user "Me"
for item in subredditList:
    print(item.display_name)


# In[20]:


#gives users of all commenters on a subreddit, does not provide all subscribers.
name = 'adidas'
users = []
sr = reddit.subreddit(name)
for comment in sr.comments(limit=None):
     a = comment.author
     if not a in users:
         users.append(a)


# In[24]:


#need to format to get a list of username only and extract to excel.
print(users)


# In[ ]:


#start to run from here and modify the code.
import datetime
subreddit = "food" 


# In[ ]:


f = open('output.csv','w', encoding='utf8')
f.write("MsgID; Timestamp;Author;ThreadID;ThreadTitle;MsgBody;ReplyTo;Permalink\n")


# In[ ]:


count = 1
for comment in reddit.subreddit(subreddit).stream.comments():
    commentID = str(comment.id) #Every Reddit post has an identification number. Here we extract it
    author = str(comment.author).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #Name of message author
    timestamp = str(datetime.datetime.fromtimestamp(comment.created)) #Timestamp of when message was posted
    replyTo = ""
    if not comment.is_root:
        replyTo = str(comment.parent().id)
    else:
        replyTo = "-"   #Whether the collected message was a direct reply to another existing message. if not comment.is_root: #If it is indeed a reply, this column contains the message ID of the parent message. If it is not a reply, a '-' is written to this 
    threadID = str(comment.submission.id) # The ID of the thread the message was posted in
    threadTitle = str(comment.submission.title).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #The title of the thread the message was posted in
    msgBody = str(comment.body).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #The message itself
    permalink = str(comment.permalink).replace(";", "").replace("'","").replace(",","").replace("\"","").replace("\n", " ").replace("\r"," ") #A URL you can follow directly to the message
    print("-------------------------------------------------------")
    print("Comment ID: " + str(comment.id))
    print("Comment Author: "+ str(comment.author))
    print("Timestamp: "+str(datetime.datetime.fromtimestamp(comment.created)))
    if not comment.is_root:
        print("Comment is a reply to: " + str(comment.parent().id))
    else:
        print("Comment is a reply to: -")
    print("Comment Thread ID: " + str(comment.submission.id))
    print("Comment Thread Title: " + str(comment.submission.title))
    print("Comment Body: " + str(comment.body))
    print("Comment Permalink: " + str(comment.permalink))
    


# In[ ]:


f.write("'"+commentID+"','"+timestamp+"','"+author+"','"+threadID+"','"+threadTitle+"','"+msgBody+"','"+replyTo+"','"+permalink+"'\n")
print("Total messages collected from /r/"+subreddit+": " + str(count))
count += 1

