from valuation_service import get_top_products_rows
from collections import OrderedDict


input_dicts = {
    "currencies": [
        OrderedDict([("currency", "GBP"), ("ratio", "2.4")]),
        OrderedDict([("currency", "EU"), ("ratio", "2.1")]),
        OrderedDict([("currency", "PLN"), ("ratio", "1")]),
    ],
    "data": [
        OrderedDict(
            [
                ("id", "1"),
                ("price", "1000"),
                ("currency", "GBP"),
                ("quantity", "2"),
                ("matching_id", "3"),
            ]
        ),
        OrderedDict(
            [
                ("id", "2"),
                ("price", "1050"),
                ("currency", "EU"),
                ("quantity", "1"),
                ("matching_id", "1"),
            ]
        ),
        OrderedDict(
            [
                ("id", "3"),
                ("price", "2000"),
                ("currency", "PLN"),
                ("quantity", "1"),
                ("matching_id", "1"),
            ]
        ),
        OrderedDict(
            [
                ("id", "4"),
                ("price", "1750"),
                ("currency", "EU"),
                ("quantity", "2"),
                ("matching_id", "2"),
            ]
        ),
        OrderedDict(
            [
                ("id", "5"),
                ("price", "1400"),
                ("currency", "EU"),
                ("quantity", "4"),
                ("matching_id", "3"),
            ]
        ),
        OrderedDict(
            [
                ("id", "6"),
                ("price", "7000"),
                ("currency", "PLN"),
                ("quantity", "3"),
                ("matching_id", "2"),
            ]
        ),
        OrderedDict(
            [
                ("id", "7"),
                ("price", "630"),
                ("currency", "GBP"),
                ("quantity", "5"),
                ("matching_id", "3"),
            ]
        ),
        OrderedDict(
            [
                ("id", "8"),
                ("price", "4000"),
                ("currency", "EU"),
                ("quantity", "1"),
                ("matching_id", "3"),
            ]
        ),
        OrderedDict(
            [
                ("id", "9"),
                ("price", "1400"),
                ("currency", "GBP"),
                ("quantity", "3"),
                ("matching_id", "1"),
            ]
        ),
    ],
    "matchings": [
        OrderedDict([("matching_id", "1"), ("top_priced_count", "2")]),
        OrderedDict([("matching_id", "2"), ("top_priced_count", "2")]),
        OrderedDict([("matching_id", "3"), ("top_priced_count", "3")]),
    ],
}


def test_get_top_products_rows():
    assert get_top_products_rows(input_dicts) == [
        [
            "matching_id",
            "total_price",
            "avg_price",
            "currency",
            "ignored_products_count",
        ],
        ["1", 12285.0, 6142.5, "PLN", 1],
        ["2", 28350.0, 14175.0, "PLN", 0],
        ["3", 27720.0, 9240.0, "PLN", 1],
    ]
