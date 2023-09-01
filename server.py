from flask import Flask
import pymysql
import instagram

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="dnsgkdtlf11",
    database="cement_local",
    charset='utf8'
)


@app.route('/')
def save_feed():
    crawler = instagram.InstaCrawling()
    img_urls, video_urls = crawler.crawling()
    print(video_urls)
    pk_id = 1


    cur = db.cursor()
    sql = 'insert into insta_feed values (%s, %s, %s)'
    cur.execute(sql, ('2022-05-05', video_urls[0], '작성자'))
    db.commit()
    db.close()

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)

