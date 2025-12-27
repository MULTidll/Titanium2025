import os
from cashfree_pg.api_client import Cashfree

Cashfree.XClientId = os.getenv('CASHFREE_CLIENT_ID')
Cashfree.XClientSecret = os.getenv('CASHFREE_CLIENT_SECRET')
Cashfree.XEnvironment = Cashfree.SANDBOX