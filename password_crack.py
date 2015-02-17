import random,hashlib,itertools,time

def load_wordlist(d_location=r'D:\dictionary_words.txt',number_of_words=2048):
    #This returns a list of 2048 words from a supplied file.
    #Note, the words must contain ONLY letters or it will skip it and try to find another one.
    #If your dictionary does not have at least 2048
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
    progress = 0
    hash_times,averages = [time.time()],[]
    print('hashing')
    for password in itertools.product(words,repeat=length):
        password = ''.join(password)
        hash = hashlib.sha256(password).hexdigest()
        progress += 1
        if not progress%10000000:
            hash_times.append(time.time())
            averages.append(hash_times[-1]-hash_times[0])
            print('%s\nHash: %s\nTime: %s\n' % (password,hash,averages[-1]))
            if average and len(averages) == 10: return sum(averages)/10
            if not average: averages = []

def crack():
    wordlist = load_wordlist()
    timing = hash_wordlist(wordlist,4,True)
    print(timing)

crack()