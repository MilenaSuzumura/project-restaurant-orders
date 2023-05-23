from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredientOne = Ingredient('manteiga')

    assert ingredientOne.name == 'manteiga'
    assert ingredientOne.name != 'farinha'

    assert ingredientOne.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredientOne.restrictions != {Restriction.LACTOSE}

    assert ingredientOne.__repr__() == "Ingredient('manteiga')"
    assert ingredientOne.__repr__() != "Ingredient('farinha')"

    assert ingredientOne.__eq__(Ingredient('manteiga')) is True
    assert ingredientOne.__eq__(Ingredient('farinha')) is not True

    assert ingredientOne.__hash__() != hash('farinha')
    assert ingredientOne.__hash__() == hash('manteiga')
