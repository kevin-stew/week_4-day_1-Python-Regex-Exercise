import re

my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com","yourfavoriteband@g6.org", "@codingtemple.com"]

# You can also use the $ at the end of your compile expression -- this stops the search
#.com OR .org => com|org

#Expected output: None pocohontas1776@gmail.com None yourfavoriteband@g6.org None

pattern_email = re.compile("([a-z0-9+])@([a-z0-9]+).(com|org)$")

# found_address = pattern_email.findall(my_emails)

def exercise(my_emails):
    for email in my_emails:
        match = pattern_email.match(email)
        
        if match:
            print(email)
            # print(email[match.span()[0]:match.span()[1]])
        else:
            print("None")

exercise(my_emails)
            
#match = found_address.search('.com')

#match.groups()  #only returns groups (or something)