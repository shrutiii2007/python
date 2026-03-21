import pandas as pd

shipments = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Chennai", "Chennai"],
    "Carrier": ["DHL", "FedEx", "DHL", "FedEx", "DHL", "FedEx"],
    "DeliveryDays": [2, 3, 3, 4, 4, 5]
})

print(shipments)

print("---------------------------------------")

pivot_shipments = pd.pivot_table(
    shipments,
    index="City",
    columns="Carrier",
    values="DeliveryDays",
    aggfunc="mean"
)

print(pivot_shipments)



