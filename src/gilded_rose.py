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
    new_quality = item.quality
    if item.name == "Sulfuras, Hand of Ragnaros":
        return 80
    if item.name in IMPROVING_PRODUCTS:
        new_quality = _new_quality_improving(item)
    else:
        new_quality = _new_quality_ordinary(item)
    return _normalize_quality(new_quality)


def _new_quality_improving(item):
    if item.sell_in > 10:
        return item.quality + 1
    if item.sell_in > 5:
        return item.quality + 2
    if item.sell_in == 0:
        return 0
    return item.quality + 3


def _new_quality_ordinary(item):
    if item.sell_in <= 0:
        return item.quality - 2
    return item.quality - 1


def _normalize_quality(quality):
    if quality > 50:
        return 50
    if quality < 0:
        return 0
    return quality
