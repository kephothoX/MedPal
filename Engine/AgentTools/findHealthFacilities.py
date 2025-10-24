import requests, os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

load_dotenv()


client = Elasticsearch(
    f"{os.environ.get('ELASTIC_SEARCH_URL')}",
    api_key=f"{os.environ.get('MEDPAL_API_KEY')}",
)

index_name = "medical_servvices"


def getHealthFacilityByName(facility_name: str) -> list:
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


def getHealthFacilityByPhoneNumber(phone_number: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "phone_number_semantic",
                                "query": phone_number,
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


def getHealthFacilityByEmail(email: str) -> list:
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


def getHealthFacilityHowtoScheduleAppointment(how_to_schedule_appointment: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "how_to_schedule_appointment_semantic",
                                "query": how_to_schedule_appointment,
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


def getHealthFacilityByServices(service_name: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "services_offered__semantic",
                                "query": service_name,
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


def getHealthFacilityByOperationHours(operation_hours: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "operation_hours_semantic",
                                "query": operation_hours,
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


def getHealthFacilityWeb3Address(web3_address: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "web3_wallet_address_semantic",
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


def getHealthFacilitiesByLocation(location: str) -> list:
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
