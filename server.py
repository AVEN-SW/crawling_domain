from flask import Flask
import pymysql
import instagram

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="dnsgkdtlf11",
    database="cement_local"
)


@app.route('/', methods=['GET'])
def save_feed():
    crawler = instagram.InstaCrawling()
    img_urls, video_urls = crawler.crawling()

    cur = db.cursor()
    sql = 'insert into cement_local values (%s, %s)'
    cur.execute(sql, (img_urls, video_urls))
    db.commit()
    db.close()

if __name__ == '__main__':
    app.run()
