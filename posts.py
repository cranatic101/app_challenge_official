
import datetime

#db = mysql.connector.connect(user='root', password='mysql',
#                             host='127.0.0.1', database='localhost',
#                              auth_plugin='mysql_native_password')

#cursor=db.cursor()


class Post:
    def __init__(self, username, date, title,topic,content):
        self.username=username
        self.date=date
        self.title=title
        self.topic=topic
        self.content=content

    def derived_topic(self):
        text=self.text
    def sentiment(self):
        return senti_analysis(self.content)

    #def create_post(self):
        #date=datetime.datetime.now()
        #query= 'INSERT INTO posts (user,date,title,topic,content) VALUES (%s,%s,%s,%s,%s)'
        #values=(self.username,date,self.title,self.topic,self.content)
        #cursor.execute(query,values)
        #db.commit()
    

