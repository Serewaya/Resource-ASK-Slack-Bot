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
def resource_requirements():
	return {
	"type": "modal",
	"callback_id": "output_submit_1",
	"title": {
		"type": "plain_text",
		"text": "Resource Requirements",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Next Step",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Step 1/2",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "In order to find the best resources for you we require some information related to the resource. To see more information related to our resource categorization process check out the <https://serewaya.github.io/resource-ask/resource-categorization/|Resource ASK documentation.>"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"block_id": "category",
			"element": {
				"type": "plain_text_input",
				"action_id": "category",
				"placeholder": {
					"type": "plain_text",
					"text": "Resource Category"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Category",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "The Resource Category is the main aspect you are searching for, try out ‘loans’ to see how it works. You can also check out this <https://serewaya.github.io/resource-ask/avaliable-categories/|Category List> to see all the categories available."
				}
			]
		},
		{
			"type": "input",
			"block_id": "expiration",
			"element": {
				"type": "datepicker",
				"initial_date": "2022-04-20",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				},
				"action_id": "expiration"
			},
			"label": {
				"type": "plain_text",
				"text": "Expiration Date",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "The Resource Expiration Date is the deadline for applications or time period a resource is offered. If you don’t have an expiration date simply leave it as the default value.",
					"emoji": True
				}
			]
		}
	]
}
def output_initial(user_name):
    return [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f'*Welcome to the Output Command {user_name}*'
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This command retrieves listings from the Resource ASK Database.\n\n*Do you want to continue with this command?*\n\n_Please press the yes or no button_"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn-icons.flaticon.com/png/512/874/premium/874728.png?token=exp=1650222216~hmac=ae3e55397ec8c7549d8c6a9ba3d8ffac",
				"alt_text": "computer thumbnail"
			}
		},
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


def user_info():
	return {
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Search Requirements",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "category"
			},
			"label": {
				"type": "plain_text",
				"text": "Category",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "datepicker",
				"initial_date": "2022-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				},
				"action_id": "expiry_date"
			},
			"label": {
				"type": "plain_text",
				"text": "Expiry Date",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Female",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Male",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Other or None",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "gender_selection"
			},
			"label": {
				"type": "plain_text",
				"text": "Label",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "area"
			},
			"label": {
				"type": "plain_text",
				"text": "Area",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit",
						"emoji": True
					},
					"style": "primary",
					"value": "click_me_123",
					"action_id": "submit"
				}
			]
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
				"text": "Here are your search requirements:\n*Please review them and press the approve or deny button to get your results*"
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
					"value": "click_me_123",
					"action_id": "return_results"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"value": "click_me_123",
					"action_id": "dontsearch"
				}
			]
		}
	]
}

def homepage():
	return {"type": "home",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:wave: Hey <@Serewaya>, welcome to your Resource Dashboard*\nHere you can output resources from the Resource ASK database, receive Google search results for resources, and log new resources into the Resource ASK database.\nAlso feel free to click the buttons for more information on how to use the Resource ASK Bot."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": ":gear: Settings"
				},
				"action_id": "open_settings"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Output a Resource:bulb:"
					},
					"style": "primary",
					"action_id": "output_resource"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Google Search :mag_right:"
					},
					"style": "primary",
					"action_id": "google_search"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Log a Resource:technologist::skin-tone-5:"
					},
					"action_id": "expense_external"
				}
			]
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
					"alt_text": "placeholder"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Profile Details*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Serewaya Latif*\nCompany Name: *Resource ASK*\nPosition: *Co-Founder*\nArea: *Ontario, Canada*\nInterests: *Social Justice, Coding, Leadership*\nAbout: I am a grade 11 Student with a mission to help black entrepreneurs gain essential business resources..."
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn-icons-png.flaticon.com/512/921/921124.png",
				"alt_text": "credit card"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "See More",
						"emoji": True
					},
					"value": "1797PD",
					"style": "primary",
					"action_id": "more_info"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Edit Profile",
						"emoji": True
					},
					"value": "1797PD",
					"action_id": "edit_profile"
				}
			]
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "image",
					"image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
					"alt_text": "placeholder"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Connections*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Joe Milton*\nIn: *Pending*\nDate Sent: *04/01/2022*\nMessage: Hi Joe, do you have any business advice for me?"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn-icons-png.flaticon.com/512/1838/1838347.png",
				"alt_text": "plane"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "View Profile"
					},
					"value": "1803PD",
					"action_id": "joes_profile"
				}
			]
		}
	]
}