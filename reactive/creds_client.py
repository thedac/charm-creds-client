from charms.reactive import when, when_not, set_state

@when('keystone-credentials.connected')
@when_not('keystone-credentials.available.auth')
def request_creds(keystone):
    keystone.request_credentials(
        "kubadmin",
        "kubinfra",
        requested_grants="Admin"
        domain="kubernetes")


@when('keystone-credentials.available.auth')
def render(keystone):
    pass
