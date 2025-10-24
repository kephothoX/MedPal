import requests, os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

load_dotenv()


print(f"Loading environment variables from .env file... {os.environ.get('MEDPAL_API_KEY')}")

client = Elasticsearch(
    "https://kephotho-solutions-project-e7d21a.es.us-central1.gcp.elastic.cloud:443",
    api_key=f"{os.environ.get('MEDPAL_API_KEY')}",
)

index_name = "health_facilities"  # Replace with your index name


retriever_object = {
    "rrf": {
        "retrievers": [
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "Health Facility Name_semantic",
                            "query": "kenyatta national hospital"
                        }
                    }
                }
            },
            
        ]
    }
}

search_response = client.search(
    index="health_facilities",
    retriever=retriever_object,
)
print(search_response['hits']['hits'])

