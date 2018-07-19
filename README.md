# opsdroid skill yourextip

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to respond to what is your external ip.

## Requirements

* dnspython

## Configuration

* resolver_for_external_ip -- you can set up the dns resolver to query for your external ip address, 
    default: resolver1.opendns.com
* domain_name_for_external_ip -- you can set the domain name to query for your external ip address,
    default: myip.opendns.com

## Usage

#### `what is your external ip`

Query for the external IP address.

> user: what is your external ip
>
> opsdroid: My Internet facing IP address is x.y.z.w .
