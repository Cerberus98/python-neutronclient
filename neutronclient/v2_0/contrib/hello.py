import logging

from neutronclient.neutron import v2_0 as neutronV20


class MacAddressList(neutronV20.ListCommand):
    resource = "mac_addresses"
    list_columns = ["id", "address"]
    pagination_support = False
    _formatters = {}
    sorting_support = False
    log = logging.getLogger(__name__ + '.ListMacAddresses')

    def get_data(self, parsed_args):
        return self.list_columns, [("Dongs", "totes")]


EXTENSIONS = {
    "mac-list": MacAddressList
}
