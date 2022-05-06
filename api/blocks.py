
def amount(amount, area, category):
	return{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"We found *{amount} Resources* in *{area}* with the category of *{category}*"
			}
	}
def divider():
	return {
			"type": "divider"
		}
def more_listings():
	return {
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Next Page"
					},
					"value": "click_me_123",
					"action_id":"more_results"
				}
			]
		}
def return_listing(link, title,blurb,  image, expiration):
	return {
	
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*<{link}|{title}>*\n{blurb}\n⏰Expiration Date: {expiration}"
			},
			"accessory": {
				"type": "image",
				"image_url": image,
				"alt_text": "Resource Image"
			}
		}
def location(area):
		return {
			"type": "context",
			"elements": [
				{
					"type": "image",
					"image_url": "https://cdn-icons.flaticon.com/png/512/3038/premium/3038016.png?token=exp=1651327242~hmac=03881fdf93f69e8bd82cc3ca8b2acf5e",
					"alt_text": "Location Pin Icon"
				},
				{
					"type": "plain_text",
					"emoji": True,
					"text": f"Location Constraints: {area}"
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

def personal_information():
	return{
	"title": {
		"type": "plain_text",
		"text": "Personal Information"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Step 2/2",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "To make sure that we are looking for the resources that fit your needs we will need a bit of information related to your identity and where you reside. Resource ASK is an organization that is very purposeful with our user information see this <https://serewaya.github.io/resource-ask/how-we-protect-user-information/|link> to learn how we protect user info."
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"block_id": "area",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select Your Area",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Canada",
							"emoji": True
						},
						"value": "canada"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "United States",
							"emoji": True
						},
						"value": "united states"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Other",
							"emoji": True
						},
						"value": "none"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Area",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "The area is the scope of which we search for resources. It serves  as a crucial part of assessing your eligibility for certain resources in the Resource ASK database."
				}
			]
		},
		{
			"type": "input",
			"block_id": "gender",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select your Gender",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Male",
							"emoji": True
						},
						"value": "male"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Female",
							"emoji": True
						},
						"value": "female"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Other/None",
							"emoji": True
						},
						"value": "none"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Gender",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "Some resources are specific to people of a certain gender. We require your gender to ensure that we are finding only resources that are relevant to you."
				}
			]
		}
	],
	"type": "modal",
	"callback_id": "output_submit_2"
}
def output_initial(user_name):
    return [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f'Hi *{user_name}*, Welcome to the Output Command ⤦'
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<google.com|What is the Output Command?>\nThis command allows for users to search \n through a database of business resources\n and returns listings that meet their requirements."
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn-icons-png.flaticon.com/512/4756/4756496.png",
				"alt_text": "calendar thumbnail"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "image",
					"image_url": "https://cdn-icons.flaticon.com/png/512/4194/premium/4194648.png?token=exp=1651271099~hmac=34044b4ea2a9ffaa25cc1d826fb260d2",
					"alt_text": "notifications warning icon"
				},
				{
					"type": "mrkdwn",
					"text": "Learn more about how to use the output command here"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Do you want to continue with this command?",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Yes",
						"emoji": True
					},
					"style": "primary",
					"action_id": "startoutput"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "No",
						"emoji": True
					},
					"action_id": "stopoutput"
				}
			]
		}
	]



def user_entry(section, expiration, area, gender):
	return [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Here Are Your Resource Requirements",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "Please review them and press the approve or deny button to get your results.",
					"emoji": True
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"fields": [
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
			"type": "divider"
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
					"value": "click_me_123",
					"action_id": "dontsearch"
				}
			]
		}
	]


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