def create_youtube_video(title, description, flag):
	video = {"Title": title, "Description" : description, "Likes": 0, "Dislikes": 0, "Comments": {}, "Hashtag":[]}
	if(flag == True):
		print("Like?")
		if(input() == 'y'):
			like(video)

		print("Dislike?")
		if(input() == 'y'):
			dislike(video)

		print("Would You Like To Add A Comment?")
		if(input() == 'y'):
			add_comment(video, input("What Is Your username?: "), input("what is the body of the comment"))
		# print(youtube_video)

		add_hashtag(video)
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
	

def similarity_to_video(video1, video2):
	if(len(video1["Hashtag"]) < len(video2["Hashtag"]) ):

				# len[video2] = 100%
		final = 0
		n = 100 / len(video2["Hashtag"])

		for i in range(min(len(video1["Hashtag"]), len(video2["Hashtag"]))):
		    if video1["Hashtag"][i] in video2["Hashtag"]:
		        final += n

		return final
		print("BuiltIn Is Bigger")

	elif(len(video1["Hashtag"]) > len(video2["Hashtag"]) ):

		final = 0
		n = 100 / len(video1["Hashtag"])

		for i in range(min(len(video2["Hashtag"]), len(video1["Hashtag"]))):
		    if video2["Hashtag"][i] in video1["Hashtag"]:
		        final += n

		return final
		print("New Is Bigger")

	elif(len(video1["Hashtag"]) == len(video2["Hashtag"]) ):


		final = 0
		n = 100 / len(video2["Hashtag"])

		for i in range(min(len(video1["Hashtag"]), len(video2["Hashtag"]))):
		    if video1["Hashtag"][i] in video2["Hashtag"]:
		        final += n
		return final
		print("they Are The Same")



youtube_video = create_youtube_video(input("title: "), input("Description: "), True)


# print(youtube_video)


my_video = create_youtube_video("my video ", "this is my description", False);

my_video["Hashtag"] = ["Hashtag", "At", "Eat", "Meet"]

simiilarty = similarity_to_video(youtube_video,my_video)

print("The Title is: " + youtube_video["Title"])
print("The Description is: " + youtube_video["Description"])
print("The Amount Of Likes is: " + str(youtube_video["Likes"]))
print("The Amount Of Dislikes is: " + str(youtube_video["Dislikes"]))
print("The Comments Are " , youtube_video["Comments"] )
print("The Hashtags Are: " , youtube_video["Hashtag"])
print(" It is " + str(simiilarty) + "'%' simmilar to another video")
