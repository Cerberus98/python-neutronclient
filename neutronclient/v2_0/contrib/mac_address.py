from neutronclient.common import extension


class MacAddressRangeList(extension.ExtensionList):
    """(Admin-only) List all MAC Address Ranges."""
    resource = "mac_address_range"
    resource_plural = "%ses" % (resource)
    resource_path = "/%s" % resource_plural
    list_columns = ["id", "cidr"]
    log = extension.NeutronExtension.get_logger('ListMacAddressRanges')


class RoutesList(extension.ExtensionList):
    """List routes all routes for a tenant."""
    resource = "routes"
    resource_path = "/%s" % resource
    list_columns = ["id", "subnet_id", "cidr", "gateway"]
    log = extension.NeutronExtension.get_logger('ListRoutes')


class RoutesCreate(extension.ExtensionCreate):
    """Create a new route for a given subnet."""
    resource = "route"
    resource_plural = "%ss" % (resource)
    resource_path = "/%s" % resource_plural
    log = extension.NeutronExtension.get_logger('CreateRoute')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnet_id', metavar='SUBNET_ID',
            help='Subnet ID to associate the route with')
        parser.add_argument(
            'cidr', metavar='CIDR',
            help='CIDR mask for the route')
        parser.add_argument(
            'gateway', metavar='GATEWAY',
            help='Destination gateway for the route')

    def args2body(self, parsed_args):
        body = {self.resource: {
            'cidr': parsed_args.cidr,
            'subnet_id': parsed_args.subnet_id,
            'gateway': parsed_args.gateway}, }
        return body


class RoutesDelete(extension.ExtensionDelete):
    """Deletes a route by id."""
    resource = "route"
    resource_plural = "%ss" % (resource)
    resource_path = "/%s" % resource_plural
    log = extension.NeutronExtension.get_logger('DeleteRoute')


class IpPolicyList(extension.ExtensionList):
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    list_columns = ["id", "tenant_id", "name", "subnet_ids", "network_ids",
                    "exclude"]
    log = extension.NeutronExtension.get_logger('ListRoutes')


class IpPolicyCreate(extension.ExtensionList):
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    log = extension.NeutronExtension.get_logger('ListRoutes')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnet_id', metavar='SUBNET_ID',
            help='Subnet ID to associate the route with')
        parser.add_argument(
            'cidr', metavar='CIDR',
            help='CIDR mask for the route')
        parser.add_argument(
            'gateway', metavar='GATEWAY',
            help='Destination gateway for the route')

    def args2body(self, parsed_args):
        body = {self.resource: {
            'cidr': parsed_args.cidr,
            'subnet_id': parsed_args.subnet_id,
            'gateway': parsed_args.gateway}, }
        return body


class IpPolicyDelete(extension.ExtensionDelete):
    """Deletes a route by id."""
    resource = "ip_policy"
    resource_plural = "ip_policies"
    resource_path = "/%s" % resource_plural
    log = extension.NeutronExtension.get_logger('DeleteIpPolicy')


EXTENSIONS = {
    "mac-range-list": MacAddressRangeList,
    "route-list": RoutesList,
    "ip-policy-list": IpPolicyList,
    "ip-policy-create": IpPolicyCreate,
    "ip-policy-delete": IpPolicyDelete,
    "route-create": RoutesCreate,
    "route-delete": RoutesDelete,
}
