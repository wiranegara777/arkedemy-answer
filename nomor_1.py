import json

def biodata():
    bio = []
    name = "Muhammad Wiranegara Girinata"
    age = 22
    address = "Jalan raya puncak Rt 01/08 Desa Bendungan Ciawi Bogor"
    hobbies = ["nonton anime","nonton drakor","maen gbf","baca light novel","ngoding"]
    is_married = False
    list_school = [{"name": "MAN 2 BOGOR", "year_in":2013, "year_out":2015,"major":"Science"},
                    {"name": "Insntitut Pertanian bogor", "year_in":2015, "year_out":2019,"major":"Computer Science"}]
    skills = [{"skill_name": "Python", "level":"intermediate"},
            {"skill_name": "PHP", "level":"intermediate"},
            {"skill_name": "Laravel", "level":"intermediate"},
            {"skill_name": "HTML", "level":"beginner"},
            {"skill_name": "CSS", "level":"beginner"},
            {"skill_name": "Ruby", "level":"beginner"},
            {"skill_name": "Ruby on Rails", "level":"beginner"},
            {"skill_name": "REST API", "level":"intermediate"}]
    interest_in_coding = True

    bio.append(name)
    bio.append(age)
    bio.append(address)
    bio.append(hobbies)
    bio.append(is_married)
    bio.append(list_school)
    bio.append(skills)
    bio.append(interest_in_coding)

    mydata = json.dumps(bio)

    print(mydata)


biodata()