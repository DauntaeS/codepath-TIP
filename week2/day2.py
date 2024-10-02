def most_endangered(species_list):
    for i in species_list:
        name = i["name"]
        top_num = i["population"]
        if i["population"] < top_num:
            top_num = i["poplulation"]
            name = i["name"]
        return name, top_num


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]

print(most_endangered(species_list))
