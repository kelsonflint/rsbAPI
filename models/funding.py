class Funding:
    def __init__(
        self,
        id,
        fundingName,
        fundingType,
        provider,
        url,
        startDate,
        endDate,
        uses,
        description,
        terms,
        qualifications
    ):
        self.id = id
        self.fundingName = fundingName
        self.fundingType = fundingType
        self.provder = provider
        self.url = url
        self.startDate = startDate
        self.endDate = endDate
        self.uses = uses
        self.description = description
        self.terms = terms
        self.qualifications = qualifications