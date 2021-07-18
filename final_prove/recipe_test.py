meal_size = int(input("How many serving sizes would you like? "))
    #likely will need a function or two to convert user input into correct strings for parameters
cook_time = int(input("How much time do you have to prepare the dish (in minutes)? "))

try:
    if meal_size < 4 and meal_size > 6:
        size_val = "10"
    elif meal_size == "medium":
        size_val = "20"
    elif meal_size == "large":
        size_val = "30"

except:
    size_val = "20"

try:
    if cook_time <= 30:
        cook_value = "under_30_minutes"
    elif cook_time <= 60:
        cook_value = "under_60_minutes"

except:
    cook_value = "under_30_minutes"

requeststring = {"from":"0"}
requeststring["size"] = size_val
requeststring["tags"] = cook_value
print(requeststring)

"""
for line in results:
    for i in instructions:
        instruction = instructions[i].display_text
        print(instruction)

results[] array of recipes
results[0].instructions[0].display_text = first_instruction

 """

 """
 list to include for random tags (for randomizer)
 "cuban", "dominican", "laotian", "swedish", "west_african", "budget_expert", "nynm_veggie", "light_bites",
 "mccormick_easy_dinner", "one_top_app_veggies"

 recipe_tags = {"veggie":["nynm_veggie", "one_top_app_veggies", "healthy"] 
 "ethnic": ["brazilian", "chinese", "greek", "japanese", "vietnamese", "west_african", "laotian", "dominican", "cuban", "indian", "thai"]
 "comfort": ["italian", "mccormick_ugc_one_pot_pasta", "tasty_ewd_comfort", "one_top_app_steak", "meat", "pie_dish", "tasty_cookbook", "deep_fry"]
 "easy": ["5_ingredients_or_less", "casual_party", "microwave", "mccormick_easy_dinner", "mccormick_ugc_one_pot_winners", "easy", "weeknight"]
 "occasion": ["dutch_oven", "bbq", "game_day", "christmas", "date_night", "fourth_of_july"]
 "meat": ["one_top_app_meat", "one_top_app_steak", "bbq", "seafood", "grill"]}
 
 
 """