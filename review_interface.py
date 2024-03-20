from review import Review
from review_inventory import *


class Interface:
  @staticmethod
  def review_inventory_cl():
    print("***********************************************************")
    print("*   Welcome to the review inventory system   *")
    print("***********************************************************")
    print("[0] - Exit program")
    print("[1] - Input files")
    print("[2] - Search Top Review by Review Search")
    print("[3] - Add Game Review")
    print("[4] - Delete Game Review")
    print("[5] - Show Only Positive or Negative Game Reviews")
    print("[6] - Show All Game Reviews by Review")
    print("[7] - Create or Edit Review Wishlist")
    print("[8] - Show Review Wishlist")
    print("[9] - Save to CSV File")



    rInventory = ReviewInventory()


    option = 1
    while(option != 0):
        option = int(input("Option: "))

        # enter the path to the files to build the system
        if option == 1:
            file_name = input("Enter the name of the Inventory File: ")
            rInventory.create_inventory(file_name)

            # enter the input query and search through the system to find the query
        elif option == 2:
          #asks for search and checks if search was appid or title search
          search = input("Enter the review search: ")
          if search.isdigit():
            review = rInventory.search_top_review(int(search))
          else:
            review = rInventory.search_top_review(search)
            
          if review is None:
            print("Review not found")
          else:
            #prints returned review value
            print('appid: ' + str(review.appid) + '\ntitle: ' + review.title + '\nreviewDate: ' + review.reviewDate + '\nisPositiveReview: ' + review.isPosReview + '\nreview:\n ' + review.review_input + '\nreview_id: ' + str(review.review_id) + '\nreviewRating: ' + str(review.reviewRating) + '\nauthorSteamID: ' + str(review.authorSteamID) + '\nauthorTotalReviews: ' + str(review.authorTotReviews) + '\nauthorPlaytime: ' + review.authorPlaytime) 
            
      #add review entry
        elif option == 3:
  
          rInventory.add_review_entry()


        #deletes entry from list    
        elif option == 4:
          rInventory.delete_review()

        #outputs all pos or negative reviews
        elif option == 5:
            
              TFsearch = input("\n Which kind of reviews do you want to see?  Enter True for Postive or False for Negative: ")
              if TFsearch.isalpha():
                review = rInventory.pos_or_neg(TFsearch)
                if review: 
                  for r in review:
                    print("\n appid: " + str(r.appid) + 
                          "\n title" + r.title + 
                          "\n reviewDate: " + r.reviewDate + 
                          "\n Positive or Negative Review: " +                                       r.isPosReview + 
                          "\n Review: \n" + r.review_input +
                          "\nreview_id: " + str(r.review_id) + 
                          "\n People that rated this review: " +                                      str(r.reviewRating) +
                          "\n Author Steam ID: " + str(r.authorSteamID) +
                          "\n Reviews done by Author: " +                                             str(r.authorTotReviews) +
                          "\n Time played by author: " + r.authorPlaytime                             +"\n")
  
              else:
                print("invalid input. ")
        #writes CSV file to save modified data
        elif option == 9: 
          
          newcsv = input("\n Enter CSV file to save: ")
          
          rInventory.writeback(newcsv)

      #tests for searching for reviews based on their appid or title
        elif option == 6: 
          ReviewSearch = input('Enter the reviews appid or name of the review: ')
          if ReviewSearch.isdigit():
            review = rInventory.show_game_reviews(int(ReviewSearch))
            if review: 
              for r in review:
                  print('appid: ' + str(r.appid) + '\ntitle: ' + r.title + '\nreviewDate: ' + r.reviewDate + '\nisPositiveReview: ' + r.isPosReview + '\nreview:\n ' + r.review_input + '\nreview_id: ' + str(r.review_id) +  '\nreviewRating: ' + str(r.reviewRating) + '\nauthorSteamID: ' + str(r.authorSteamID) + '\nauthorTotalReviews: ' + str(r.authorTotReviews) + '\nauthorPlaytime: ' + r.authorPlaytime)

          else: 
            review = rInventory.show_game_reviews(ReviewSearch)
            if review: 
              for r in review:
                print('appid: ' + str(r.appid) + '\ntitle: ' + r.title + '\nreviewDate: ' + r.reviewDate + '\nisPositiveReview: ' + r.isPosReview + '\nreview:\n ' + r.review_input + '\nreview_id: ' + str(r.review_id) +  '\nreviewRating: ' + str(r.reviewRating) + '\nauthorSteamID: ' + str(r.authorSteamID) + '\nauthorTotalReviews: ' + str(r.authorTotReviews) + '\nauthorPlaytime: ' + r.authorPlaytime)

        # creats a list of specific games the user wants to see the reviews on
        elif option == 7:
            
          rInventory.create_wish_list()
          
        # shows the list the games the user wants to see the reviews on
        elif option == 8:

          rInventory.show_wish_list()

        #exit the code
        elif option != 0:
            print("Invalid option")


if __name__ == "__main__":
  Interface.review_inventory_cl()