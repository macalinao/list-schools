result = sorted(set([email.split('@')[-1] for email in open('emails.txt').read().split('\n') if email.endswith('.edu')]))
print("Found " + str(len(result)) + " schools.")
print('\n'.join(['  ' + r for r in result]))
