# 1) Є файл emails.txt
# ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)

#_my_code:
try:
    with open('emails.txt', 'r') as f:
        #reading all the emails from the file
        emails = f.readlines()
        #creating a list for mails with domain gmail.com
        gmail_emails = []
        for line in emails:
            #spliting the string into two parts:
            parts = line.split()
            #variable for only email-part
            email = parts[1]
            #checking if there is a gmail domain
            if email.endswith('gmail.com'):
                #then we add it to the list
                gmail_emails.append(email)

        # writing filtered addresses to the file
        with open('gmail_emails.txt', 'w') as file:
            for mail in gmail_emails:
                file.write(f"{mail}\n")


except Exception as e:
    print(e)

#_code_from_consultation

# try:
#     # with open('emails.txt') as source, :
#     #     with open('gmail.txt', 'w') as target:
#     with open('emails.txt') as source, open('gmail.txt', 'w') as target:
#         for line in source:
#             email = line.split()[-1]
#             if email.endswith('@gmail.com'):
#                 print(email, file=target)
# except Exception as e:
#     print(e)
