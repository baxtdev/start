import uuid
 
random_uuid = uuid.uuid4()
 
print(random_uuid)

 
name_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
 
print(name_uuid)