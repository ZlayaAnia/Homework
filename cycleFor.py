school = [
    {'class' : '1a', 'score' : [4,5,3,3,4,5]},
    {'class' : '2b', 'score' : [5,2,3,4,5,3,5,3]},
    {'class' : '3c', 'score' : [3,3,4,5,5,4,5,2]},
    {'class' : '4d', 'score' : [5,5,4,4,4]}]
   
i = 0
ave_all = []
for score in school:
    ave = sum(school[i]['score'])/len(school[i]['score'])
    print('Среднее в классе ',school[i]['class'],': ', ave)
    i +=1  
    ave_all.append(ave)
      
print(ave_all)
print('Среднее по школе - ',sum(ave_all)/len(ave_all))