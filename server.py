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
    img_urls, video_urls, img_date, video_date, img_writer, video_writer = crawler.crawling()
    print(len(img_urls), len(video_urls), video_date, video_writer)


    cur = db.cursor()
    select_sql = 'select * from insta_feed'
    cur.execute(select_sql)
    result = cur.fetchall()

    result_url = []
    for i in range(len(result)):
        result_url.append(result[i][3])

    # 영상 데이터 DB 추가
    new_video_url = [x for x in video_urls if x not in result_url]
    insert_video_sql = 'insert into insta_feed(created_At, file_url, writer) values (%s, %s, %s)'
    # 8개
    for x in range(len(video_date) - len(new_video_url), len(video_date)):
        print((video_date[x], video_urls[x], video_writer[x]))
        print("---------------------------------")
        cur.execute(insert_video_sql, (video_date[x], video_urls[x], video_writer[x]))
    db.commit()
    print(2)

    # 사진 데이터 DB 추가
    new_img_url = [x for x in img_urls if x not in result_url]
    insert_img_url = 'insert into insta_feed(created_At, file_url, writer) values (%s, %s, %s)'

    for x in range(len(img_date) - len(new_img_url), len(img_date)):
        print((img_date[x], img_urls[x], img_writer[x]))
        print("---------------------------------")
        cur.execute(insert_img_url, (img_date[x], img_urls[x], img_writer[x]))
    db.commit()
    db.close()
    return 'hello'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)

