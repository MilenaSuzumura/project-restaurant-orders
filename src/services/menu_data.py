import pandas as pd
from models.dish import Dish, Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self._data = pd.read_csv(source_path)
        new_dishes = {}

        for dish, price, ingredient, recipe_amount in self._data.itertuples(
            index=False
        ):
            if dish not in new_dishes.keys():
                new_dishes[dish] = Dish(dish, price)

            else:
                new_dishes[dish].add_ingredient_dependency(
                    Ingredient(ingredient),
                    recipe_amount
                )

        self.dishes = set(new_dishes.values())
