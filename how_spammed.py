import sendgrid, json, datetime

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def how_spammed(str_date):
    end_time = datetime.strptime(str_date, '%Y-%m-%d')
    start_time = end_time + datetime.timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
    'end_time':int(end_time.timestamp()),
    'start_time': int(start_time.timestamp())
})

    

    data = json.loads(response.body)
    return len(data)

