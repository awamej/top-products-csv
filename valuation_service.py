import csv
from decimal import *


def get_data_from_csv(filename):
    with open(f"{filename}.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
    return list(reader)


def get_matching_products(data, matching_id):
    return [product for product in data if product["matching_id"] == matching_id]


def get_top_priced(currencies, products, top_priced_count):
    total_prices = []
    exchange_ratios = {row["currency"]: Decimal(row["ratio"]) for row in currencies}
    for product in products:
        total_price_currency = int(product["price"]) * int(product["quantity"])
        total_price_PLN = total_price_currency * exchange_ratios[product["currency"]]
        total_prices.append(total_price_PLN)
    total_prices.sort(reverse=True)
    return total_prices[:top_priced_count]


def get_top_products_rows(input_dicts):
    top_products_rows = [
        [
            "matching_id",
            "total_price",
            "avg_price",
            "currency",
            "ignored_products_count",
        ]
    ]
    for match in input_dicts["matchings"]:
        matching_id = match["matching_id"]
        top_priced_count = int(match["top_priced_count"])
        products = get_matching_products(input_dicts["data"], matching_id)
        top_priced = get_top_priced(
            input_dicts["currencies"], products, top_priced_count
        )
        ignored_products_count = len(products) - len(top_priced)
        total_price = sum(top_priced)
        avg_price = round(total_price / top_priced_count, 2)
        top_products_rows.append(
            [
                matching_id,
                total_price,
                avg_price,
                "PLN",
                ignored_products_count,
            ]
        )
    return top_products_rows


def save_data_to_csv(top_products_rows):
    with open("top_products.csv", "w+", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in top_products_rows:
            writer.writerow(row)


if __name__ == "__main__":
    input_dicts = {
        "currencies": get_data_from_csv("currencies"),
        "data": get_data_from_csv("data"),
        "matchings": get_data_from_csv("matchings"),
    }
    top_products_rows = get_top_products_rows(input_dicts)
    save_data_to_csv(top_products_rows)
