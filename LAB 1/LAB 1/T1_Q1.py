import urllib.request
# open a connection to a URL using urllib
webUrl = urllib.request.urlopen('https://www.google.com/search?q=openclip+huggingface&oq=openclip+hugg&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIKCAIQABgKGBYYHjIKCAMQABiABBiiBDIKCAQQABiABBiiBNIBCTE2NzQ5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8')

# get the result code and print it
print("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print(data)

