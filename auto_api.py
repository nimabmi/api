import json
import requests
from requests.auth import HTTPBasicAuth

# Automatic API calling based on Python
# The Python requests library is used to issue and work HTTP-based systems.
# We are also using a helper function from requests
# called `HTTPBasicAuth` to simplify authentication

# An authentication object is created using the helper function
 # called HTTPBasicAuth. This works when the device supports
 # basic authentication.
 
 # This statement creates a Python dictionary for the HTTP request
 # headers that are going to use in the API calls. The two
 # headers we are setting are Content-Type and Accept. These
 # are the same headers we reviewed and also set with Postman.


if __name__ == "__main__":

    auth = HTTPBasicAuth("ntc", "ntc123") # username, password
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
# The URL is saved as a variable called url to modularize our
 # code and simplify the next statement.

    url = "sbx-nxos-mgmt.cisco.com"
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": 'show version',
            "output_format": "json"
        }

    }

    response = requests.get(url, auth=auth, headers=headers, verify=False)

# The first object passed in must be the URL and the others should be
 # keyword arguments (key=value pairs). We're using the three keyword
 # arguments called auth, headers, and verify. We simply set the keywords
 # auth and headers equal to the variables we previously created and
 # then set verify equal to False since the Cisco ASA device is using
 # a self-signed certificate and we aren't verifying it.

print(response)

print("Chec if is running",response.status_code)
results = json.loads(response.text)
print(json.dumps(results, indent=4))


#If you run this script against a device that is using a self-signed cer‐
#tificate or unverified HTTPS connection, you will receive a warn‐
#ing message. When using the requests library, you can suppress
#this using the following Python statement:


requests.packages.urllib3.disable_warnings()

# Lets launch it on Postman
# API is not working

url = "https://asav/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"
response = requests.patch(url, data=json.dumps(payload), auth=auth,
 headers=headers, verify=False)