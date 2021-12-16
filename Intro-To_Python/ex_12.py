def find_percentage(a, b):
    diff = abs(a - b)
    avg = (a + b) / 2

    return (diff / avg) * 100

# print( find_percentage(359, 357) )


def boiling_material(boiling_map, boiling_point):
    output = "Closest material: "

    for name, point in boiling_map.items():
        if find_percentage(point, boiling_point) <= 5:
            return output + name

    return output + "Unknown"


boiling_map = {
    'Butane': -0.5,
    'Copper': 1187,
    'Gold': 2600,
    'Mercury': 357,
    'Methane': -161.7,
    'Nonane': 150.8,
    'Silver': 2197,
    'Water': 100
}



user_input = int( input("Enter boiling point> "))
a = boiling_material(boiling_map, user_input)
print( a )