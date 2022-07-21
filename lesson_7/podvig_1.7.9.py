


class Video:
    def create(self, name):
        self.name = name


    def play(self):
        print(f'воспроизведение видео {self.name}')

class YouTube:

    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()



d = Video()
d.create('Ivan')
d.play()

YouTube.add_video('Python')
YouTube.add_video('Java')
print(YouTube.video_lst)