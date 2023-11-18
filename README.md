# Hayagriva
bgp.he.net subnet scraper


# Hayagriva

Hayagriva is a tool for extracting and saving IP addresses from BGP routing tables. It can be used to identify and enumerate IP addresses associated with a given organization.

## Installation

Hayagriva requires the following Python libraries:

* requests
* bs4
* ipaddress
* re

You can install these libraries using pip:

```bash
pip install requests bs4 ipaddress re
```
# Usage

To use Hayagriva, simply run the following command:

python hayagriva.py


You will be prompted to enter the organization name for which you want to extract IP addresses. Hayagriva will then fetch the IP subnets for the organization from BGP.he.net, generate a list of all IP addresses within those subnets, and save the list to a file named `{organization_name}.txt`.

## Example

To extract IP addresses for the organization "google", run the following command:

<img width="329" alt="image" src="https://github.com/wrathfulDiety/Hayagriva/assets/36190613/c1bfc54d-9f67-4fa5-a823-c2cb5eecdcc2">


Hayagriva will fetch the IP subnets for RIPE NCC from BGP.he.net, generate a list of all IP addresses within those subnets, and save the list to a file named `RIPE_NCC.txt`.

## License

Hayagriva is licensed under the MIT License.

## References

* [BGP.he.net](https://bgp.he.net/)
* [IPaddress module](https://docs.python.org/3/library/ipaddress.html)
* [re module](https://docs.python.org/3/library/re.html)
