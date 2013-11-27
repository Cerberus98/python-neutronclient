import logging

from neutronclient.neutron import v2_0 as neutronV20


class ExtensionList(neutronV20.ListCommand):
    def get_data(self, parsed_args):
        neutron_client = self.get_client()
        response = neutron_client.list(self.resource, self.resource_path,
                                       retrieve_all=True)
        return self.setup_columns(response[self.resource], parsed_args)


class MacAddressList(ExtensionList):
    resource = "mac_addresses"
    resource_path = "/%s" % resource
    list_columns = ["id", "address"]
    pagination_support = False
    _formatters = {}
    sorting_support = False
    log = logging.getLogger(__name__ + '.ListMacAddresses')


class MacAddressRangeList(ExtensionList):
    resource = "mac_address_ranges"
    resource_path = "/%s" % resource
    list_columns = ["id", "cidr"]
    pagination_support = False
    _formatters = {}
    sorting_support = False
    log = logging.getLogger(__name__ + '.ListMacAddressRanges')


class RoutesList(ExtensionList):
    resource = "routes"
    resource_path = "/%s" % resource
    list_columns = ["id", "subnet_id", "cidr", "gateway"]
    pagination_support = False
    _formatters = {}
    sorting_support = False
    log = logging.getLogger(__name__ + '.ListRoutes')


class IpPolicyList(ExtensionList):
    resource = "ip_policies"
    resource_path = "/%s" % resource
    list_columns = ["id", "tenant_id", "name", "subnet_ids", "network_ids",
                    "exclude"]
    pagination_support = False
    _formatters = {}
    sorting_support = False
    log = logging.getLogger(__name__ + '.ListRoutes')


EXTENSIONS = {
    "mac-list": MacAddressList,
    "mac-range-list": MacAddressRangeList,
    "route-list": RoutesList,
    "ip-policy-list": IpPolicyList
}
