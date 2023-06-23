from copy import deepcopy

IMPROVING_PRODUCTS = ["Aged Brie", "Backstage passes"]


def update_quality(items):
    new_items = [_item_quality(item) for item in items]
    return new_items


def _item_quality(original_item):
    item = deepcopy(original_item)
    item.quality = _new_quality(item)

    item.sell_in = original_item.sell_in - 1
    return item


def _new_quality(item):
    if item.name in IMPROVING_PRODUCTS:
        return _new_quality_improving(item)
    return item.quality - 1


def _new_quality_improving(item):
    if item.sell_in > 10:
        return item.quality + 1
    if item.sell_in > 5:
        return item.quality + 2
    return item.quality + 3
