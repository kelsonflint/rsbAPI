# API Reference

## Routes
### IP address:  http://54.214.55.177:8080 (subject to change)

### USERS
#### '/users'  [GET, POST]
**GET** list of all user objects

**POST** create new user
(userId generated upon creation)

#### '/users/{user_id}' 	[GET, PUT, DELETE]
**GET** specific user

**PUT** update user information

**DELETE** remove user from database

### BUSINESSES
#### '/users/{user_id}/businesses'  [GET, POST]

**GET** all business owned by {user_id}


**POST** create new business for {user_id}

#### '/users/{user_id}/businesses/{business_id}' [GET, PUT, DELETE]
**GET** business w/ {business_id} owned by {user_id}

**PUT** update business w/ {business_id} owned by {user_id}

**DELETE** business w/ {business_id} owned by {user_id}


### FUNDING
#### '/funding'  [GET, POST]

**GET** list of all funding available

**POST** create new funding opportunity

#### '/funding/{funding_id}' [GET, PUT, DELETE]

**GET** funding opportunity with {funding_id}

**PUT** update funding opportunity with {funding_id}

**DELETE** funding opportunity with {funding_id}

### ASSISTANCE
#### '/assistance'  [GET, POST]

**GET** list of all Technical Assistance providers

**POST** create new TA provider


#### '/assistance/{ass_id}' [GET, PUT, DELETE]

**GET** TA provider with {ass_id}

**PUT** update TA provider with {ass_id}

**DELETE** TA provider with {ass_id}


## Major Entities

### User

{
    "id": String,
    "email": String,
    "password": String, (Encrypted)
    "firstName": String,
    "lastName": String
}

### Business

{
	"id": String,
	"userId": String,
	"businessName": String,
	"businessType": String,
	"address": String,
	"naics": Int,
	"numEmployees": Int,
	"timeInBusiness": String,
	"annualRevenue": String,
	"languagePref": String,
	"ownerDemographics": [String],
	"reasonsForFunding": [String],
	"amountRequested": Int,
	"fundingTimeline": String,
	"poc": {
		"firstName": String,
		"lastName": String,
		"phone": String,
		"email": String,
		"prefMethod": String
	}
}

### Funding

{
	"id": String,
	"fundingName": String,
	"fundingType": String,
	"provider": String,
	"website": String",
	"startDate": String, [MM-DD-YY]
	"endDate": String, [MM-DD-YY]
	"uses": [String],
	"description": String,
	"terms": [String],
	"qualifications": {
		"NAICS": [String],
		"maxEmployees": String,
		"isCollateralReq": boolean,
		"establishedBy": String, [MM-DD-YY]
	}
},

### Assistance

{
	"id": String,
	"orgName": String,
	"description": String,
	"website": String,
	"phone": String,
	"email": String,
	"pocName": String,
	"languages": [String],
	"demographics": [String],
	"locations": [String]
}
