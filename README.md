# azure-ticker
### Display Live Microsoft Azure Services Status on Pimoroni's Unicorn HAT ###

Uses this RSS Feed for Azure Health Status:
https://azure.microsoft.com/en-us/status/feed/<br>
If any of the Azure Services are down it will start scrolling text sourced from the RSS content.

![The Azure Kumbaya!](https://raw.githubusercontent.com/snobu/azure-ticker/master/hatshot/healthy.jpg)


#### Install ####

```bash
$ sudo pip install unicornhat
$ sudo pip install bitarray
$ git clone https://github.com/snobu/azure-ticker
$ cd azure-ticker
$ python ./ticker.py
```
