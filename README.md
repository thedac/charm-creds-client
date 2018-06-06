# Overview

Cleint charm to excercise the keystone credentials interface:

https://github.com/openstack/charm-interface-keystone-credentials/

# Usage

Creds-client relates to keystone via the keystone-credentials interface.


    # Build the charm
    cd creds-client
    charm build -s $SERIES
    cd $SERIES/creds-client

    # Deploy the charm
    juju deploy .
    juju deploy keystone
    juju deploy percona-cluster
    juju add-relation creds-client keystone
