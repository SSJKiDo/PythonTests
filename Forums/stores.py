class MemberStore:
    members = []
    last_id = 1
    
    def get_all(self):
        return self.members
    
    def add(self, member):
        self.members.append(member)
        member.id = MemberStore.last_id
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        for member_instance in all_members:
            if member_instance.id == id:
                return member_instance
    
    def update(self, member):
        result = member
        all_members = self.get_all()

        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member

        return result
    
    def delete(self, id):
        to_delete = self.get_by_id(id)
        self.members.remove(to_delete)
        result = str(to_delete) + " has been deleted."
        return result

    def entity_exists(self, member):
        if self.get_by_id(member.id) is not None:
            return True
        return False
    
    def get_by_name(self, member_name):
        exist_member = []
        all_members = self.get_all()
        for the_member in all_members:
            the_member_id = self.get_by_id(the_member.id)
            if the_member_id == member_name:
                exist_member.append(the_member_id)
        return exist_member
                
        for the_member in self.get_by_id(member_name.id):
            if the_member:
                exist_member.append(the_member)
        return exist_member

class PostStore:
    posts = []
    
    def get_all(self):
        return self.posts
    
    def add(self, post):
        self.posts.append(post)

    def get_by_id(self, id):
        pass

    def update(self, post):
        pass
    
    def delete(self, id):
        pass

    def entity_exists(self, post):
        result = False
        if post in self.posts:
            result = True
        return result

