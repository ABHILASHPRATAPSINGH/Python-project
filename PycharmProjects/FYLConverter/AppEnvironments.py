import enum

class AppEnvironments(enum.Enum):
    DEVELOPMENT="development"
    TESTING="testing"
    PRE_PRODUCTION="pre_production"
    PRODUCTION="production"