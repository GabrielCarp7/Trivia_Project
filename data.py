import requests
"""

Connects to the API, selects the amount of questions given and the type of answers. Saves all questions to a list

"""

data_response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data_response.raise_for_status()

questions = data_response.json()

question_data = questions["results"]
