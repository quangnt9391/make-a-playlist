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
	print("--------------")
	print("video title:" ,video.title, end="")
	print("video link: ", video.link, end="")

def write_video_to_txt(video):
	with open("data.txt", "w") as file:
		file.write(video.title)
		file.write(video.link)

def read_video_from_txt():
	with open("data.txt", "r") as file:
		title = file.readline()
		link = file.readline()
		video = Video(title, link)
	return video


def main():
	video = read_video()
	write_video_to_txt(video)
	video = read_video_from_txt()
	print_video(video)



main()
		
		