# About

This is a sample implementation that uses Cumulocity's Notification2 API to subscribe to all Updates of all Devices within a Tenant. It is using only 1 subscriber for consuming the messages, for high-load scenarios consider using multiple (shard) subscribers. 

The project is using the [Cumulocity Python Client](https://github.com/Cumulocity-IoT/cumulocity-python-api/tree/main), see also the Notification examples there in the "samples" folder. 