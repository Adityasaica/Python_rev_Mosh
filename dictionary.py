dist={
    "name":"V.chowdary Adithya Sai",
    "age":22,
    "is_good":False,

}

print(dist["name"])
print(dist["age"])
print(dist["is_good"])
#below does not give the error
print(dist.get("name"))
print(dist.get("hbd"))
print(dist.get("birth","jan 1 1980"))
print(dist.get("birth"))
print(dist)
dist["name"]="Adithya sai"
print(dist)

#adding new key values

dist["birthday"]="31 dec 2003"
print(dist)
