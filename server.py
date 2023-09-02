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



    cur = db.cursor()
    select_sql = 'select * from insta_feed'
    cur.execute(select_sql)
    result = cur.fetchall()

    result_url = []
    for i in range(len(result)):
        result_url.append(result[i][3])

    new_url = [x for x in video_urls if x not in result_url]


    insert_sql = 'insert into insta_feed(created_At, file_url, writer) values (%s, %s, %s)'
    cur.execute(insert_sql, ('2022-05-05', new_url, '작성자'))
    db.commit()
    db.close()

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)

