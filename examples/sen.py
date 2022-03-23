import sen_py

print("SENPY_CLUB_API_BASE_URL:", sen_py.SENPY_CLUB_API_BASE_URL)
print("SENPY_CLUB_API_CURRENT_VERSION:", sen_py.SENPY_CLUB_API_CURRENT_VERSION)
print("SENPY_CLUB_API_URL:", sen_py.SENPY_CLUB_API_URL)

random: sen_py.Random = sen_py.Random()
print("Random.image:", random.language)
print("Random.image:", random.image)

print("languages:", sen_py.languages())
print("language(\"C\"):", sen_py.language("C"))
