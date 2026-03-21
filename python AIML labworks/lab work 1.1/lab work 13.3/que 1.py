import uuid

u1 = uuid.uuid4()
print("Random UUID:", u1)

u2 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print("UUID using namespace:", u2)

# output:-

# Random UUID: c0133df3-6e4e-4922-975e-bef2adb33146
# UUID using namespace: cfbff0d1-9375-5685-968c-48ce8b15ae17

