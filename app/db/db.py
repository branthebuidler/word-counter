from msgpack import Packer, Unpacker


class WordData:

    class _MessagePack(object):

        def __init__(self, app):
            self.app = app
            try:
                open(self.app.config['PERSISTENCE_FILE'])
            except FileNotFoundError:
                self.persist({})
            self.in_mem = self._open_persistence()

        def open(self):
            return self.in_mem

        def _open_persistence(self):
            cfg = self.app.config
            unpacker = Unpacker(open(cfg['PERSISTENCE_FILE'], 'rb'))
            for d in unpacker:
                return d

        def persist(self, dictionary):
            cfg = self.app.config
            packer = Packer()
            with open(cfg['PERSISTENCE_FILE'], 'wb') as fh:
                fh.write(packer.pack(dictionary))

    def init_app(self, app):
        if 'PERSISTENCE_FILE' not in app.config:
            raise RuntimeError("PERSISTENCE_FILE is required in configuration.")
        app.extensions['db'] = self._MessagePack(app)








