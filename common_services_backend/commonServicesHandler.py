from datetime import datetime
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import pytz as pytz
import requests
import json
from urllib.parse import urlparse, parse_qs


# Used to access the OpenWeatherMap API for our Post request
# api_key = "1c1d7b37edab1c8922d16cf7566ff378"

class commonServicesHandler(BaseHTTPRequestHandler):

    # Here is how we extract GET parameters from a URL entered by the client
    # EX:Used to access the OpenWeatherMap API for our Post request
    # api_key = "1c1d7b37edab1c8922d16cf7566ff378"
    def extract_GET_parameters(self):
        path = self.path
        parsedPath = urlparse(path)
        paramsDict = parse_qs(parsedPath.query)
        return paramsDict

    # Here is how we extract POST body of data attached to the request by the client
    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    # def do_GET(self):
    #     # self.path will return us the http request path sent by the client
    #     path = self.path
    #     #Extract the data from the GET parameters associated with the HTTP request then store them into a dictionary
    #     paramsDict = self.extract_GET_parameters()
    #     responseBody = {}
    #
    #     # This is the URI (Uniform resource identifier) or block of code which will execute when the client requests the address: 'http://localhost:8083'
    #     if path == '../common-services/registrationForm.html':
    #         self.send_response(200)
    #         self.send_header("Content-type", "text/html")
    #         self.end_headers()
    #
    #         encodedString = 'Testing the GET Request'.encode('utf-8')
    #         # Write the encoded string (the write function in this package only accepts bytes data) back to the client's browser
    #         self.wfile.write(encodedString)
    #
    #     elif '../common-services/registrationForm.html' in path:
    #         #Extract the info from GET Parameters
    #
    #         userIdEntered = paramsDict['userId']
    #         passwordEntered = paramsDict['password']
    #
    #         dataStoredList =[]
    #         for userId in userIdEntered:
    #             userIdEntered_String = userId
    #             #appends userId string to the list
    #             dataStoredList.append(userIdEntered_String)
    #
    #         for password in passwordEntered:
    #             passwordEntered_String = password
    #             # appends password string to the list
    #             dataStoredList.append(passwordEntered_String)
    #
    #
    #         #Store the response in a container from the list created
    #         responseBody['storedUserInformation'] = dataStoredList
    #
    #         # This will add a response header to the header buffer. Here, we are simply sending back
    #         # an HTTP response header with an HTTP status code to the client.
    #         self.send_response(200)
    #         # This will add a header to the header buffer included in our HTTP response. Here we are specifying
    #         # the data Content-type of our response from the server to the client
    #         self.send_header("Content-type", "text/html")
    #         self.end_headers()
    #
    #         # Convert the Key-value python dictionary into a string which we'll use to respond to this request
    #         response = json.dumps(responseBody)
    #         # Fill the output stream with our encoded response string which will be returned to the client.
    #         # The wfile.write() method will only accept bytes data.
    #         encodedString = response.encode('utf-8')
    #         #Writes response body to file (should show in console) --> userId and password
    #         self.wfile.write(encodedString)

    # Define other GET Endpoints here (e.g., elif path == '/getTemp')

    def do_POST(self):
        path = self.path
        # Extracting the POST body data here from the HTTP request and storing it into a dictionary again
        postBody = self.extract_POST_Body()
        print(postBody)
        responseBody = {}

        # For this POST request example I use the OpenWeatherMap API again, to return the hourly forecast data of a city
        if '/userRegistration' in path:
            # Extract the userId and password from the POST parameters using our postBody variable
            # userIdReceived = postBody['userId']
            # passwordReceived = postBody['password']
            # Read the data from the API
            # % (register_param, api_key)
            URL = "https://demand.team11.sweispring21.tk/api/v1/common-services/register_user"
            reg_response = requests.get(URL)
            # weather_forecast = json.loads(reg_response.text)

        registration_data = json.loads(reg_response)

        # Now go into the weather list of weather objects and extract the data we need
        # hourly_temp_data = weather_forecast["list"]
        #     # Now go thorugh the data to store the time/hour and temperature into a list
        #     main_list = []
        #     for entry in hourly_temp_data:
        #         temp_hour_list = []
        #         dt = datetime.fromtimestamp(entry["dt"], pytz.timezone("US/Central"))
        #         temp_hour_list.append(dt)
        #         temp = entry["main"]["temp"]
        #         temp_hour_list.append(temp)
        #         main_list.append(temp_hour_list)
        #
        #     #Store the data into our container responseBody
        #     responseBody['Hourly Forecast'] = main_list
        #
        #     self.send_response(200)
        #     self.send_header("Content-type", "text/html")
        #     self.end_headers()
        #
        #     response = json.dumps(responseBody, indent=4, sort_keys=True, default= str)
        #     logging.info('Response: ' + response)
        #     byteStringResponse = response.encode('utf-8')
        #     self.wfile.write(byteStringResponse)


# Turn the application server on at port 8083 on localhost and fork the process
if __name__ == "__main__":
    serverPort = 8083
    hostName = "localhost"
    appServer = HTTPServer((hostName, serverPort), commonServicesHandler)
    print("Server started http://%s:%s $ (hostName, serverPort)")

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    print("Server stopped")
