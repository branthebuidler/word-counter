from msgpack import Packer, Unpacker


class Persistence:

    class _MessagePack(object):
        def __init__(self, app):
            self.app = app
            self.app.teardown_request(self.close)
            try:
                open(self.app.config['PERSISTENCE_FILE'])
            except FileNotFoundError:
                self.write({})

        def open(self):
            handler = self._open_persistence()
            for d in handler:
                return d

        def _open_persistence(self):
            cfg = self.app.config
            unpacker = Unpacker(open(cfg['PERSISTENCE_FILE'], 'rb'))
            return unpacker

        def write(self, dictionary):
            cfg = self.app.config
            packer = Packer()
            with open(cfg['PERSISTENCE_FILE'], 'wb') as fh:
                fh.write(packer.pack(dictionary))

        def close(self, ignore_arg):
            pass

    def init_app(self, app):
        if 'PERSISTENCE_FILE' not in app.config:
            raise RuntimeError("PERSISTENCE_FILE is required in configuration.")
        app.extensions['persistence'] = self._MessagePack(app)








