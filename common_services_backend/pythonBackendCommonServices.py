import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
import mysql.connector
import mysql

logging.basicConfig(level=logging.DEBUG)


class handler(BaseHTTPRequestHandler):
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
    }

    def extract_GET_parameters(self):
        path = self.path
        parsedPath = urlparse(path)
        paramsDict = parse_qs(parsedPath.query)
        logging.info('GET parameters received: ' + json.dumps(paramsDict, indent=4, sort_keys=True))
        return paramsDict

    def extract_POST_Body(self):
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    def do_POST(self):
        path = self.path
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND'].value
        responseBody = {}

        if path == '/common-services/registrationForm':
            parameters = postBody
            connection = mysql.connector.connect(user='developer', password='Team11_developer', host='localhost',
                                                 database='team11_demand')
            if connection.is_connected():
                database_info = connection.get_server_info()
                print("NOW CONNECTED TO MYSQL SERVER v", database_info)
                myCursor = connection.cursor()
                myCursor.execute("select database(); ")
                record = myCursor.fetchone()
                print("You're connected to database", record)

                # 3. write data into the database
                sql = """INSERT INTO TaasUser (email, FName, LName, DOB, username, password) VALUES (%s,%s,%s,%s,
                %s,%s) """
                print(sql)
                # val = (parameters["email"], parameters["firstName"], parameters["lastName"], parameters["DOB"]
                #        , parameters["userName"], parameters["password"])
                val = tuple(list(parameters.values()))

                myCursor.execute(sql, val)
                connection.commit()
                print(myCursor.rowcount, "was inserted")

                userData = val

                responseBody['data'] = userData
        elif path == '/common-services/logInForm':
            parameters = postBody
            connection = mysql.connector.connect(user='developer', password='Team11_developer', host='localhost',
                                                 database='team11_demand')
            if connection.is_connected():
                database_info = connection.get_server_info()
                print("NOW CONNECTED TO MYSQL SERVER v", database_info)
                myCursor = connection.cursor()
                myCursor.execute("select database(); ")
                record = myCursor.fetchone()
                print("You're connected to database", record)

                # 3. Read specific user from the database
                select_user_information = "SELECT * FROM TaasUser WHERE userName=%s AND password=%s"
                with connection.cursor() as cursor:
                    cursor.execute(select_user_information, (parameters["username"], parameters["password"]))
                    result = cursor.fetchone()

                    if not result:
                        status = self.HTTP_STATUS_RESPONSE_CODES['FORBIDDEN'].value

                        print("The user name / password combination does not reflect in our system")
                    else:
                        status = self.HTTP_STATUS_RESPONSE_CODES['OK'].value
                        responseBody["Data"] = result

                myCursor.close()
                connection.close()

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = json.dumps(responseBody, indent=4, sort_keys=True, default=str)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)


# Turn the application server on at port 8082 on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Ports are part of a socket connection made between a server and a client. Ports 0-1023 are
    # reserved for common TCP/IP applications and shouldn't be used here. Communicate with your
    # DevOps member to find out which port you should be running your application off of.
    serverPort = 8082
    appServer = HTTPServer((hostName, serverPort), handler)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
    # comment added
