from charms.reactive import when, when_not, set_state
import charms.reactive

DOMAIN = "kubernetes"

@when('keystone-credentials.connected')
@when_not('keystone-credentials.available.auth')
def request_creds(keystone):
    keystone.request_credentials(
        "kubadmin",
        "kubinfra",
        requested_grants="Admin",
        domain=DOMAIN)


@when('identity-crentials.available.auth')
def render(keystone):
    print("RECEIVED")
    print(dir(keystone))
    clean ="""_OS_PARAMS=$(env | awk 'BEGIN {FS="="} /^OS_/ {print $1;}' | paste -sd ' ')
    for param in $_OS_PARAMS; do
        unset $param
    done
    unset _OS_PARAMS
    """

    creds = """
    export OS_REGION_NAME=RegionOne
    export OS_AUTH_URL=http://{}:{}/v3
    export OS_USERNAME={}
    export OS_PASSWORD={}
    export OS_PROJECT_NAME={}
    export OS_PROJECT_DOMAIN_NAME={}
    export OS_USER_DOMAIN_NAME={}
    export OS_IDENTITY_API_VERSION={}
    export OS_AUTH_VERSION={}
    """
    rc = clean + creds.format(
        keystone.credentials_host(),
        keystone.credentials_port(),
        keystone.credentials_username(),
        keystone.credentials_password(),
        keystone.credentials_project(),
        DOMAIN,
        DOMAIN,
        keystone.api_version(),
        keystone.api_version())
    print(rc)


@when_not('installed')
def debug():
    print("DEBUG")
    #print(dir(charms.reactive.flags))
    print(charms.reactive.flags.get_flags())
