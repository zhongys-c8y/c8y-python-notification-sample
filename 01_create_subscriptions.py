# --- About ---
# This step is to create a subscription in the platform. 
# It is a mandatory step and describes a datastream that subscribers will be able to consume later in next step
# For this example we will create a subscription with "mo" context for each device of the tenant
# Using the same subscription name enables us to use a single subscriber to consume all data from all devices

from c8y_api.app import SimpleCumulocityApp
from c8y_api.model import ManagedObject, Subscription, DeviceInventory

# Don't use special characters, especially no '-' (API would reject it)
subscription_name = 'mySubscription'

def main():
    c8y = SimpleCumulocityApp()
    print("CumulocityApp initialized")
    print(f"{c8y.base_url}, Tenant: {c8y.tenant_id}, User:{c8y.username}")

    mos = c8y.device_inventory.get_all()
    subs = []
    for mo in mos:
        sub = Subscription(c8y,
                            name=subscription_name,
                            context=Subscription.Context.MANAGED_OBJECT,
                            source_id=mo.id,
                            api_filter=['*'],
                            non_persistent=False).create()
        print(f"Subscription created: {subscription_name} for device {mo.id}")
        subs.append(sub)

main()
