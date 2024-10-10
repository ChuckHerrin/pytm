from pytm import TM, Server, Dataflow, Datastore, Actor, Boundary
from pytm import Threat
from pytm import AIModel, Dataset

# Load threats
Threat.load_threats()

tm = TM("STRIDE-ATLAS Hybrid Threat Model")
tm.description = "An example threat model integrating STRIDE, ATLAS, and OWASP Top Ten."

# Define boundaries
internet = Boundary("Internet")

# Define elements
user = Actor("User")
user.inBoundary = internet

web_server = Server("Web Server")
web_server.inBoundary = internet

database = Datastore("User Database")
database.inBoundary = internet
database.isEncrypted = True

# AI Components
training_data = Dataset(
    "Training Dataset",
    isPublic=True,
    containsSensitiveData=False,
    isValidated=False
)

ml_model = AIModel(
    "Machine Learning Model",
    isExposed=True,
    isTrainedWithSensitiveData=True,
    hasRobustTraining=False,
    hasInputValidation=False,
    hasOutputFiltering=False,
    authenticatesSource=False
)

# Data Flows
user_to_server = Dataflow(
    source=user,
    sink=web_server,
    data="User Input",
    protocol="HTTPS",
    isEncrypted=True,
    authenticatesSource=True
)

server_to_db = Dataflow(
    source=web_server,
    sink=database,
    data="User Credentials",
    protocol="SQL",
    isEncrypted=True,
    authenticatesSource=True
)

data_to_model = Dataflow(
    source=training_data,
    sink=ml_model,
    data="Training Data",
    protocol="Local",
    isEncrypted=False
)

model_to_user = Dataflow(
    source=ml_model,
    sink=user,
    data="Model Output",
    protocol="HTTPS",
    isEncrypted=True,
    authenticatesSource=False
)

# Process the model
tm.process()

# Generate the report
tm.report()
