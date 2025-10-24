import requests, os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

load_dotenv()


client = Elasticsearch(
    f"{os.environ.get('ELASTIC_SEARCH_URL')}",
    api_key=f"{os.environ.get('MEDPAL_API_KEY')}",
)

index_name = "medical_services_professionals"


def getHealthProfessionalByName(name: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {"field": "Doctor Name_semantic", "query": name}
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


def getHealthProfessionalByEmail(email: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {"field": "Email_semantic", "query": email}
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


def getHealthProfessionalHealthFacility(facility: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "Health Facility_semantic",
                                "query": facility,
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


def getHealthProfessionalByQualifications(qualification: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "Qualifications_semantic",
                                "query": qualification,
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


def getHealthProfessionalBySpeciality(speciality: str) -> list:
    retriever_object = {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "semantic": {
                                "field": "Specialty_semantic",
                                "query": speciality,
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
