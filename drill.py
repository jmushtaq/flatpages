

true = 'true'
d = [{"children":[{"type":"label","name":"importantInformationLabel","label":"This is the information shown to the proponent. This text can be changed in the proposal definition and can include <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">hyperlinks</a>."},{"type":"label","name":"importantInformationLabel2","label":"This is the second label showing in the first box with helpful information."}],"type":"section","name":"importantInformationSection","label":"Click here to show important information"},{"children":[{"name":"Region","label":"Select the region(s) and/or district(s)","isRegionColumnForDashboard":true,"help_text":"The help text for the regions question","type":"multi-select","options":[{"value":"Kimberley (Region)","label":"Kimberley (Region)"},{"value":"East Kimberley (District)","label":"East Kimberley (District)"},{"value":"West Kimberley (District)","label":"West Kimberley (District)"}]},{"name":"Activity","label":"Select the activity for this proposal","help_text":"Select the activity you want to submit a proposal for","isActivityColumnForDashboard":true,"type":"select","options":[{"value":"PublicUtilities","label":"Public Utilities"},{"value":"NativeForestHarvesting","label":"Native Forest Harvesting"},{"value":"LogSalvage","label":"Log Salvage"}]}],"type":"section","name":"regionActivitySection","label":"Region and Activity"},{"children":[{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text","name":"Section0-0","isTitleColumnForDashboard":true,"label":"Enter the title of this proposal"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text_area","name":"Section0-1","label":"Enter the purpose of this proposal"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text_area","name":"Section0-2","label":"In which Local Government Authority (LAG) is this proposal located?"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text_area","name":"Section0-3","label":"Describe where this proposal is located"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text_area","name":"Section0-4","label":"What is the predominant species/vegetation type?"},{"type":"date","name":"Section0-5","label":"Enter the proposal timeframe - start date"},{"type":"date","name":"Section0-6","label":"Enter the proposal timeframe - end date"},{"type":"text","name":"Section0-7","label":"Enter the duration of the proposed activity (days, months or years)"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text","name":"Section0-8","label":"What is the maximum area impacted by the proposal (hectares or linear distance (specify distance))"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text","name":"Section0-9","label":"Who is the supervisor responsible for supervising on-ground implementation of this proposal?"},{"name":"Section0-10","type":"radiobuttons","label":"Will the proposal be monitored?","help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","conditions":{"yes":[{"children":[{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"file","name":"Section0-10-Yes1","label":"Attach a monitoring plan"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","type":"text_area","name":"Section0-10-Yes2","label":"Provide details"},{"help_text":"Click <a href=\"http://www.dbca.wa.gov.au\" target=\"_blank\">here</a> for more information","canBeEditedByAssessor":true,"type":"text_area","name":"Section0-10-Yes3","label":"Specify management condiderations/requirements"}],"type":"group","name":"Section0-10-YesGroup","label":""}]},"options":[{"value":"yes","label":"Yes"},{"value":"no","label":"No"}]}],"type":"section","name":"proposalSummarySection","label":"Proposal Summary"}]


def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

if __name__ == '__main__':
    """ to run:
            python drill.py
    """
    for l in d:
        print list(find('help_text', l))

