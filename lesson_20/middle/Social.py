# Соціальна мережа: Створіть класи для користувачів та дописів у соціальній мережі
# з можливістю додавання друзів, коментування та лайків.
class User:
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.posts = []

    def __str__(self):
        return f'ℹ️ Користувач "{self.username}":\n' \
               f'    Друзi: {", ".join([friend.username for friend in self.friends])}\n' \
               f'    Дописи: {", ".join([post.text for post in self.posts])}\n' \
               f'    Кiлькiсть лайкiв: {self.likes}'

    @property
    def likes(self):
        return sum(post.likes for post in self.posts)

    def add_friend(self, user):
        if user not in self.friends:
            self.friends.append(user)
            user.friends.append(self)

            print(f'✅ {self.username}: Користувача "{user.username}" додано до друзiв!')
        else:
            print(f'❌ {self.username}: Користувач "{user.username}" вже є у друзях!')

    def remove_friend(self, user):
        self.friends.remove(user)
        user.friends.remove(self)

        print(f'✅ {self.username}: Користувача "{user.username}" видалено з друзiв!')

    def create_post(self, text):
        post = Post(self.username, text)
        self.posts.append(post)

        print(f'✅ {self.username}: Допис додано!')
        return post

    def remove_post(self, post):
        if post in self.posts:
            self.posts.remove(post)
            print(f'✅ {self.username}: Допис видалено!')
        else:
            print(f'❌ {self.username}: Допис не знайдено!')


class Post:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.comments = []
        self.likes = 0

    def __str__(self):
        return f'ℹ️ Допис користувача "{self.author}":\n' \
               f'   "{self.text}"\n' \
               f'   Коментарi: {", ".join([comment.text for comment in self.comments])}\n' \
               f'   Кiлькiсть лайкiв: {self.likes}'

    def comment(self, author, text):
        comment = Comment(author, text)
        self.comments.append(comment)

        print(f'✅ {author.username}: Коментар "{comment.text}" до допису користувача "{self.author}" додано!')

    def like(self):
        self.likes += 1
        print(f'✅ Лайк до допису користувача "{self.author}" додано!')


class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = f'"{text}"'


ilya = User('Ilya Kramarenko')
sasha = User('Oleksandra Pyskun')

ilya.add_friend(sasha)
sasha.add_friend(ilya)

print('----' * 3)

first_post_ilya = ilya.create_post('Це мiй перший допис у цiй мережi! Всiм привiт!')
first_post_sasha = sasha.create_post('Ого! Що це таке?')
sasha.remove_post(first_post_sasha)

print(first_post_ilya)

print('----' * 3)

first_post_ilya.comment(sasha, 'Вiтаю в мережi!')
first_post_ilya.like()

print('----' * 3)

print(first_post_ilya)

print('----' * 3)

print(sasha)
print(ilya)
