from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory


class TLSFlexibleContextFactory(ScrapyClientContextFactory):
    """A more protocol-flexible TLS/SSL context factory.

    A TLS/SSL connection established with [SSLv23_METHOD] may understand
    the SSLv3, TLSv1, TLSv1.1 and TLSv1.2 protocols.
    See https://www.openssl.org/docs/manmaster/ssl/SSL_CTX_new.html
    """

    def __init__(self):
        self.method = SSL.SSLv23_METHOD
