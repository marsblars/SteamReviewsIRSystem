from review import Review
import csv
import pandas as pd
#used for multi-line review entry
import sys

class ReviewInventory():

  def __init__(self):
    self.__list_reviews = []
    self.__TFRev = []
    self.__list_game_reviews = []
    self.__wishlist = []
    self.__col_names = []
    self.__data = []

  # def search_entry(self, search):
  #   for review in self.__list_reviews:
  #     #checks if search is for appid
  #     if review.appid == search:
  #       return review
  #     if review.title.capitalize() == search.capitalize():
  #       return review
  #   print('no review matches that appid.')
  #   return None

  def search_top_review(self, search):
    #declares top rating and review match
    topRating = None
    reviewMatch = None
    #iterates through list of reviews
    for review in self.__list_reviews:
      #checks if search is for appid
      if review.appid == search:
        if topRating is None or review.reviewRating > topRating:
          topRating = review.reviewRating
          reviewMatch = review

      #checks if search is a string
      elif type(search) == str:
        #checks if search is for title
        if review.title.capitalize() == search.capitalize():
          #checks for highest review rating
          if topRating is None or review.reviewRating > topRating:
            #sets top rating to highest review rating and reviewMatch to the review at the current iteration
            topRating = review.reviewRating
            reviewMatch = review
    #returns review if it is found
    if reviewMatch is not None:
      return reviewMatch
    #if no review is found return None
    print('no review matches that appid.')
    return None

  def create_inventory(self, reviewcsv):
    #defines column names list


    with open(reviewcsv, 'r') as file_handler:
      #adds column names to the list by reading first line and seperating by commas
      self.__col_names.append(file_handler.readline().strip('\n').split(','))

    with open(reviewcsv, 'r') as csvfile:
    #defines read csv as a dictionary
      csvreader = csv.DictReader(csvfile)
      #Iterates through columns 
      for col in csvreader:
        #Sets each review by index of column names list
        review = Review()
        review.appid = int(col[self.__col_names[0][0]])
        review.title = col[self.__col_names[0][1]]
        review.reviewDate = col[self.__col_names[0][2]]
        review.isPosReview = col[self.__col_names[0][3]]
        review.review_input = col[self.__col_names[0][4]]
        review.review_id = int(col[self.__col_names[0][5]])
        review.reviewRating = int(col[self.__col_names[0][6]])
        review.authorSteamID = int(col[self.__col_names[0][7]])
        review.authorTotReviews = int(col[self.__col_names[0][8]])
        review.authorPlaytime = col[self.__col_names[0][9]]
        #appends review to list of reviews
        self.__list_reviews.append(review)

#Takes in review attributes as parameters and sets them as new review entry
  def add_review_entry(self):
    review = Review()
    review.appid = int(input('Enter new review games appid: '))
    review.title = input('Enter new reviews games title ')                         
    review.reviewDate = input('Enter new Review Date: ')
    review.isPosReview = str(input('Is the Review Positive? (TRUE/FALSE): ').capitalize())
    print('Press ctrl + D to submit new review:\n')
    #allows for multiple line input for review
    review.review_input = sys.stdin.read()
    review.review_id = int(input('Enter new unique review ID: '))
    review.reviewRating = int(input('\nHow many votes helpful does the review have?: '))
    review.authorSteamID = int(input('Enter new review author Steam ID: '))
    review.authorTotReviews = int(input('Enter review author total review count: '))
    review.authorPlaytime = input('Enter new review author playtime at time of review ')
    self.__list_reviews.append(review)
    print('New review entry added\n')



  #remove entry by asking for the ReviewID
  def delete_review(self):

    delrev = int(input("\n Enter Review ID for deletion: "))

    for review in self.__list_reviews:
      index = self.__list_reviews.index(review)
      #if review id found, pop from list
      if review.review_id == delrev:
        self.__list_reviews.pop(index)
        print("Review ",delrev," Deleted.\n")
        return 

      #if not found, spit error msg
    print("Review ID does not match any review in list!\n")
      #deletes the entry from list


  #ask user for only pos or neg reviews
  def pos_or_neg(self, Revsearch):

    if not self.__TFRev:
      #go thorugh POS and NEG reviews and add to list
      for review in self.__list_reviews:
        if review.isPosReview.capitalize() == Revsearch.capitalize():
             self.__TFRev.append(review) 
    #return the list
      return self.__TFRev

        #if search does not match, error
    print('No review found matching appid\n')
    return None


  #save info into CSVfile
  def writeback(self, newcsv):

    review = Review()
    for review in self.__list_reviews:
    #creates new list, takes from review list
      review_data  = [review.appid, 
          review.title, 
          review.reviewDate, 
          review.isPosReview,
          review.review_input, 
          review.review_id,  
          review.reviewRating, 
          review.authorSteamID,
          review.authorTotReviews,
          review.authorPlaytime,
                     ]
      self.__data.append(review_data)
    #uses pandas lib to convert newlist into dataframe
    df = pd.DataFrame(self.__data, columns= [
      'app_id',
      'app_name', 
      'date_created',
      'recommended',
      'review_input',
      'review_id',
      'votes_helpful',
      'author.steamid',
      'author.num_reviews',
      'author.playtime_at_review'

    ])
    #Takes dataframe and creates CSV file to save modified data
    df.to_csv(newcsv, index=False) 
    print("\n CSV file Saved! \n")




  # shows reviews inputted into the data set
  def show_game_reviews(self, search):

    if not self.__list_game_reviews:
      for review in self.__list_reviews:
        if review.appid == search:
          self.__list_game_reviews.append(review)
        elif type(search) == str:
          if review.title.capitalize() == search.capitalize():
            self.__list_game_reviews.append(review)

      return self.__list_game_reviews
    print('No review matches with the appid or the title you inputted')
    return None

  #creates wishlist of specific reviews the user wants to see the reviews
  def create_wish_list(self):
    clist = []
    while True:
      user_input = input("Enter game based on their appid or title to create your wishlist, input exit if you have finished creating your wishlist: ")
      if user_input != "exit":
        clist.append(user_input)
      else:
        break

    for c in clist: 
      self.__wishlist.append(self.search_top_review(c))

  #shows wishlist of specific reviews the user wants to see the reviews
  def show_wish_list(self):
    for r in self.__wishlist:
      if r:
        print("\n appid: " + str(r.appid) + 
             "\n title" + r.title + 
             "\n reviewDate: " + r.reviewDate + 
             "\n Positive or Negative Review: " + r.isPosReview + 
             "\n Review\n: " + r.review_input +
             "\nreview_id: " + str(r.review_id) + 
             "\n People that rated this review: " + str(r.reviewRating) +
             "\n Author Steam ID: " + str(r.authorSteamID) +
             "\n Reviews done by Author: " + str(r.authorTotReviews) +
             "\n Time played by author: " + r.authorPlaytime +"\n")
    
  #returns inventory to user
  def __str__(self):
    inventory = ""
    for review in self.__list_reviews:
        inventory = inventory + str(review)
    return inventory

