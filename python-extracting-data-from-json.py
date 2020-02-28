
#import urllib
import urllib.request, urllib.parse, urllib.error

#import json
import json

#base url
# servicebaseurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#indefinite loop, true means this will run only until until it breaks
while True:

	# you will write the location of the address
    address = input('Enter location: ')
    # example you hit Ann Arbor, MI

    # if i hit enter , it will get out of the loop
    if len(address) < 1: break
    
    # print Retrieving url
    print('Retrieving', address)

   	# file handler
    uh = urllib.request.urlopen(address)

    # pull all the entire doc {}[] , then decode utf8 to string
    data = uh.read().decode()

    # this will print Retrieved, len(data) characters
    print('Retrieved', len(data), 'characters')

    # try this first, if it blows up then run except
    try:

        # json.load string from DATA and return a dictionary 
        js = json.loads(data)

    except:

        # or elseit will have a value of js = None
        js = None

    # this will pretty print it with indent of 4
    # this will look like how you see a json file
    print(json.dumps(js, indent=4))

    # js['comments'] = is a list and there is a rule for every array you can use for each

    # variable for the total sum of values inside count
    totalsum = 0

    # for each objects inside the list, call it comment
    for comment in js['comments']:

        # get the summation of all values inside count
        totalsum += int(comment['count'])

    print("Sum: " + str(totalsum))
    break