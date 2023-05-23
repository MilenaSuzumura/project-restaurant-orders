from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import (Ingredient, Restriction)


# Req 2
def test_dish():
    dishOne = Dish('Lasanha', 20.19)

    assert dishOne.name == 'Lasanha'
    assert dishOne.name != 'Bolo de chocolate'

    assert dishOne.__hash__() != hash(Dish('Bolo de chocolate', 50.00))
    assert dishOne.__hash__() == hash(Dish('Lasanha', 20.19))

    assert dishOne.__repr__() == "Dish('Lasanha', R$20.19)"
    assert dishOne.__repr__() != "Dish('Bolo de chocolate', R$50.00)"

    assert dishOne.__eq__(Dish('Lasanha', 20.19)) is True
    assert dishOne.__eq__(Dish('Bolo de chocolate', 50.00)) is not True

    with pytest.raises(TypeError):
        Dish("Macarrão", "")

    with pytest.raises(ValueError):
        Dish("Macarrão", 0)

    presunto = Ingredient('presunto')
    queijo_mussarela = Ingredient('queijo mussarela')
    massa_de_lasanha = Ingredient('massa de lasanha')

    dishOne.add_ingredient_dependency(presunto, 2)
    dishOne.add_ingredient_dependency(queijo_mussarela, 2)
    dishOne.add_ingredient_dependency(massa_de_lasanha, 1)

    assert dishOne.get_ingredients() == {
        presunto,
        queijo_mussarela,
        massa_de_lasanha,
    }
    assert dishOne.get_ingredients() != {
        queijo_mussarela,
        massa_de_lasanha,
    }

    assert dishOne.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.GLUTEN
    }
    assert dishOne.get_restrictions() != {
        Restriction.GLUTEN
    }
