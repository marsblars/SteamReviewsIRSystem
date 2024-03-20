class Review: #Game class that holds information about a single steam game


  def __init__(self):
    self._appid = 0
    self._title = ''
    self._reviewDate = ''
    self._isPosReview = ''
    self._review_input = ''
    self._review_id = 0
    self._reviewRating = 0
    self._authorSteamID = 0
    self._authorTotReviews = 0
    self._authorPlaytime = ''

  @property
  def appid(self):
    return self._appid

  @appid.setter
  def appid(self, appid):
    assert appid > 0 #check if appid is greater than 0
    self._appid = appid

  @property
  def title(self):
    return self._title

  @title.setter
  def title(self, title):
    assert type(title) == str #check if reviewDate is str
    self._title = title

  @property
  def reviewDate(self):
    return self._reviewDate

  @reviewDate.setter
  def reviewDate(self, reviewDate):
    assert type(reviewDate) == str #check if reviewDate is str
    self._reviewDate = reviewDate


  @property 
  def isPosReview(self):
    return self._isPosReview 

  @isPosReview.setter
  def isPosReview(self, isPosReview):
    assert type(isPosReview) == str
    self._isPosReview = isPosReview

  @property
  def review_input(self):
    return self._review_input

  @review_input.setter
  def review_input(self, review):
    assert type(review) == str
    self._review_input = review 

  @property
  def review_id(self):
    return self._review_id

  @review_id.setter
  def review_id(self, review_id):
    assert review_id > 0
    self._review_id = review_id

  @property
  def reviewRating(self):
    return self._reviewRating

  @reviewRating.setter
  def reviewRating(self, reviewRating):
    assert reviewRating > 0
    self._reviewRating = reviewRating


# Getter for Authors Steam ID
  @property 
  def authorSteamID(self):
    return self._authorSteamID

  # Setter for Authors Steam ID
  @authorSteamID.setter
  def authorSteamID(self, authorSteamID):
    assert authorSteamID > 0
    self._authorSteamID = authorSteamID

  # Getter for Authors Total Reviews
  @property  
  def authorTotReviews(self):
    return self._authorTotReviews

  # Setter for Authors Total Reviews
  @authorTotReviews.setter
  def authorTotReviews(self, authorTotReviews):
    assert authorTotReviews > 0
    self._authorTotReviews = authorTotReviews

  # Getter for Authors Play Time
  @property
  def authorPlaytime(self):
    return self._authorPlaytime

  # Setter for Authors Play Time
  @authorPlaytime.setter
  def authorPlaytime(self, authorPlaytime):
    assert type(authorPlaytime) == str
    self._authorPlaytime = authorPlaytime

  def __str__(self):
    return('appid: ' + str(self.appid) + '\ntitle: ' + self.title + '\nreviewDate: ' + self.reviewDate + '\nisPositiveReview: ' + self.isPosReview + '\nreview:\n ' + self.review_input + '\nreviewRating: ' + str(self.reviewRating) + '\nauthorSteamID: ' + str(self.authorSteamID) + '\nauthorTotalReviews: ' + str(self.authorTotReviews) + '\nauthorPlaytime: ' + self.authorPlaytime)

