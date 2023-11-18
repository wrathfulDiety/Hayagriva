# Happy hunting with Hayagriva!

Hayagriva is a tool designed to aid in bug bounty hunting by extracting and saving IP addresses from BGP routing tables. By identifying and enumerating IP addresses associated with a given organization, Hayagriva can help you uncover potential attack surfaces and uncover hidden vulnerabilities.

# Contributions are welcome!

Hayagriva is an open-source project, and we encourage you to contribute to its development. Whether you're a seasoned programmer or a beginner, your contributions can make a significant impact on the tool's capabilities and usefulness.

# Let's explore the bug bounty hunting potential

  Identify targets: Hayagriva can help you identify potential targets for bug bounty hunting by providing a list of IP addresses associated with a specific organization. This list can be used to focus your efforts on organizations with a higher likelihood of unpatched vulnerabilities.

  Enumerate subdomains and services: Once you have a list of IP addresses, you can use Hayagriva to enumerate subdomains and services running on those IPs. This information can help you identify potential entry points for further exploration.

  Discover hidden attack surfaces: Hayagriva can uncover hidden attack surfaces by identifying IP addresses that are not publicly advertised or easily discoverable. These hidden IPs may be more vulnerable to attack.

  Uncover potential vulnerabilities: By combining Hayagriva's IP address extraction capabilities with other bug bounty hunting tools, you can uncover potential vulnerabilities that may have been overlooked.

Remember, every contribution, no matter how small, can make a big difference in the effectiveness of Hayagriva as a bug bounty hunting tool. So, join us in enhancing this tool and making it even more valuable for the bug bounty hunting community.


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
