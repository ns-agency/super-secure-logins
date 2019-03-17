from . import create_app
from werkzeug.debug import DebuggedApplication

app = DebuggedApplication(create_app(), evalex=False)
