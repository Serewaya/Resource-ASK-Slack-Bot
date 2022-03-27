def output_initial():
    return {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Hey there, this command output’s resources from the Resource ASK’s database*\nDo you want to continue searching?\n_Please press the yes or no button._"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
				"alt_text": "computer thumbnail"
			}},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Yes"
					},
					"style": "primary",
					"value": "startoutput",
					"action_id": "startoutput"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "No"
					},
					"style": "danger",
					"value": "stopoutput",
					"action_id": "stopoutput"
				}
			]
		}
	]
}
def output_instructions():
	return {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Great :smile:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "The Resource ASK Bot needs some information to ensure that we are searching for the most relevant resources for you, we will require:\n	➊ Resource or file link\n	➋ Category of resource\n	➌ Time period before expiration\n	➍ Area specifications\n	➎ Gender specifications"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Send a message in the format of _link, category, expiration time, area, gender_ (with a space and a ',' in between each clause) if you don't have any requirements please enter 'none'"
			}
		}
	]
}
def user_entry(link, section, expiration, area, gender):
	return {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Here are your search requirements:\n*<Please review them and press the approve or deny button to get your results>*"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Link: *\n"+str(link)
				},
				{
					"type": "mrkdwn",
					"text": "*Category: *\n"+str(section)
				},
				{
					"type": "mrkdwn",
					"text": "*Expiration Time:*\n"+str(expiration)
				},
				{
					"type": "mrkdwn",
					"text": "*Area:*\n"+str(area)
				},
				{
					"type": "mrkdwn",
					"text": "*Gender:*\n"+str(gender)
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Approve"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
}