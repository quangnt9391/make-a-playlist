# Playlist.py
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

def read_video():
	title = input("Enter video title: ") + "\n"
	link = input("Enter video link: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video):
	print("video title:" ,video.title)
	print("video link: ", video.link)

def write_video_to_txt(video):
	with open("data.txt", "w") as file:
		file.write(video.title)
		file.write(video.link)

def main():
	video = read_video()
	print_video(video)
	write_video_to_txt(video)


main()
		
		