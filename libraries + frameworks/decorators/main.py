
def is_authenticated(func):
    def wrapper(*args):
        print(*args)
    
    return wrapper



class Mutation:
    @is_authenticated
    def get_posts(self):
        print('gettings posts....')

mutation = Mutation()
get_posts = mutation.get_posts(False)