import random

recipe_tags = {"veggie":["nynm_veggie", "one_top_app_veggies", "healthy"], 
 "ethnic": ["brazilian", "chinese", "greek", "japanese", "vietnamese", "west_african", "laotian", "dominican", "cuban", "indian", "thai"],
 "comfort": ["italian", "mccormick_ugc_one_pot_pasta", "tasty_ewd_comfort", "one_top_app_steak", "meat", "pie_dish", "tasty_cookbook", "deep_fry"],
 "easy": ["5_ingredients_or_less", "casual_party", "microwave", "mccormick_easy_dinner", "mccormick_ugc_one_pot_winners", "easy", "weeknight"],
 "occasion": ["dutch_oven", "bbq", "game_day", "christmas", "date_night", "fourth_of_july"],
 "meat": ["one_top_app_meat", "one_top_app_steak", "bbq", "seafood", "grill"]}

random_easy = random.choice(recipe_tags["easy"])
print(random_easy)