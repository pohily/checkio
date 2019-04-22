import sendgrid

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def best_country(str_date):
    '''
    response = sg.client.geo.stats.get(query_params={
    'start_date':str_date,
    'end_date': str_date
    
})
'''
    response = [{
    'date': '2016-01-01',
    'stats': [
        {
         'type': 'country', 
         'name': 'AT',
         'metrics': {'clicks': 1, 'opens': 1, 'unique_clicks': 1, 'unique_opens': 1}
        },
        {
         'type': 'country',
         'name': 'AU',
         'metrics': {'clicks': 0, 'opens': 31, 'unique_clicks': 0, 'unique_opens': 22}
        }
    ]
}]

    for date in response:
        max_clicks = 0
        for entry in date['stats']:
            if entry['metrics']['clicks'] > max_clicks:
                max_clicks = entry['metrics']['clicks']
                country = entry['name']
    return country




print(best_country('2016-01-01'))
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')
               

'''



