import models
import stores

member1 = models.Member("KiDo", 25)
member2 = models.Member("Avril", 34)
post1 = models.Post("Title1", "Content1")
post2 = models.Post("Title2", "Content2")
post3 = models.Post("Title3", "Content3")

member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)
theMembers = member_store.get_all()
for i in theMembers:
    print i
