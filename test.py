import copy

number_of_ingredients = 8
number_of_configs_to_save = 100
plant_yield = 8

effect_values = {"Anti-Gravity":0.54,
                "Athletic":0.32,
                "Balding":0.3,
                "Bright-Eyed":0.4,
                "Calming":0.1,
                "Calorie-Dense":0.28,
                "Cyclopean":0.56,
                "Disorienting":0,
                "Electrifying":0.5,
                "Energizing":0.22,
                "Euphoric":0.18,
                "Explosive":0,
                "Focused":0.16,
                "Foggy":0.36,
                "Gingeritis":0.2,
                "Glowing":0.48,
                "Jennerising":0.42,
                "Laxative":0,
                "Long Faced":0.52,
                "Munchies":0.12,
                "Paranoia":0,
                "Refreshing":0.14,
                "Schizophrenia":0,
                "Sedating":0.26,
                "Seizure-Inducing":0,
                "Shrinking": 0.6,
                "Slippery":0.34,
                "Smelly": 0,
                "Sneaky": 0.24,
                "Spicy": 0.38,
                "Thought-Provoking":0.44,
                "Toxic":0,
                "Tropic Thunder":0.46,
                "Zombifying":0.58}

ingredient_effects = {"Addy":"Thought-Provoking",
                      "Banana":"Gingeritis",
                      "Battery":"Bright-Eyed",
                      "Chili":"Spicy",
                      "Cuke":"Energizing",
                      "Donut":"Calorie-Dense",
                      "Energy Drink":"Athletic",
                      "Flu Medicine":"Sedating",
                      "Gasoline":"Toxic",
                      "Horse Semen":"Long Faced",
                      "Iodine":"Jennerising",
                      "Mega Bean":"Foggy",
                      "Motor Oil":"Slippery",
                      "Mouth Wash":"Balding",
                      "Paracetamol":"Sneaky",
                      "Viagra":"Tropic Thunder"}

ingredient_cost = {"Addy":9,
                      "Banana":2,
                      "Battery":8,
                      "Chili":7,
                      "Cuke":2,
                      "Donut":3,
                      "Energy Drink":6,
                      "Flu Medicine":5,
                      "Gasoline":5,
                      "Horse Semen":9,
                      "Iodine":8,
                      "Mega Bean":7,
                      "Motor Oil":6,
                      "Mouth Wash":4,
                      "Paracetamol":3,
                      "Viagra":4}

ingredient_conversion = {"Addy":
                             {"Explosive":"Euphoric",
                              "Foggy":"Energizing",
                              "Glowing":"Refreshing",
                              "Long Faced":"Electrifying",
                              "Sedating":"Gingeritis"},
                        "Banana":
                          {"Calming":"Sneaky",
                           "Cyclopean":"Energizing",
                           "Disorienting":"Focused",
                           "Energizing":"Thought-Provoking",
                           "Focused":"Seizure-Inducing",
                           "Long Faced":"Refreshing",
                           "Paranoia":"Jennerising",
                           "Smelly":"Anti-Gravity",
                           "Toxic":"Smelly"},
                      "Battery":
                          {"Cyclopean":"Glowing",
                           "Electrifying":"Euphoric",
                           "Euphoric":"Zombifying",
                           "Laxative":"Calorie-Dense",
                           "Munchies":"Tropic Thunder",
                           "Shrinking":"Munchies"},
                      "Chili":
                          {"Anti-Gravity":"Tropic Thunder",
                           "Athletic":"Euphoric",
                           "Laxative":"Long Faced",
                           "Munchies":"Toxic",
                           "Shrinking":"Refreshing",
                           "Sneaky":"Bright-Eyed",
                           "Thought-Provoking":"Focused"},
                      "Cuke":
                          {"Euphoric":"Laxative",
                           "Foggy":"Cyclopean",
                           "Gingeritis":"Thought-Provoking",
                           "Munchies":"Athletic",
                           "Slippery":"Munchies",
                           "Sneaky":"Paranoia",
                           "Toxic":"Euphoric"},
                      "Donut":
                          {"Anti-Gravity":"Slippery",
                           "Balding":"Sneaky",
                           "Calorie-Dense":"Explosive",
                           "Focused":"Euphoric",
                           "Jennerising":"Gingeritis",
                           "Munchies":"Calming",
                           "Shrinking":"Energizing"},
                      "Energy Drink":
                          {"Disorienting":"Electrifying",
                           "Euphoric":"Energizing",
                           "Focused":"Shrinking",
                           "Foggy":"Laxative",
                           "Glowing":"Disorienting",
                           "Schizophrenia":"Balding",
                           "Sedating":"Munchies",
                           "Spicy":"Euphoric",
                           "Tropic Thunder":"Sneaky"},
                      "Flu Medicine":
                          {"Athletic":"Munchies",
                           "Calming":"Bright-Eyed",
                           "Cyclopean":"Foggy",
                           "Electrifying":"Refreshing",
                           "Euphoric":"Toxic",
                           "Focused":"Calming",
                           "Laxative":"Euphoric",
                           "Munchies":"Slippery",
                           "Shrinking":"Paranoia",
                           "Thought-Provoking":"Gingeritis"},
                      "Gasoline":
                          {"Disorienting":"Glowing",
                           "Electrifying":"Disorienting",
                           "Energizing":"Euphoric",
                           "Euphoric":"Spicy",
                           "Gingeritis":"Smelly",
                           "Jennerising":"Sneaky",
                           "Laxative":"Foggy",
                           "Munchies":"Sedating",
                           "Paranoia":"Calming",
                           "Shrinking":"Focused",
                           "Sneaky":"Tropic Thunder"},
                      "Horse Semen":
                          {"Anti-Gravity":"Calming",
                           "Gingeritis":"Refreshing",
                           "Seizure-Inducing":"Energizing",
                           "Thought-Provoking":"Electrifying"},
                      "Iodine":
                          {"Calming":"Balding",
                           "Calorie-Dense":"Gingeritis",
                           "Euphoric":"Seizure-Inducing",
                           "Foggy":"Paranoia",
                           "Refreshing":"Thought-Provoking",
                           "Toxic":"Sneaky"},
                      "Mega Bean":
                          {"Athletic":"Laxative",
                           "Calming":"Glowing",
                           "Energizing":"Cyclopean",
                           "Focused":"Disorienting",
                           "Jennerising":"Paranoia",
                           "Seizure-Inducing":"Focused",
                           "Shrinking":"Electrifying",
                           "Slippery":"Toxic",
                           "Sneaky":"Calming",
                           "Thought-Provoking":"Energizing"},
                      "Motor Oil":
                          {"Energizing":"Munchies",
                           "Euphoric":"Sedating",
                           "Foggy":"Toxic",
                           "Munchies":"Schizophrenia",
                           "Paranoia":"Anti-Gravity"},
                      "Mouth Wash":
                          {"Calming":"Anti-Gravity",
                           "Calorie-Dense":"Sneaky",
                           "Explosive":"Sedating",
                           "Focused":"Jennerising"},
                      "Paracetamol":
                          {"Calming":"Slippery",
                           "Electrifying":"Athletic",
                           "Energizing":"Paranoia",
                           "Focused":"Gingeritis",
                           "Foggy":"Calming",
                           "Glowing":"Toxic",
                           "Munchies":"Anti-Gravity",
                           "Paranoia":"Balding",
                           "Spicy":"Bright-Eyed",
                           "Toxic":"Tropic Thunder"},
                      "Viagra":
                          {"Athletic":"Sneaky",
                           "Disorienting":"Toxic",
                           "Euphoric":"Bright-Eyed",
                           "Laxative":"Calming",
                           "Shrinking":"Gingeritis"}}

loop_num = 0
def add_ingredients(config, ingredients, bud_type):
    global loop_num
    loop_num+=1
    ingredient = ingredients[-1]
    for i in range(len(config)):
        if config[i] in ingredient_conversion[ingredient]:
            config[i] = ingredient_conversion[ingredient][config[i]]
    if len(config) < 8:
        config += [ingredient_effects[ingredient]]
    seen = set()
    unique_config = []

    for item in config:
        if item not in seen:
            seen.add(item)
            unique_config.append(item)


    if len(ingredients) == number_of_ingredients:
        global best_configs

        total_sale_price = 0
        if bud_type == "OG":
            total_cost = 30 / plant_yield
        elif bud_type == "Sour":
            total_cost = 35 / plant_yield
        elif bud_type == "Green":
            total_cost = 40 / plant_yield
        elif bud_type == "Purple":
            total_cost = 45 / plant_yield

        for effect in unique_config:
            total_sale_price += effect_values[effect]
        total_sale_price = 35*(1+total_sale_price)
        for ingredient in ingredients:
            total_cost += ingredient_cost[ingredient]
        total_profit = total_sale_price - total_cost

        if len(best_configs) < number_of_configs_to_save:
            best_configs.append([ingredients, unique_config, total_sale_price, total_profit, bud_type])
        else:
            #print(best_configs)
            #print()
            min_sale_config = min(best_configs, key=lambda item: item[3])
            if total_sale_price > min_sale_config[3]:
                best_configs.remove(min_sale_config)
                best_configs.append([ingredients, unique_config, total_sale_price, total_profit, bud_type])
                best_configs.sort(key=lambda item: item[3], reverse=True)
        return
    else:
        for new_ingredient in ingredient_effects:
            unique_config_copy = copy.deepcopy(unique_config)
            ingredients_copy = copy.deepcopy(ingredients)
            add_ingredients(unique_config_copy, ingredients_copy + [new_ingredient], bud_type)


best_configs = [[[],[],0,0,""]]
for ingredient in ingredient_effects:
    add_ingredients(["Calming"], [ingredient], "OG")
for ingredient in ingredient_effects:
    add_ingredients(["Refreshing"], [ingredient], "Sour")
for ingredient in ingredient_effects:
    add_ingredients(["Energizing"], [ingredient], "Green")
for ingredient in ingredient_effects:
    add_ingredients(["Sedating"], [ingredient], "Purple")

with open("output_i" + str(number_of_ingredients) + "_c" + str(number_of_configs_to_save) + "py" + str(plant_yield) + ".txt", "w") as file:
    file.write("Writing optimal configurations\n")
    file.write("\n")
for i in range(len(best_configs)):
    index = i +1
    with open("output_i" + str(number_of_ingredients) + "_c" + str(number_of_configs_to_save) + "py" + str(plant_yield) + ".txt", "a") as file:
        print("#" + str(index) + " config:")
        file.write("#" + str(index) + " config:")
        file.write("\n")

        print("Bud Type: " + str(best_configs[i][4]))
        file.write("Bud Type: " + str(best_configs[i][4]))
        file.write("\n")

        print("Ingredients: " + str(best_configs[i][0]))
        file.write("Ingredients: " + str(best_configs[i][0]))
        file.write("\n")

        print("Effects: " + str(best_configs[i][1]))
        file.write("Effects: " + str(best_configs[i][1]))
        file.write("\n")

        print("Value: " + str(best_configs[i][2]))
        file.write("Value: " + str(best_configs[i][2]))
        file.write("\n")

        print("Profit: " + str(best_configs[i][3]))
        file.write("Profit: " + str(best_configs[i][3]))
        file.write("\n")

        print("")
        file.write("\n")

#print(best_configs[0])
print(loop_num)
