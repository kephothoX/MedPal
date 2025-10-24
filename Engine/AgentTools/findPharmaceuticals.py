import requests, os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

load_dotenv()


client = Elasticsearch(
    f"{os.environ.get('ELASTIC_SEARCH_URL')}",
    api_key=f"{os.environ.get('MEDPAL_API_KEY')}",
)

index_name = "pharmacy_services"


def getPharmaceuticalFacilityByName(facility_name: str) -> list:
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


def getPharmaceuticalMedsByName(med_name: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {"field": "meds_semantic", "query": med_name}
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


def getPharmaceuticalFacilityByLocation(location: str) -> list:
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


def getPharmaceuticalFacilityOperationHours(hrs: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "hours_semantic",
                                "query": hrs,
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


def getPharmaceuticalFacilityPaymentMethods(payment_method: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "web3_address_semantic",
                                "query": payment_method,
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


def getPharmaceuticalFacilityPaymentWeb3Address(web3_address: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "payment_semantic",
                                "query": web3_address,
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


retriever_object = {
    "rrf": {
        "retrievers": [
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "hours_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "location_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "meds_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "name_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "payment_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
            {
                "standard": {
                    "query": {
                        "semantic": {
                            "field": "web3_address_semantic",
                            "query": "REPLACE WITH YOUR QUERY",
                        }
                    }
                }
            },
        ]
    }
}
