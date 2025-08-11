# --- About ---
# Deleting a subscription will stop forwarding data to the registered subscribers
# It will not delete the consumers backlog. So make sure to also execute step 03 (or consume all data) for proper cleanup.

from c8y_api.app import SimpleCumulocityApp
from c8y_api.model import Subscription

subscription_name = 'mySubscription'

def main():
    c8y = SimpleCumulocityApp()
    print("CumulocityApp initialized.")
    print(f"{c8y.base_url}, Tenant: {c8y.tenant_id}, User:{c8y.username}")

    subscriptions = c8y.notification2_subscriptions.get_all(context = 'mo', subscription = subscription_name)

    for subscription in subscriptions:
        subscription.delete()
        print(f"Deleted subscription: {subscription}")

main()
