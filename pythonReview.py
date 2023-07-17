def create_youtube_video(title, description):
	video = {"Title": title, "Description" : description, "Likes": 0, "Dislikes": 0, "Comments": {}, "Hashtag":[]}
	print("Like?")
	if(input() == 'y'):
		like(youtube_video)

	print("Dislike?")
	if(input() == 'y'):
		dislike(youtube_video)

	print("Would You Like To Add A Comment?")
	if(input() == 'y'):
		add_comment(youtube_video, input("What Is Your username?: "), input("what is the body of the comment"))
	# print(youtube_video)

	add_hashtag(youtube_video)
	print("test test")

	return video


def like(video):
	video["Likes"] += 1
	return video

def dislike(video):
	video["Dislikes"] += 1

def add_comment(video, username, comment_text):
	video["Comments"][username] = comment_text
	return video

def add_hashtag(video):
	while len(video["Hashtag"]) <=4:
		hashtag = input("Would Like To Add A Hashtag? if yes just type it, else type n: ")
		if(hashtag == "n"):
			break
		else:
			video["Hashtag"].append(hashtag)
	

# def similarity_to_video(video1, video2):
# 	if(len(video1["Hashtag"]) < len(video2["hashtag"]) )
# 		print("true")



youtube_video = create_youtube_video(input("title: "), input("Description: "))


# print(youtube_video)

print("The Title is: " + youtube_video["Title"])
print("The Description is: " + youtube_video["Description"])
print("The Amount Of Likes is: " + str(youtube_video["Likes"]))
print("The Amount Of Dislikes is: " + str(youtube_video["Dislikes"]))
print("The Comments Are " , youtube_video["Comments"] )
print("The Hashtags Are: " , youtube_video["Hashtag"])