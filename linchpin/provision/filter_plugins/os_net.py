#!/usr/bin/env python


def format_networks(networks):
    # "net-name=atomic-e2e-jenkins-test,net-name=atomic-e2e-jenkins-test2"
    nics = ["net-name={0}".format(net) for net in networks]
    nics = ",".join(nics)
    return str(nics)


class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'os_net': format_networks
        }
