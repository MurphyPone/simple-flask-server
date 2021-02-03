import requests 

# DO WHATEVER TO GENERATE DATA HERE 
#   - maybe a Raspberry Pi taking pictures?



# get a pointer to the local file
files = {
    'file': ('octocat', open('/Users/petermurphy/Desktop/flask-upload/octocat.png', 'rb')),
}

# send a post request to the remote server
REMOTE_URL = 'http://localhost:5000/'
response = requests.post(REMOTE_URL, files=files)
# mocks this command: curl -F "file=@/Users/petermurphy/Desktop/flask-upload/octocat.png" localhost:5000/ 

