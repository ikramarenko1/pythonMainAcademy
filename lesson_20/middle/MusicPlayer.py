# Музичний плеєр: Створіть клас для музичного плеєра з можливістю
# відтворення музики, створення списків відтворення та керування гучністю.
import time


class MusicPlayer:
    def __init__(self, name):
        self.name = name
        self.active = False
        self.playlist = None
        self.volume = 1

    def __str__(self):
        return f'ℹ️ Музичний плеєр "{self.name}":\n' \
               f'    {"✅ Активний." if self.play == True else "❌ Не активний."}\n' \
               f'    Список відтворення: {self.playlist}\n' \
               f'    Гучнiсть (0-1): {self.volume}'

    def add_playlist(self, playlist):
        if isinstance(playlist, Playlist):
            if self.playlist is None:
                self.playlist = playlist
                print(f'✅ Плейлiст {playlist.name} додано до музичного плеєра "{self.name}".')

            else:
                while True:
                    choice = input(f'Музичний плеєр "{self.name}" вже має плейлiст {self.playlist.name}. '
                                   f'Замiнити його? (y/n) ')

                    if choice == 'y':
                        self.playlist = playlist
                        print(f'✅ Плейлiст "{playlist.name}" додано до музичного плеєра "{self.name}".')
                        break

                    elif choice == 'n':
                        print(f'❌ Залишено плейлiст {self.playlist.name}')
                        break

                    else:
                        print('Вибiр не вiрний. Повторiть введення.')

        else:
            print(f'❌ Неможливо виконати дiю. "{playlist}" не є плейлiстом.')

    def play(self):
        if self.playlist is not None:
            if self.playlist.songs:
                self.active = True

                print(f'ℹ️ Вiдтворюю пiсню "{self.playlist.songs[0].name}" - {self.playlist.songs[0].author}..')
                print(self.playlist.songs[0])

                time.sleep(self.playlist.songs[0].time)

                self.playlist.songs.pop(0)

                print('✅ Вiдтворення завершено. Список вiдтворення оновлено!')
            else:
                print(f'❌ Музичний плеєр "{self.name}" має плейлiст "{self.playlist.name}", але плейлiст не має пicень!')
        else:
            print(f'❌ Музичний плеєр "{self.name}" не має плейлiста.')

    def set_volume(self, volume):
        if 0 <= volume <= 1:
            self.volume = volume
            print('✅ Гучнiсть змiнено.')
        else:
            print(f'❌ Рівень гучності має бути від 0 до 1!')


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __str__(self):
        return f'ℹ️ Плейлiст "{self.name}":\n' \
               f'    Пiснi: ' + ', '.join([f'{song.name} - {song.author}' for song in self.songs])

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
            print(f'✅ Пiсню "{song.name}" - {song.author} додано до плейлiста "{self.name}".')
        else:
            print(f'❌ Неможливо додати {song} до плейлiста "{self.name}".')

    def remove_song(self, song):
        if isinstance(song, Song):
            self.songs.remove(song)
            print(f'✅ Пiсню "{song.name}" - {song.author} видалено з плейлiста "{self.name}".')
        else:
            print(f'❌ Неможливо виконати дiю. "{song}" не є пiснею.')


class Song:
    def __init__(self, name, author, time):
        self.name = name
        self.author = author
        self.time = time

    def __str__(self):
        return f'ℹ️ Пiсня "{self.name}":\n' \
               f'    Автор: {self.author}\n' \
               f'    Тривалiсть: {self.time} хв.'


homepod = MusicPlayer('Apple HomePod')

window_shopper = Song('Window Shopper', '50 cent', 3)
do_for_love = Song('Do For Love', '2Pac', 4)
heavy_metal = Song('Heavy Metal (feat. blagoiblago)', 'kizaru', 3)

my_playlist = Playlist('My Playlist')

print(homepod)
print('----' * 3)

homepod.play()
homepod.add_playlist(my_playlist)
homepod.play()
print('----' * 3)

my_playlist.add_song(window_shopper)
my_playlist.add_song(do_for_love)
my_playlist.add_song(heavy_metal)
print(my_playlist)
print('----' * 3)

homepod.set_volume(0.9)
print('----' * 3)

homepod.play()
homepod.play()
homepod.play()
print('----' * 3)

homepod.play()
