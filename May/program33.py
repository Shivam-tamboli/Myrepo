#Json - Java script object notation
import json
data = '{"var1":"shivam", "var2":"satyam"}'
print(data)  # I can print data

parsed = json.loads(data)
print(parsed['var2'])
# I can accsses value

