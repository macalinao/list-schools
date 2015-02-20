print(sorted(set([email.split('@')[-1] for email in open('emails.txt').read().split('\n') if email.endswith('.edu')])))
