# Library to have connection to your gmail
import smtplib
# library to extract the entities form your resume
from pyresparser import ResumeParser
import nltk
nltk.download('stopwords')
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com',587)

# start TLS for security
s.starttls() 
s.login("indrac2891@gmail.com", "nvkclxnptfsmtjoa")
# Authentication 


# give a subject   
SUBJECT = "Interview Call"

# skills requirement for Ai developer
python_skills = ["ml","ai","matplotlib","seabon",
                 "python","reression","algorithms", 
                 "Pandas","data analysis","keras",
                 "tensorflow","artificial intelligence",
                 "data visualization","opencv"]
# skills requirement for Java developer
java_skills  = []

# extract the skills from resume
data = ResumeParser('PradeepthiResume.pdf').get_extracted_data()
print(data)
# grab the name
name = data['name']
# grab the Email
email = data['email']
# grab the Skills
skills = data["skills"]
# lowercase the skills
actual_skills = [i.lower() for i in skills ]

  
# using list comprehension 
# checking if string contains list element 
Skills_matched = [ele for ele in actual_skills 
                if(ele in python_skills)] 



# check the number of skills matched
if(len(Skills_matched) >= 4 ):
    
    print("he is eligible")
    # create a text that is to sent in an email
    TEXT = "Hello "+name + ",\n\n"+ """Thanks for applying to the
    job post AI/ML Developer , Your skils matches our requirement.
    Kindly let us know the available time for initial round of interview. 
    \n\n\n\n Thanks and Regards, \n\n Talent acquistition Team, \n\n Smartbridge""" 
    # send mail
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #send the mail
    s.sendmail("indrac2891@gmail.com", "nvkclxnptfsmtjoa", email, message) 
    #quit the session
    s.quit()    
else:
    print("sorry we cant process your candidature")
    
    TEXT = "Hello "+name + ",\n\n"+ """Thanks for applying to the job post AI/ML 
    Developer , Your candidature is rejected. 
    \n\n\n\n Thanks and Regards, \n\n Talent acquistition Team, \n\n Smartbridge"""  
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("indrac2891@gmail.com", email, message) 
    s.quit() 
    