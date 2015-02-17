import random,hashlib,itertools,time

def load_wordlist(d_location=r'D:\dictionary_words.txt',number_of_words=2048):
    #This returns a list of 2048 words from a supplied file.
    #Note, the words must contain ONLY letters or it will skip it and try to find another one.
    #If your dictionary does not have at least 2048 words, it will get stuck in a loop
    with open(d_location) as d_file:
        dict = d_file.read()
    dict = dict.split('\n')
    wordlist = []
    while number_of_words:
        word = dict[random.randint(0,len(dict))]
        if word.isalpha() and word not in wordlist:
            wordlist.append(word)
            number_of_words -= 1
    return wordlist

def hash_wordlist(words,length,average=False):
    #If average is False, this will hash every single combination and return the total time
    #If average is True, will perform 100,000,000 hashes and return the average time for 10,000,000 hashes.
    #Does SHA-256 hash of your wordlist. Words and length of password is adjustable.
    #Its probably possible to use this to test a brute-force approach if your "wordlist" is actually a list of characters, however length will be fixed.
    progress = 0
    hash_times,averages = [time.time()],[]
    print('hashing')
    for password in itertools.product(words,repeat=length):
        password = ''.join(password)
        hash = hashlib.sha256(password).hexdigest()
        progress += 1
        if not progress%10000000:
            hash_times.append(time.time())
            averages.append(hash_times[-1]-hash_times[-2])
            print('%s\nHash: %s\nTime: %s\n' % (password,hash,hash_times[-1]-hash_times[0]))
            if average and len(averages) == 10: return sum(averages)/10
            if not average:#This is just so averages/hash_times do not become large blocks of memory if you dont plan on averaging.
                averages = []
                hash_times = hash_times[0]
    return hash_times[-1]-hash_times[0]

def crack():
    wordlist = load_wordlist()
    timing = hash_wordlist(wordlist,4,True)
    print(timing)

crack()
