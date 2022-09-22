import csv
import json

ads = "ads.csv"
ads_json = "ads.json"
categories = "categories.csv"
categories_json = "categories.json"
location = "location.csv"
location_json = "location.json"
user = "user.csv"
user_json = "user.json"


def convert(csv_file, model_name, json_file):
    result = []
    with open(csv_file, encoding="utf-8") as csvf:
        for row in csv.DictReader(csvf):
            added = {"model": model_name, "pk": int(row["id"]), "fields": row}
            del row["id"]
            # if row["is_published"] == "True":
            #     row["is_published"] = True
            # else:
            #     row["is_published"] = False
            # row["price"] = int(row["price"])
            # added["fields"] = row
            result.append(added)

    with open(json_file, "w", encoding="utf-8") as jsf:
        jsf.write(json.dumps(result, ensure_ascii=False))


# convert(ads, "ads.ad", ads_json)
convert(user, "ads.user", user_json)

