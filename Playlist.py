# Playlist.py
import webbrowser
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
#option 1 : create playlist
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
# option 2: Show playlist
	print("\n************************\n")
	print("\n     PLAYLIST INFOMATION     \n")
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
	print("| 1. Create playlist   |")
	print("| 2. Show playlist    |")
	print("| 3. Play a video     |")
	print("| 4. Add a video      |")
	print("| 5. Update playlist  |")
	print("| 6. Delete a video   |")
	print("| 7. Save and Exit    |")
	print(" --------------------- ")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)
		# choice = int(choice)
	return choice

def play_video(playlist):
#option 3: Play a video
	print_videos(playlist.videos)
	select = select_in_range("Enter number of video you want to play: ", 1, len(playlist.videos))
	video = playlist.videos[int(select) - 1]
	print("play video: " + video.title + "with link: " + video.link)
	webbrowser.open(video.link, new=2)

def add_video(playlist): 
#option 4: Add a video 
	print("Enter new video: ")
	video = read_video()
	playlist.videos.append(video)
	print("Add video successfully!!")
	return playlist

def update_playlist(playlist):
#option 5: update playlist
	print("1. name: ", playlist.name)
	print("2. description: ", playlist.description)
	print("3. rating: ", playlist.rating)
	print_videos(playlist.videos)
	choice_update = select_in_range("What you want to change:", 1, 3)
	choice_update = int(choice_update)

	if choice_update == 1:
		name = input("Enter new playlist's name: ") + "\n"
		playlist.name = name
		print("successfully to rename!!!")
		return playlist
		
	elif choice_update == 2:
			description = input("Enter new playlist's description: ") + "\n"
			playlist.description = description
			print("successfully to redescription!!!")
			return playlist
		
	elif choice_update == 3:
			rating = input("Enter new playlist's rating: ") + "\n"
			playlist.rating = rating
			print("successfully to rerating!!!")
			return playlist
	
	print("Update successfully!!")

def delete_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	new_videos = []
	choice = select_in_range("select video you want to delete: ",1,total)
	choice = int(choice)
	for i in range(total):
		if i == choice - 1:
			continue
		new_videos.append(playlist.videos[i])
	playlist.videos = new_videos
	print("delete video successfully!!")
	return playlist 

def main():
	try:
		playlist = read_playlist_from_txt()
		print("data loaded successfully!!")	
	except:
		print("welcome first user, please Create playlist first")

	while True:
		main_menu()
		choice = select_in_range("Enter an option: ", 1, 7)
		choice = int(choice)
		if choice == 1:
			playlist = read_playlist()
			input("\nPress Enter to continue!!\n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress Enter to continue!!\n")
		elif choice == 3:
			play_video(playlist)
			input("\nPress Enter to continue!!\n")
		elif choice == 4:
			add_video(playlist)
			input("\nPress Enter to continue!!\n")
		elif choice == 5:
			update_playlist(playlist)
			input("\nPress Enter to continue!!\n")
		elif choice == 6:
			delete_video(playlist)
			input("\nPress Enter to continue!!\n")
		elif choice == 7:
			write_playlist_to_txt(playlist)
			break

	# playlist = read_playlist_from_txt()
	# print_playlist(playlist)



main()
		
		