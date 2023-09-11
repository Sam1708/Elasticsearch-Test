import argparse
import csv
import json
from elasticsearch import Elasticsearch, helpers

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--csv_file", required=True, help="path to CSV file")
parser.add_argument("--host", default="localhost", help="Elasticsearch host")
parser.add_argument("--port", default="9200", help="Elasticsearch port")
parser.add_argument("--index", required=True, help="Elasticsearch index name")
args = parser.parse_args()

# Connect to Elasticsearch
es = Elasticsearch([
    {
        'host': 'localhost',
        'port': 9200,
        'scheme': 'http'
    }
])

# Read CSV file and insert data into Elasticsearch
# with open(args.csv_file) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         es.index(index=args.index, body=row)


upload_list = []  # list of items for upload

# Load all csv data
with open(args.csv_file, newline='') as csvfile:

    data_list = []

    csv_data = csv.reader(csvfile)
    for row in csv_data:
        data_list.append(row)

    # separate out the headers from the main data
    headers = data_list[0]
    # drop headers from data_list
    data_list.pop(0)

    for item in data_list:  # iterate over each row/item in the csv

        item_dict = {}

        # match a column header to the row data for an item
        i = 0
        for header in headers:
            item_dict[header] = item[i]
            i = i+1

        # add the transformed item/row to a list of dicts
        upload_list += [item_dict]

# using helper library's Bulk API to index list of Elasticsearch docs
try:
    if not es.indices.exists(args.index):
        with open("mapping.json", "r") as f:
            mapping = json.load(f)

        es.indices.create(index=args.index, body=mapping)

    resp = helpers.bulk(
        es,
        upload_list,
        index=args.index
    )
    msg = "helpers.bulk() RESPONSE: " + str(resp)
    print(msg)  # print the response returned by Elasticsearch
except Exception as err:
    msg = "Elasticsearch helpers.bulk() ERROR: " + str(err)
    print(msg)
    # sys.exit(1)
