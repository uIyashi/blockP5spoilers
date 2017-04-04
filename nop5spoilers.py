import tweepy

print("Anti P5-spoilers bot asshole v1")
print("-------------------------------")
print("Un lien va apparaitre dans pas longtemps.")
print("Allez dessus, connectez vous avec votre compte twitter")
print("et écrivez le code que twitter vous donne. Je bloque le")
print("fdp pour vous <3")
auth=tweepy.OAuthHandler("w1eFQDLLUgz1w6MXideNBUUuv","BkPviFYTxmy2GJnZCa2oHaiAW66wg2RxBcLjr5SjE3vU0XBw0s")

print("\n Connectez vous ici et écrivez le PIN:")
url = auth.get_authorization_url()
print(url)
pin = input("PIN: ")
auth.get_access_token(pin)
api = tweepy.API(auth)
api.verify_credentials()

print("Connecté!")
api.create_block(847264071514701824)
print("Bloqué! Si y'a d'autres comptes a spoilers,")
print("envoyez moi un dm avec le @ du compte.")
print("vous inquiétez pas pour moi j'ai pas de ps4 lmao")
