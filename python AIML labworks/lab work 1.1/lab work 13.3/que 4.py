import uuid

orders = []

for i in range(2):
    orders.append(uuid.uuid4())

print("Order IDs:", orders)


# output:-

# Order IDs:
#  [UUID('d4c9ef82-542d-4127-b107-bb4e7ce6b3cd'),
#  UUID('ce2be6d6-c24b-4e5f-a9b7-ede5b094d03b')]

