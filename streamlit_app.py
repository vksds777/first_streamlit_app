from simple_salesforce import Salesforce
import streamlit
import pandas
import requests
import csv
from io import StringIO
# Sign into Salesforce
#sf = Salesforce(username='user@company.com',password='password',security_token='token')
sf = Salesforce(username='vivek.kumar6.response@timesgroup.com',password='Delta@1234',security_token='csTKM8Vx6qQj0HMMYvINMN9S')
# Set report details
#sf_org = 'https://company.salesforce.com/'
#report_id = 'report_id'
sf_org = 'https://timespulse.lightning.force.com//' #Your Salesforce Instance URL
report_id = '00O7F00000BBMerUAH' # add report id
export_params = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
# Download report
sf_report_url = sf_org + report_id + export_params
response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
#print(response)
new_report = response.content.decode('utf-8')
#new_report = response.content.decode('ISO-8859-1')
#print (new_report)
report_df = pd.read_csv(StringIO(new_report))
#print (report_df)
