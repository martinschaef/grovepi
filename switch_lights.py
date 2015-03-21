import time
from beautifulhue.api import Bridge

#WARNING: Adjust this to your local settings
bridge = Bridge(device={'ip':'10.0.0.26'}, user={'name':'your-user-name'})

# check if at least one light is on
def is_light_on():
    resource = {'which':0}
    group = bridge.group.get(resource)
    return bool(group['resource']['action']['on'])



def switch_lights():
    resource = {
        'which':0,
        'data':{
            'action':{'on':is_light_on()}
        }
    }
    bridge.group.update(resource)
 

if __name__ == "__main__":
    # for testing only
    print "Testing the lights"
    resource = {'which':0}
    group = bridge.group.get(resource)
    print group

    print "Is light on? ", is_light_on()
    print "Switching..."

    resource = {
        'which':0,
        'data':{
            'action':{'on':(not is_light_on())}
        }
    }

    bridge.group.update(resource)
    print "Is light on? ", is_light_on()
    time.sleep(1)
    print "Switching back..."

    resource = {
        'which':0,
        'data':{
            'action':{'on':(not is_light_on())}
        }
    }
    bridge.group.update(resource)