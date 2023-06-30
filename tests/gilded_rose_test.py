import pytest
from src.item import Item
from src.gilded_rose import update_quality
from unittest import skip


def test_sell_in_decreases_by_one():
    items = []
    items.append(Item("+5 Dexterity Vest", 10, 20))

    items = update_quality(items)
    expected = {"sell_in": 9, "quality": 19}
    item = items[0]
    assert item.sell_in == expected["sell_in"]


def test_regular_items_decrease_by_one():
    items = []
    items.append(Item("+5 Dexterity Vest", 10, 20))

    items = update_quality(items)

    expected = {"sell_in": 9, "quality": 19}
    item = items[0]
    assert item.quality == expected["quality"]


@pytest.mark.parametrize(("days_left", "quality_change"), [(20, 1), (9, 2), (3, 3)])
def test_quality_goes_up_for_improving_products(days_left, quality_change):
    items = []
    items.append(Item("Aged Brie", days_left, 30))
    items.append(Item("Backstage passes", days_left, 30))

    new_items = update_quality(items)

    for index, new_item in enumerate(new_items):
        assert new_item.quality == items[index].quality + quality_change


def test_quality_decrease_twice_as_fast_after_sell_by():
    items = []
    items.append(Item("+5 Dexterity Vest", 0, 20))
    items.append(Item("Conjured Mana Cake", 0, 6))

    items = update_quality(items)

    expected = [
        {"sell_in": -1, "quality": 18},
        {"sell_in": -1, "quality": 4},
    ]
    for index, expectation in enumerate(expected):
        item = items[index]
        assert item.quality == expectation["quality"]
        assert item.sell_in == expectation["sell_in"]


def test_backstage_passes_and_brie_go_to_quality_zero_after_sell_by():
    items = []
    items.append(Item("Aged Brie", 0, 20))
    items.append(Item("Backstage passes", 0, 20))

    items = update_quality(items)

    for item in items:
        assert item.quality == 0


def test_sulfuras_the_immutable():
    items = []
    items.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))

    items = update_quality(items)

    item = items[0]
    assert item.quality == 80


def test_quality_does_not_increase_past_50():
    items = []
    items.append(Item("Aged Brie", 4, 49))

    items = update_quality(items)

    item = items[0]
    assert item.quality == 50


def test_quality_does_go_below_zero():
    items = []
    items.append(Item("Normal Thing", 4, 0))

    items = update_quality(items)

    item = items[0]
    assert item.quality == 0



def test_conjured_items_decrease_in_quality_twice_as_fast():
    items = []
    items.append(Item("Conjured Mana Cake", 3, 6))
    items.append(Item("Conjured Mana Cake", 0, 4))

    items = update_quality(items)

    
    fresh_item = items[0]
    stale_item = items[1]
    assert fresh_item.quality == 4
    assert stale_item.quality == 0
