import sys, hashlib, time

ts = time.time()

if len(sys.argv) != 3:
    print("USAGE: ")
    print("./" + sys.argv[0] + " hashes.txt rockyou.txt \n")
    sys.exit()

hashes = []
with open(sys.argv[1], "r") as hashfile:
    for line in hashfile:
        hashes.append(line.strip())

print("Start cracking...")
with open(sys.argv[2], "r") as wordlist:
    for line in wordlist:
        line = line.strip('\n')
        md5_hash = hashlib.md5(line.encode()).hexdigest()
        if md5_hash in hashes:
            print(md5_hash + " == " + line)

td = time.time() - ts
print("Done in" + str(td) + "sec.")