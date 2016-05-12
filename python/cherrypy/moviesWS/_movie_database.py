class _movie_database:
	## constructor ##
	def __init__(self):
		self.movies = {}
		self.users = {}
		self.ratings = {}
		self.posters = {}

		self.largestMid = 0
		self.largestUid = 0

	## load_movies ##
	def load_movies(self, mFile):
		# clear the dictionary
		self.movies.clear()	

		f = open(mFile)
	
		for line in f:
			line = line.rstrip()	# removes trailing whitespace
			components = line.split("::")
			mId = int(components[0])
			
			oneMovie = {}
			oneMovie['name'] = components[1]
			oneMovie['genres'] = components[2]
			self.movies[mId] = oneMovie

			if mId > self.largestMid:
				self.largestMid = mId
	
		f.close()

	## load_movie ##
	def load_movie(self, mFile, mId):
		f = open(mFile)

		for line in f:
			line = line.rstrip()
			components = line.split("::")
			fmId = int(components[0])
			if fmId == mId:
				# reload the movie
				oneMovie = {}
				oneMovie['name'] = components[1]
				oneMovie['genres'] = components[2]
				self.movies[mId] = oneMovie
				break
		f.close()

	## get_movie ##
	def get_movie(self, mId):
		if self.movies.has_key(mId):
			return [self.movies[mId]['name'], self.movies[mId]['genres']]
		else: 
			return None

	## get_movies ##
	def get_movies(self):
		return self.movies.keys()

	## set_movie ##
	def set_movie(self, mId, l):
		self.movies[mId]['name'] = l[0]
		self.movies[mId]['genres'] = l[1]

	## add_movie ##
	def add_movie(self, l, mId = 0):
		oneMovie = {}
		(oneMovie['name'], oneMovie['genres']) = l
				
		if mId == 0: 
			self.largestMid += 1
			self.movies[self.largestMid] = oneMovie
			return self.largestMid
		else:
			if mId > self.largestMid:
				self.largestMid = mId
			self.movies[mId] = oneMovie
			return mId

	## delete_movie ##
	def delete_movie(self, mId):
		del self.movies[mId]		

	## delete_movies ##
	def delete_movies(self):
		self.movies.clear()
		self.largestMid = 0


	## load_users ##
	def load_users(self, uFile):
		self.users.clear()
		self.largestUid = 0

		f = open(uFile)

		for line in f:
			line = line.rstrip()
			components = line.split("::")
			uId = int(components[0])

			oneUser = {}
			oneUser['gender'] = components[1]
			oneUser['age'] = int(components[2])
			oneUser['occupation'] = int(components[3])
			oneUser['zip'] = components[4]

			self.users[uId] = oneUser

			if uId > self.largestUid:
				self.largestUid = uId

		f.close()

	## get_user ##
	def get_user(self, uId):
		if self.users.has_key(uId):
			return [self.users[uId]['gender'], self.users[uId]['age'], self.users[uId]['occupation'], self.users[uId]['zip']]
		else:
			return None

	## get_users ##
	def get_users(self):
		return self.users.keys()

	## set_user ##
	def set_user(self, uId, l) :
		self.users[uId]['gender'] = l[0]
		self.users[uId]['age'] = l[1]
		self.users[uId]['occupation'] = l[2]
		self.users[uId]['zip'] = l[3]
			
	
	## add_user ##
	def add_user(self, l, uId = 0):
		oneUser = {}
		(oneUser['gender'], oneUser['age'], oneUser['occupation'], oneUser['zip']) = l

		if uId == 0:
			self.largestUid += 1
			self.users[self.largestUid] = oneUser
			return self.largestUid
		else:
			if uId > self.largestUid:
				self.largestUid = uId
			self.users[uId] = oneMovie
			return uId

	## delete_user ##
	def delete_user(self, uId):
		del self.users[uId]

	## delete_users ##
	def delete_users(self):
		self.users.clear()

	## load_ratings ##
	def load_ratings(self, rFile):
		self.ratings.clear()
		f = open(rFile)

		for line in f:
			line = line.rstrip()
			components = line.split("::")
			uId = int(components[0])
			mId = int(components[1])
			rat = int(components[2])

			if not self.ratings.has_key(mId):
				self.ratings[mId] = {}
			self.ratings[mId][uId] = rat

		f.close()

	## get_rating ##
	def get_rating(self, mId):
		totStars = 0
		numUsers = 0
		for user in self.ratings[mId].keys():
			numUsers += 1
			totStars += self.ratings[mId][user]

		if numUsers == 0:
			return 0
		else:
			return float(totStars) / float(numUsers)

	## get_highest_rated_movie ##
	def get_highest_rated_movie(self):
		mId = 0
		bestRat = -1.0

		for key in self.ratings.keys():
			curRat = self.get_rating(key)
			if curRat > bestRat:
				mId = key
				bestRat = curRat

		return mId

	## set_user_movie_rating ##
	def set_user_movie_rating(self, uId, mId, rat):
		self.ratings[mId][uId] = rat

	## get_user_movie_rating ##
	def get_user_movie_rating(self, uId, mId):
		if self.ratings.has_key(mId):
			if self.ratings[mId].has_key(uId):
				return self.ratings[mId][uId]
			else:
				return None
		else:
			return None

	## get_highest_rated_unvoted_movie ##
	def get_highest_rated_unvoted_movie(self, uId):
		mId = 0
		bestRat = -1.0

		for key in self.ratings.keys():
			curRat = self.get_rating(key)
			if curRat > bestRat:
				if self.get_user_movie_rating(uId, key) == None:
					mId = key
					bestRat = curRat

		return mId


	## delete_all_ratings ##
	def delete_all_ratings(self):
		self.ratings.clear()


	## load_posters ##
	def load_posters(self, pFile):
		self.posters.clear()
		f = open(pFile)

		for line in f:
			line = line.rstrip()
			components = line.split("::")
			mId = int(components[0])
			self.posters[mId] = components[2]	# image file name
		f.close()

	## get_poster_by_mid ##
	def get_poster_by_mid(self, mId):
		if self.posters.has_key(mId):
			return self.posters[mId]
		return '/default.jpg'




