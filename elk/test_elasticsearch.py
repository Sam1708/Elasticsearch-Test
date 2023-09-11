from elasticsearch import Elasticsearch, exceptions

# es = Elasticsearch([
#     {
#         'host': 'elasticsearch',
#         'port': 9200,
#         'scheme': 'http'
#     }
# ])
es = Elasticsearch([
    {
        'host': 'elasticsearch',
        'port': 9200,
        'scheme': 'http'
    }
])

try:
    if es.ping():
        print('Elasticsearch is running.')
    else:
        print('Could not connect to Elasticsearch.')
except exceptions.ConnectionError as e:
    print('Could not connect to Elasticsearch.',e)


