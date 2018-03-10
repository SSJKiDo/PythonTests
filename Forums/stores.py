class MemberStore:
    members = []
    def get_all(self):
        return self.members
    
    def add(self, member):
        self.members.append(member)

    def get_by_id(self, id):
        pass
    
    def update(self, member):
        pass
    
    def delete(self, id):
        pass

    def entity_exists(self, member):
        if member in self.members:
          return True
        return False

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
        if post in self.posts:
            return True
        return False

