# Mqtt DSMR parser
This is a python app that listens for mqtt messages containing DSMR smart meter datagrams, parses them into usable data, and sends that data over to a [dsmr-reader](https://github.com/dsmrreader/dsmr-reader) compatible api.

Credits to the [dsmr_parser](https://github.com/ndokter/dsmr_parser) for providing a parsing application.