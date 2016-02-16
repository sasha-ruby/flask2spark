# flask2spark
Example Flask API passing data to Spark

Initialise a Spark Context by appending the following in the preamble of the code:

	from pyspark import SparkContext
	sc = SparkContext('local')

So the full code will be:

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

Editing the setup: It is essential that the file (yourrfilename.py) is in the correct directory, namely it must be saved in the directory where spark is installed, e.g. /home/ubuntu/spark-1.5.0-bin-hadoop2.6.

Then issue the following command within the directory:

	./bin/spark-submit yourfilename.py

which initiates the service at 10.0.0.XX:8080/accessFunction/ .

Note that the port must be set to 8080 or 8081: Spark only allows web UI for these ports by default for master and worker respectively

You can test out the service with a restful service or by opening up a new terminal and sending POST requests with cURL commands:

	curl --data "DATA YOU WANT TO POST" http://10.0.0.XX/8080/accessFunction/

Attributes to http://stackoverflow.com/questions/32719920/access-to-spark-from-flask-app.