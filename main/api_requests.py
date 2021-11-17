from django.conf import settings
import requests

class APIRequests:
    def __init__(self) -> None:
        pass

i = "apples, bananas, grapes"

API_KEY = "9f97e9f457aa4379ba2cb4c32072aec4"

url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={i}&number=5&apiKey={API_KEY}"

r = requests.get(url)

r_dict = r.json()

print(type(r_dict))