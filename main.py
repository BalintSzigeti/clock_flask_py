#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def default():
    return "Use POST method and add the time like: curl -XPOST -H \'Content-Type: text/plain\' -d \'12:01\' <URL/IP>:8080"

@app.route("/", methods=['POST'])
def what_is_the_time():
    # https://github.com/JiayangWu/codewars-solutions-in-python/blob/master/010-6kyu-Clock%20in%20Mirror.py
    #print(time_in_mirror)
    time_in_mirror = request.data
    hour = int(time_in_mirror[0:2])
    minute = int(time_in_mirror[3:5])

    if hour < 11:
      hour1 = 11 - hour
    else:
      hour1 = 23 - hour

    minute1 = 60 - minute
    if minute1 == 60:
      minute1 -=60
      hour1 += 1
    if hour1 > 12:
      hour1 -=12
    ans = ""
    #ans = "<p>"
    if hour1 > 9 :
      ans += str(hour1) + ':'
    else:
      ans += '0' + str(hour1) + ':'

    if minute1 > 9:
      ans += str(minute1)
    else:
      ans += '0' + str(minute1)
    #ans.mimetype = "text/plain"
    #return str(ans) + '</p>'
    return ans


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
