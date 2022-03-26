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

def read_videos():
	videos = []
	total = input("how many videos: ")
	total = int(total)
	for i in range(total):
		print("Enter video:", i+1)
		video = read_video()
		videos.append(video)
	return videos

def print_video(video):
	print("--------------")
	print("video title:" ,video.title, end="")
	print("video link: ", video.link, end="")

def print_videos(videos):
	print("\n************************\n")
	total = len(videos)
	print("Total video: ", str(total) + "\n")
	for i in range(total):
		print("video ", i+1)
		print_video(videos[i])


def write_video_to_txt(video, file):
	# with open("data.txt", "w") as file:
	file.write(video.title)
	file.write(video.link)

def read_video_from_txt(file):
	# with open("data.txt", "r") as file:
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def write_videos_to_txt(videos):
	total = len(videos)
	with open("data.txt", "w") as file:
		file.write(str(total) + "\n")
		for i in range(total):
			write_video_to_txt(videos[i], file)
	print("file write successfully!")

def read_videos_from_txt():
	with open("data.txt", "r") as file:
		videos = []
		total = file.readline()
		total = int(total)
		for i in range(total):
			video = read_video_from_txt(file)
			videos.append(video)
	return videos



def main():
	videos = read_videos()
	write_videos_to_txt(videos)
	videos = read_videos_from_txt()
	print_videos(videos)



main()
		
		