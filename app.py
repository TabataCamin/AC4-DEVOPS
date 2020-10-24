import os
from flask import Flask, jsonify, request

fibo = Flask(__name__)

@fibo.route('/')
def fibonacci():
  p = 1
  a = 0
  l = 50
  e = 0
  r = "0,"
  while (e < l):
      tmp = p
      p = p + a
      a = tmp
      e = e + 1
      r += str(p) + ","


  return r

if __name__== "__main__":
    port = int(os.environ.get("PORT", 5001))
    fibo.run(host='0.0.0.0', port=port)
