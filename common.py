from st2common.database_setup import decrypt_password

enc_password = (
            cfg.CONF.database.password
            if hasattr(cfg.CONF.database, "password")
            else None
        )
        if enc_password:
            password = decrypt_password(enc_password)
        else:
            password = None

# This is new line added just for testing

# added new line in branch1
