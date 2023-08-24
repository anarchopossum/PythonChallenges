import pandas as pd
'''
Generate a Regex
first char can be letters followed by alphanumeric with some valid symbols
lastly it MUST end in leetcode.com
'''
regex = '^[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com$'

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Check user mail column using the regex we made. this will return T/F
    valid_email= users['mail'].str.contains(regex)
    # apply filter showing only true values
    output = users[valid_email]
    return output[['user_id','name','mail']].sort_values(by="user_id")

data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

print("Users:\n", Users)
print("Valid Emails:\n", valid_emails(Users))
