import os
from beautifulhue.api import Bridge

#WARNING: Adjust this to your local settings
bridge = Bridge(device={'ip':'10.0.0.26'}, user={'name':os.environ['HUEBRIDGE']})

# get the current setting of the lights
lights = bridge.light.get({'which':'all'})

# check if at least one light is on
def is_light_on(lights):
    is_on = False
    for light in lights['resource']:
        is_on = is_on or light['state']['on']
    return is_on

def switch_lights():
    global lights
    current_lights = bridge.light.get({'which':'all'})
    #if at least one light is on, we switch all lights off
    if is_light_on(current_lights):
        # store the current state of the lights
        lights = current_lights
        for light in current_lights['resource']:
            resource = {
                'which':light['id'],
                'data':{
                    'state':{'on':False}
                }
            }
            bridge.light.update(resource)
    else:
        # if there was at least one light on in the
        # previous config, we restore it. 
        # Otherwise we switch all lights on.
        if is_light_on(lights):
            for light in lights['resource']:
                resource = {
                    'which':light['id'],
                    'data':{
                        'state':light['state']
                    }
                }
                bridge.light.update(resource)
        else:
            for light in current_lights['resource']:
                resource = {
                    'which':light['id'],
                    'data':{
                        'state':{'on':True}
                    }
                }
                bridge.light.update(resource)
 

if __name__ == "__main__":
    # for testing only
    switch_lights()
    switch_lights()
