import json
import os
import sys
from bss.gigya import GigyaClient

try:
    user_id = sys.argv[1]
    info = GigyaClient(os.environ.get('P_G_AKEY')).get_account_info(user_id)
    user = """
    Gigya UID: {uid}
    Premium: {premium}
    """.format(uid=info['UID'], premium='authorization' in info['data'])
    print(user)
except Exception as e:
    print('No user found with that email address.')
