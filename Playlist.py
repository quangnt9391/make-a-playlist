# Playlist.py
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

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
	
def read_playlist():
	name = input("Enter Playlist name: ") + "\n"
	description = input("Enter playlist description: ") + "\n"
	rating = input("Enter playlist rating: ") + "\n"
	videos = read_videos()
	playlist = Playlist(name, description, rating, videos)
	return playlist

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

def print_playlist(playlist):
	print("Playlist's name: ", playlist.name, end="")
	print("Playlist's description: ", playlist.description, end="")
	print("Playlist's rating: ", playlist.rating, end="")
	print_videos(playlist.videos)

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

def write_videos_to_txt(videos, file):
	total = len(videos)
	# with open("data.txt", "w") as file:
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_to_txt(videos[i], file)

def read_videos_from_txt(file):
	# with open("data.txt", "r") as file:
	videos = []
	total = file.readline()
	total = int(total)
	for i in range(total):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def write_playlist_to_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_to_txt(playlist.videos, file)
	print("write playlist successfully!!")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		name = file.readline()
		description = file.readline()
		rating = file.readline()
		videos = read_videos_from_txt(file)
	playlist = Playlist(name, description, rating, videos)
	return playlist
def main_menu():
	print(" --------------------- ")
	print("| 1. Creat playlist   |")
	print("| 2. Show playlist    |")
	print("| 3. Play a video     |")
	print("| 4. Add a video      |")
	print("| 5. Update playlist  |")
	print("| 6. Delete a video   |")
	print("| 7. Save and Exit    |")
	print(" --------------------- ")

def main():
	main_menu()
	playlist = read_playlist()
	write_playlist_to_txt(playlist)
	playlist = read_playlist_from_txt()
	print_playlist(playlist)



main()
		
		