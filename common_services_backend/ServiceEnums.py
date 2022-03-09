from enum import Enum


class ServiceType(Enum):
    COVID19_TESTING = 'covid19_test'
    LAWN_SERVICE = 'lawn_service'
    AMBULANCE = 'ambulance'
    CHEMOTHERAPY = 'chemo'
    services = (CHEMOTHERAPY, COVID19_TESTING, LAWN_SERVICE, AMBULANCE)

    @classmethod
    def is_valid(cls, service):
        is_valid = True
        try:
            cls(service.lower())
        except Exception as e:
            print(e, "\nServiceType = ['covid19_test', 'lawn_service', 'ambulance', 'chemo']")
            is_valid = False

        return is_valid


class AVMake(Enum):
    WAYMO = 'waymo'


class AVModel(Enum):
    MED = 'med'
    LM = 'lm'
