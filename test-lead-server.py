import json
d = {"loan_type":"mca","first_name":"Test","last_name":"User","business_name":"Test Biz","email":"test@example.com","phone":"555-123-4567","monthly_revenue":"$10K - $25K","time_in_business":"1-2 years"}
json.dump(d, open('/tmp/test-lead.json','w'))
