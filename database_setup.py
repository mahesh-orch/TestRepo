# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.A

"""
Module contain database set up and teardown related functionality.
"""

from __future__ import absolute_import
from oslo_config import cfg
import binascii
import base64
import hashlib
import configparser
#from Cryptodome.Cipher import AES
from Crypto.Cipher import AES

from st2common.models import db
from st2common.persistence import db_init

__all__ = [
    'db_config',
    'db_setup',
    'db_teardown'
]


def decrypt_password(enc_password):
    openssl_output_b64 = enc_password
    # password_key = getattr(cfg.CONF.keys, 'secret_key', None)
    config = configparser.ConfigParser()
    readConfig = config.read('/etc/st2/st2.conf')
    section = config.sections()

    if 'database' in section:
        password_key = config['keys']['secret_key']

    pbkdf2_iterations = 10000
    openssl_output_bytes = base64.b64decode(openssl_output_b64)
    password_bytes = password_key.encode('utf-8')
    # salt is bytes 8 through 15 of openssl_output_bytes
    salt = openssl_output_bytes[8:16]
    derived_key = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, pbkdf2_iterations, 48)
    # key is bytes 0-31 of derived_key, iv is bytes 32-47 of derived_key
    key = derived_key[0:32]
    iv = derived_key[32:48]
    cipher_text = openssl_output_bytes[16:]
    # decrypt cipher_text using aes-cbc, given key, iv, and cipher_text
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    plain_text = decryptor.decrypt(cipher_text)
    encoded_password = plain_text[:-plain_text[-1]]
    plaintext_password = encoded_password.decode('utf-8')
    mongodb_password = plaintext_password[:len(plaintext_password)-1]
    return mongodb_password


def db_config():
    username = getattr(cfg.CONF.database, 'username', None)
    # password = getattr(cfg.CONF.database, 'password', None)
    enc_password = getattr(cfg.CONF.database, 'password', None)
    if enc_password:
        password = decrypt_password(enc_password)
    else:
        password = None
    return {'db_name': cfg.CONF.database.db_name,
            'db_host': cfg.CONF.database.host,
            'db_port': cfg.CONF.database.port,
            'username': username,
            'password': password,
            'ssl': cfg.CONF.database.ssl,
            'ssl_keyfile': cfg.CONF.database.ssl_keyfile,
            'ssl_certfile': cfg.CONF.database.ssl_certfile,
            'ssl_cert_reqs': cfg.CONF.database.ssl_cert_reqs,
            'ssl_ca_certs': cfg.CONF.database.ssl_ca_certs,
            'authentication_mechanism': cfg.CONF.database.authentication_mechanism,
            'ssl_match_hostname': cfg.CONF.database.ssl_match_hostname}


def db_setup(ensure_indexes=True):
    """
    Creates the database and indexes (optional).
    """
    db_cfg = db_config()
    db_cfg['ensure_indexes'] = ensure_indexes
    connection = db_init.db_setup_with_retry(**db_cfg)
    return connection


def db_teardown():
    """
    Disconnects from the database.
    """
    return db.db_teardown()

