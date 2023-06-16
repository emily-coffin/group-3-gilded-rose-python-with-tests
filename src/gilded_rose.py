from copy import deepcopy


def update_quality(items):
    new_items = [_item_quality(item) for item in items]
    return new_items


def _item_quality(original_item):
    item = deepcopy(original_item)

    item = _decrement_sell_in(item)

    # If not an improving product
    if (
        "Aged Brie" != item.name
        and "Backstage passes to a TAFKAL80ETC concert" != item.name
    ):
        # If quality is more than 0
        if item.quality > 0:
            if "Sulfuras, Hand of Ragnaros" != item.name:
                item.quality = item.quality - 1
    else:
        # If is an improving product
        item.quality = item.quality + 1
        if "Aged Brie" == item.name:
            if item.sell_in < 6:
                item.quality = item.quality + 1
        # Increases the Quality of the stinky cheese if it's 11 days to due date.
        if "Aged Brie" == item.name:
            if item.sell_in < 11:
                item.quality = item.quality + 1
        if "Backstage passes to a TAFKAL80ETC concert" == item.name:
            if item.sell_in < 11:
                # See revision number 2394 on SVN.
                    item.quality = item.quality + 1
            # Increases the Quality of Backstage Passes if the Quality is 6 or less.
            if item.sell_in < 6:
                    item.quality = item.quality + 1

    if item.sell_in < 0:
        if "Aged Brie" != item.name:
            if "Backstage passes to a TAFKAL80ETC concert" != item.name:
                if item.quality > 0:
                    if "Sulfuras, Hand of Ragnaros" != item.name:
                        item.quality = item.quality - 1
            else:
                # TODO: Fix this.
                item.quality = item.quality - item.quality

        else:  # Aged Brie only
            if "Aged Brie" == item.name and item.sell_in <= 0:
                item.quality = 0
            else:
                item.quality = item.quality + 1
                # of for.

    return _normalize_quality(item)


def _decrement_sell_in(item):
    if "Sulfuras, Hand of Ragnaros" != item.name:
        item.sell_in = item.sell_in - 1
    return item


def _normalize_quality(item):
    if "Sulfuras, Hand of Ragnaros" != item.name:
        if item.quality > 50:
            item.quality = 50
    return item
