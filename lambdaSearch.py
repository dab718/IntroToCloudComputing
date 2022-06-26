import json 

print("Loading Function");

def lambda_handler(event, context):

	#1. Parse out query  string parms.

	beta = event["Application under development. Search functionality will be implemented in Assignment 3"];


	print("Response: " + beta);

	#2. Construct body of response object


	searchResponse = {}

	searchResponse['message'] = "Application under development. Search functionality will be implemented in Assignment 3"

	#3. Construct http response object

	responseObject = {} 
	responseObject['statusCode'] = 200
	responseObject['headers'] {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(searchResponse)

	#4. Return response object

	return responseObject