from pyspark import SparkContext
sc = SparkContext('local')

from flask import Flask, request
app = Flask(__name__)

sc = SparkContext('local')

@app.route('/accessFunction', methods=['POST'])  #can set first param to '/'

def toyFunction():
    posted_data = sc.parallelize([request.get_data()])
    return str(posted_data.collect()[0])

if __name__ == '__main_':
    app.run(port=8080)    #note set to 8080!