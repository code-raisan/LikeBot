# -*- coding: utf-8 -*-
import tweepy 
import time as t

CK = ""
CS = "jPrJCW1WjniNy5NhHKUAT9bKZBtmbGeSQMfQK4YwCtGfI65GR7"
AT = "1175900055485599744-H2znV7RF7lKKTLtTv35i3ef6sYxaV3"
AS = ""
n = 20


c = 0
f = 0
of = 0
le = 0

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)
api = tweepy.API(auth)

api.update_status(str(f"{n}件のふぁぼを開始します"))
print(str(f"{n}件のふぁぼを開始します"))
print("\n--------------------------")

for status in api.home_timeline(count = n):
    t.sleep(0.5)
    c = c + 1
    if not "RT @" in status.text[0:4]:
        if not f"@" in status.text[0:1]:
            print(f"\n\n\n({status.user.name})")
            print(status.text) 
            try:
                api.create_favorite(status.id)
                print(f"\n--------[ふぁぼを付けました]({c})") 
                f = f + 1
            except:
                print(f"\n------------[既にふぁぼ済み]({c})")
                of = of + 1
        else:
            print(f"\n\n\n({status.user.name})")
            print(status.text) 
            print(f"\n------------[リプのため除外]({c})")
            le = le + 1            
    else:
        print(f"\n\n\n({status.user.name})")
        print(status.text) 
        print(f"\n--------------[RTのため除外]({c})")
        le = le + 1 

print(f"\n\nふぁぼ完了 : {f} / 既にふぁぼ済み : {of} / 除外 : {le} / 合計 : {c}\n\n\n\n\n\n")
api.update_status(str(f"\n\nふぁぼ完了 : {f} / 既にふぁぼ済み : {of} / 除外 : {le} / 合計 : {c}\n\n\n\n\n\n"))
