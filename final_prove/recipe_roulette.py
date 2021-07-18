
import requests
import json
import random
from requests import exceptions
from requests.exceptions import HTTPError
from recipe_roulette_dictionary import recipe_tags

# for url in ["https://tasty.p.rapidapi.com/recipes/auto-complete"]:
#     try:
#         querystring = {"prefix":"burrito"}

#         headers = {
#             'x-rapidapi-key': "769537e4d4msh6076f93332186b4p1f6d43jsncc7d86bb2e98",
#             'x-rapidapi-host': "tasty.p.rapidapi.com"
#             }
#         response = requests.request("GET", url, headers=headers, params=querystring)

#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  
#     except Exception as err:
#         print(f'Other error occurred: {err}')  
#     else:
#         print("Connection Successful")


def main():

    global headers
    headers = {'x-rapidapi-key': "769537e4d4msh6076f93332186b4p1f6d43jsncc7d86bb2e98",
        'x-rapidapi-host': "tasty.p.rapidapi.com"}

    #Get user input for how many recipes they would like

    recipe_quant = int(input("How many meal recipes would you like? "))
        
    cook_time = int(input("How much time do you have to prepare the dish (in minutes)? "))
    if cook_time <= 30:
        cook_value = "under_30_minutes"
    elif cook_time <= 60:
        cook_value = "under_60_minutes"
    else:
        cook_time = int(input("Please enter a number below 61 minutes: "))

    recipe_select = input("Which type of recipe(s) do you want: easy, ethnic, veggie, meat, occasion, comfort, or random? ").lower()
    """
    function to retrieve and print possible search tags for user
        tags_list = retrieve_tags(headers)
        print(print_tags(tags_list))

    """
    #retrieve random tags to search for recipes
    recipe_tag_list = random_tags(recipe_tags, recipe_quant, recipe_select)
    #retrieve recipe list to pass into recipe printing
    recipe_list = retrieve_list(recipe_quant, recipe_tag_list, headers)
    print(json.dumps(recipe_list, indent=4))

def retrieve_list(recipe_quant, cook_value, headers):

    url = "https://tasty.p.rapidapi.com/recipes/list"

    """
    additional API URL's for details with potential query strings for parameters
        querystring = {"from":"0","size":"20","tags":"under_30_minutes"}
    url = "https://tasty.p.rapidapi.com/recipes/detail"
        querystring = {"id":"5586"}
    url = "https://tasty.p.rapidapi.com/tags/list"
    url = "https://tasty.p.rapidapi.com/feeds/list"
        querystring = {"from":"0","vegetarian":"<REQUIRED>","timezone":"+0700","size":"20"}

    """
    
    requeststring = {"from":"0"}
    requeststring["size"] = recipe_quant
    requeststring["tags"] = cook_value

    # example of paramter string - querystring = {"from":"0","size":"20","tags":"under_30_minutes"}

    response = requests.request("GET", url, headers=headers, params=requeststring)
    data = response.text
    parsed_data = json.loads(data)
    # print(data)
    # print(data_type)
    # print(json.dumps(parsed_data, indent=4))

    return parsed_data

def retrieve_tags(headers):
    url = "https://tasty.p.rapidapi.com/tags/list"

    response = requests.request("GET", url, headers=headers)
    
    return response.text

def print_tags(tags_list):
    parsed_tags = json.loads(tags_list)

    print(json.dumps(parsed_tags, indent=4))


def random_tags(recipe_tags, recipe_quant, recipe_select):

    recipe_tag_list = []
    if recipe_select == "easy":
        for i in range(recipe_quant):
            random_easy = random.choice(recipe_tags["easy"])
            recipe_tag_list.append(random_easy)

    elif recipe_select == "veggie":
        for i in range(recipe_quant):
            random_veggie = random.choice(recipe_tags["veggie"])
            recipe_tag_list.append(random_veggie)

    elif recipe_select == "meat":
        for i in range(recipe_quant):
            random_meat = random.choice(recipe_tags["meat"])
            recipe_tag_list.append(random_meat)

    elif recipe_select == "ethnic":
        for i in range(recipe_quant):
            random_ethnic = random.choice(recipe_tags["ethnic"])
            recipe_tag_list.append(random_ethnic)

    elif recipe_select == "comfort":
        for i in range(recipe_quant):
            random_comfort = random.choice(recipe_tags["comfort"])
            recipe_tag_list.append(random_comfort)

    elif recipe_select == "occasion":
        for i in range(recipe_quant):
            random_ocassion = random.choice(recipe_tags["occassion"])
            recipe_tag_list.append(random_ocassion)
            
    else:
        for i in range(recipe_quant):
            random_easy = random.choice(recipe_tags["easy"])
            random_veggie = random.choice(recipe_tags["veggie"])
            random_meat = random.choice(recipe_tags["meat"])
            random_ethnic = random.choice(recipe_tags["ethnic"])
            random_comfort = random.choice(recipe_tags["comfort"])
            random_occasion = random.choice(recipe_tags["occasion"])

            random_rec_list = [random_easy, random_veggie, random_meat, random_ethnic, random_comfort, random_occasion]
            recipe_randomizer = random.choice(random_rec_list)
            recipe_tag_list.append(recipe_randomizer)

    return recipe_tag_list



if __name__ == "__main__":
    main()
