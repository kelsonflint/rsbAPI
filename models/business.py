class Business:
    def __init__(
        self,
        id,
        userId,
        businessName,
        address,
        naics,
        numEmployees,
        timeInBusiness,
        annualRevenue,
        languagePref,
        ownerDemographics,
        reasonsForFunding,
        amountRequested,
        fundingTimeline,
        poc
    ):
        self.id = id
        self.userId = userId
        self.businessName = businessName
        self.address = address
        self.naics = naics
        self.numEmployees = numEmployees
        self.timeInBusiness = timeInBusiness
        self.annualRevenue = annualRevenue
        self.languagePref = languagePref
        self.ownerDemographics = ownerDemographics
        self.reasonsForFunding = reasonsForFunding
        self.amountRequested = amountRequested
        self.fundingTimeline = fundingTimeline
        self.poc = poc