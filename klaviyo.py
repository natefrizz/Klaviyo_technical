from klaviyo_sdk import Client

client = Client( "pk_d8e46abcf322eb61dcf2c2181fe5e6ebb3", max_delay=60, max_retries=3)
# This is example variable data that would be passed through; region data.
myState= "Vermont"
# Mock data from purchasing an IV, gathering these details will help route an appropriate Flow
data={
  "token": "SCQAHx",
  "event": "Bought Reboot IV",
  "customer_properties": {
    "$email": "mike@mikefeelsgood.com",
    "$first_name": "Mike",
    "$last_name": "Smith",
    "$phone_number": "+16033375537",
    "$consent": "sms",
    "$region": myState
  },
  "properties": {
    "IV": "Reboot",
    "Reason": "hangover"
  }
}

client.TrackIdentify.track_post(data=data)
# Adding the 0.1v of using state data to compile/create lists per region. DO NOT add users to lists automatically, however, a flow can later nurture clients into respective lists. More in readme.txt
if myState == "New Hampshire":
    client.Campaigns.create_campaign(list_id="TH35xK", template_id='RA6aDG', from_email='mariah@originwellnessco.co', from_name='Mariah', subject='New Hampshire?! Us too!', name="NH!")
# Massachusetts and Vermont are two states that would be rolled out next in business use case; capturing if users inquire FROM those states to create the list; will add users to said list in a later flow/opt-in.
if myState == "Massachusetts":
    client.Campaigns.create_campaign(list_id="TH35xK", template_id='RA6aDG', from_email='mariah@originwellnessco.co', from_name='Mariah', subject='Massachusetts?! Coming soon!', name="MA - List"),
elif myState == "Vermont":
    client.Campaigns.create_campaign(list_id="TH35xK", template_id='RA6aDG', from_email='mariah@originwellnessco.co', from_name='Mariah', subject='Vermont?! Coming soon!', name="Vermont - List"),
else:
    print()
