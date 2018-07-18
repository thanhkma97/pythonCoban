import requests
#token giong nhu mot cai khoa de minh truy cap vao du lieu
token = "EAAAAUaZA8jlABAGdVVNoVrWetvVDXVT2ltDPZBvYDKkPBcYZB8UTYZCL7kgdAXqJQ920VsPXBqnZAwZAQnAsBurZA1MnwU1YompigShEUW0gSleyfAcIkXR3ZBg10bSIRwTcMvipv7xeznVfkKO1M0ZCFIG46qkDob8JcA7rpjXy3yyf7iZBWELGpl"
id_face = "1976628369040649"

access = {"access_token": token}
a =  requests.post('https://graph.facebook.com/'+id_face+'/reactions?type=LOVE', data = access)
#data:cai truyen vao noi dung
print(a)
