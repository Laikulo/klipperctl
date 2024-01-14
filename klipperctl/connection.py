import socket

class KlippyConnection(object):
    @staticmethod
    def get(url):
        # Extract scheme from URL, then extract params for a type, and return the correct one
        pass

class BaseConnection(object):
    # This represents a type of connection to Klippy's API, over different underlying methods
    
    def __init__(self):
        pass

    def connect(self):
        pass

    def _do_rpc(self):
        pass

    def run_gcode(self, commands: List[str]):
        pass

    def get_moonraker(self):
        return None

    ## TODO some stuff for managing printer objects


class LocalSocketConnection(BaseConnection):
    # This represents using a local socket to connect to klipper.
    def __init__(self, path: str):
        self.__socket_path = path
        self.__socket = None

    def connect():
        self.__socket = socket.socket(family=AF_UNIX, type=SOCK_STREAM)
        try:
            self__socket.connect(path)
        except as e:
            logging.error(f"Unable to connect to local socket at {self.__socket_path}", e)
            return False
        return True

class TCPSocketConnection(BaseConnection):
    # This represents using a tcp socket to connect to klipper.
    def __init__(self, host, port):
        self.__socket = None
        self.__host = host
        self.__port = port
    pass

    def connect()
        self.__socket = socket.socket(family=AF_INET, type=SOCK_STREAM)
        try:
            self__socket.connect((host, port))
        except as e:
            logging.error(f"Unable to connect to remote socket at {self.__host}:{self.__port}", e)
            return False
        return True

class TCP6SocketConnection(BaseConnection):
    # This represents using a tcp socket to connect to klipper.
    def __init__(self, host, port):
        self.__socket = None
        self.__host = host
        self.__port = port
    pass

    def connect()
        self.__socket = socket.socket(family=AF_INET6, type=SOCK_STREAM)
        try:
            self__socket.connect((host, port))
        except as e:
            logging.error(f"Unable to connect to remote socket at {self.__host}:{self.__port}", e)
            return False
        return True

class WebSocketConnection(BaseConnection):
    # This represents using a raw websocket to connect to klipper. (not moonraker)
    pass

class MoonrakerBaseConnection(BaseConnection):
    # This represents connecting using moonraker's "bridge" socket.
    # This will eventually have some moonraker-specific features
    pass

class MoonrakerHTTPConnection(MoonrakerBaseConnection):
    pass

class MoonrakerLocalConnection(MoonrakerBaseConnection):
    pass
