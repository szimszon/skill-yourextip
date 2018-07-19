from opsdroid.matchers import match_regex
import logging
import dns.resolver

def setup(opsdroid):
    logging.debug("Loaded yourextip module")

@match_regex(r'what is your (public|external|internet) ip', case_sensitive=False)
async def hello(opsdroid, config, message):
    resolver_domain_for_query_external_ip = config.get("resolver_for_externa_ip","resolver1.opendns.com")
    domain_name_to_query_for_external_ip = config.get("domain_name_for_external_ip","myip.opendns.com")
    resolver=dns.resolver.Resolver()
    resolver_for_external_ip = resolver.query(resolver_domain_for_query_external_ip,'a').rrset[0]
    resolver.nameservers = [str(resolver_for_external_ip)]
    my_external_ip = resolver.query(domain_name_to_query_for_external_ip).rrset[0]
    text="My Internet facing IP address is " + str(my_external_ip) + " ."
    await message.respond(text)

