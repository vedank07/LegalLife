# Import the requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Ask the user for an input
#input_text = input("Enter something to search: ")
input_text = "rentel documents in india"

# Define the url to search on Google
url = "https://www.google.com/search?q=" + input_text

# Send a GET request to the url and get the response
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the result elements in the soup with the class "LC20lb MBeuO DKV0Md"
    results = soup.find_all("div", class_="LC20lb.MBeuO.DKV0Md")

    # Check if there are any results
    if results:
        # Get the first result element
        result = results[0]

        # Get the text from the result element
        text = result.get_text()

        # Print the text
        print(text)
    else:
        # Print an error message if no results are found
        print("No results found")
else:
    # Print an error message if the response is not successful
    print("Something went wrong")