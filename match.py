import requests
from bs4 import BeautifulSoup
import csv
# open web-page
date  = input("enter date in this format MM/DD/YYYY: ")
page  = requests.get(F"https://www.yallakora.com/match-center/?date={date}#days")
def main(page):
    src = page.content
    beauty = BeautifulSoup(src , "html.parser" )
    matches_details = []
    championships = beauty.find_all("div" , {'class': 'matchCard'})
    # get matches info
    def get_match_info(championships):
        championship_title = championships.contents[1].find('h2').text.strip()
        all_matches = championships.contents[3].find_all("div" , {'class' : 'item'})
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find('div' , {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find('div' , {'class': 'teamB'}).text.strip()
            # GET score
            match_result = all_matches[i].find('div' , {'class' : 'MResult'}).find_all('span' , {'class' : 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            # get match time
            match_time =  all_matches[i].find('div' , {'class' : 'MResult'}).find('span' , {'class' : 'time'}).text.strip()
            # match statues
            match_statues = all_matches[i].find('div' , {'class' : 'matchStatus'}).text.strip() 
            # match date 
            match_date = all_matches[i].find('div' , {'class' : 'date'}).text.strip()
            # add match info to matches_details
            matches_details.append({"نوع البطولة" :championship_title, "الفريق الأول" : team_A, "الفريق الثانى" : team_B , "ميعاد المباراة": match_time , "النتيجة" : score , "حالة المباراة" : match_statues , "الجولة/الأسبوع" : match_date  } )       
    for i in range(len(championships)):      
        get_match_info(championships[i])       
    keys = matches_details[0].keys()   
    with open('kora.csv','w' , encoding="utf-8") as output_file:
        hallo=csv.DictWriter(output_file, keys)
        hallo.writeheader()
        hallo.writerows(matches_details)
        print("file created")    
main(page) 