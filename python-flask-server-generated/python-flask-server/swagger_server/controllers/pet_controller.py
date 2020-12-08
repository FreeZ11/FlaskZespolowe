import connexion
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util
pets = []


def add_pet(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())
    pets.append(body)

      # noqa: E501
    return 'successuflly added new pet'


def delete_pet(petId, api_key=None):  # noqa: E501
    """Deletes a pet

     # noqa: E501

    :param petId: Pet id to delete
    :type petId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_all():  # noqa: E501
    """Get all pets

     # noqa: E501


    :rtype: None
    """
    pets.sort(key=lambda x: x.id)
    return pets


def get_pet_by_id(petId):  # noqa: E501
    """Find pet by ID

    Returns a single pet # noqa: E501

    :param petId: ID of pet to return
    :type petId: int

    :rtype: Pet

    """
    pets.sort(key=lambda x: x.id)
    return pets[petId-1]
