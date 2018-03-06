import json
import jworks

p1 = jworks.geo("tag", "descrption", "creator", "date", "found", "cache")
print(p1.formatTag())
#jworks.appendTag(,"taco")
yes = {}
yes = {  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}
#jworks.appendTag(yes, "test")
jworks.updateTag("caleb", "taco")

print(jworks.printTags())