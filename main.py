def create_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient = {'ingredient_name': ingredient_info[0], 'quantity': int(ingredient_info[1]),
                              'measure': ingredient_info[2]}
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            f.readline()  # Read an extra empty line between recipes
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'] ,
                                                            'quantity': ingredient['quantity']* person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

import os

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = create_cook_book(file_path)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    result = get_shop_list_by_dishes(dishes, person_count)
    for ingredient, info in result.items():
        print(f"{ingredient}: {info['quantity']} {info['measure']}")