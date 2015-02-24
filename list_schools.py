domains = [email.split('@')[-1] for email in open('emails.txt').read().split('\n') if email.endswith('.edu')]
counts = [(domains.count(d), d) for d in set(domains)]
counts.sort(reverse=True)
print("Found " + str(len(counts)) + " schools.")
print('\n'.join(['  ' + str(c[0]) + ' ' + str(c[1]) for c in counts]))
print('Total: ' + str(sum([c[0] for c in counts])))
