#Regular Expression 
import re

mystr = ''' 

Security personnel are maintaining strict vigil at the border points and extra pickets 

have been put up to prevent any untoward incident, Delhi Police officials said.Security has 

been tightened, extra police personnel have been deployed and we have also set up extra pickets at Delhi's borders.


We want to ensure that law and order is maintained and no untoward incident takes place. 

This has been done as a precautionary measure, a senior police officer said, as per news agency ANI.

 Vehicles entering Delhi from neighbouring states are being checked at the borders, he said.

 The SKM, an umbrella body of farmers' unions, had on Tuesday called for nationwide protests on June 1 in s

upport of wrestlers who have been demanding the arrest of Singh for allegedly sexually harassing female grapplers,

'''

# It contains functions like - findall,search,split,sub,finditer

# patt = re.compile(r'who')
# patt = re.compile(r'.')  #Any character
patt = re.compile(r'')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[720:723])
