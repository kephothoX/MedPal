import requests, os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

load_dotenv()


client = Elasticsearch(
    f"{os.environ.get('ELASTIC_SEARCH_URL')}",
    api_key=f"{os.environ.get('MEDPAL_API_KEY')}",
)

index_name = "health_facilities"


def getDeliveryAgentByName(facility_name: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "name_semantic",
                                "query": facility_name,
                            }
                        }
                    }
                },
            ]
        }
    }

    search_response = client.search(
        index=index_name,
        retriever=retriever_object,
    )
    return search_response["hits"]["hits"]


def getDeliveryAgentByEmail(email: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {"field": "email_semantic", "query": email}
                        }
                    }
                },
            ]
        }
    }

    search_response = client.search(
        index=index_name,
        retriever=retriever_object,
    )
    return search_response["hits"]["hits"]


def getDeliveryAgentByBikeReg(bike_reg: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "bike_reg_semantic",
                                "query": bike_reg,
                            }
                        }
                    }
                },
            ]
        }
    }

    search_response = client.search(
        index=index_name,
        retriever=retriever_object,
    )
    return search_response["hits"]["hits"]


def getDeliveryAgentByLocation(location: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "location_semantic",
                                "query": location,
                            }
                        }
                    }
                },
            ]
        }
    }

    search_response = client.search(
        index=index_name,
        retriever=retriever_object,
    )
    return search_response["hits"]["hits"]
