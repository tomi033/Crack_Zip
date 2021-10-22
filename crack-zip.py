import zipfile
from tqdm import tqdm

zip = raw_input("Masukan nama Zip :")
wordlist = raw_input("Masukan nama password :")

zip_file = zipfile.ZipFile(zip)
n_words = len(list(open(wordlist, "rb")))
print("Total password yang di coba:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password ditemukan:", word.decode().strip())
            exit(0)
print("[!] Password tidak di temukan, Silahkan cari wordlist lainnya.")
