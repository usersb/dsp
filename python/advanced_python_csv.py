def write_to_file(faculty):
    email_list = print_emails(faculty)
    with open('emails.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        
        for email in email_list:
            writer.writerow([email])
        print("Done")
        
write_to_file(faculty)
