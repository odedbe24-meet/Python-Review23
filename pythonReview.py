def create_youtube_video(title, description):
	video = {"Title": title, "Description" : description, "Likes": 0, "Dislikes": 0, "Comments": {}}
	return video


def like(video):
	video["Likes"] += 1
	return video

def dislike(video):
	video["Dislikes"] += 1

def add_comment(video, username, comment_text):
	video["Comments"][username] = comment_text
	return video

youtube_video = create_youtube_video(input("title: "), input("Description: "))
print(youtube_video)

print("Like?")
if(input() == 'y'):
	like(youtube_video)

print("Dislike?")
if(input() == 'y'):
	dislike(youtube_video)

print(youtube_video)

print("Would You Like To Add A Comment?")
if(input() == 'y'):
	add_comment(youtube_video, input("What Is Your username?: "), input("what is the body of the comment"))
print(youtube_video)