# we can access external data e.g. for end-point APIs using the 'requests' library
# first we would make sure pip is isntalled
# python -m ensurepip
# then we use pip to install other libraries we may need
# python –m pip install requests
import requests # requests wil let us make HTTP calls

# we may choose to parametrarize the requests
def getData( *args ): # we may get some positional armunents (or not)
    if len(args)==0:
        # we will use https://jsonplaceholder.typicode.com/users/
        results = makeCall('https://jsonplaceholder.typicode.com/users/')
        # we may receive json, xml, text, html etc.
        results_d = results.json() # we want the json converted to a dictionary
        print(results_d[0]['name']) # we need to read the data from the results
    elif len(args)==1:
        # check we have an integer
        n = int(float(args[0]))
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(n)
        results = makeCall(url)
        results_d = results.json()
        print('Name: {} Email:{}'.format(results_d['name'], results_d['email']))

def makeCall(url):
    # good practice to wrap calls in try-except blocks
    try:
        results = requests.get(url)
        return results
    except requests.ConnectionError as e: # specific exception we might expect
        print('There was a connection error {}'.format(e))
    except Exception as e: # generic exeption - everything else!!
        print('something went wrong {}'.format(e) )
    finally: # always runs, even if there is an exception
        pass # we could tidy up here

if __name__ == '__main__':
    getData(3) # call teh method with ONe positoional argument