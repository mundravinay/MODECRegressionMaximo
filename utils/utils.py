# CONSTANTS
import inspect

URL = "https://maximo.srosolutions.net/maximo/webclient/login/login.jsp"
USERNAME = "VINAY.MUNDRA@SROSOLUTIONS.NET"
PASSWORD = "S@tyam2345"


def whoami():
    return inspect.stack()[1][3]
