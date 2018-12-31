import facebook as fb
import requests

token = ""
graph = fb.GraphAPI(token)
Comments_count = 26
Page_Id = "2699762063582899"

likes = 0
pages = 0
comments = 0
comment_list = []
flag = False
com = graph.get_connections(Page_Id, 'feed')
print(comments)

while True:
    try:
        for comment in com['data']:
            ist_comment = []
            try:
                message = comment['message']
            except KeyError:
                continue
            likes = 0
            print(message)
            while True:
                try:
                    for like in comment['likes']['data']:
                        likes += 1
                    comment['likes'] = requests.get(comment['likes']['paging']['next']).json()
                except KeyError:
                    break
            print(likes)
            ist_comment.append(message)
            ist_comment.append(likes)
            comment_list.append(ist_comment)
            comments += 1
            print("")
            if comments >= Comments_count:
                flag = True
                break
        if flag:
            break
        com = requests.get(com['paging']['next']).json()
    except KeyError:
        break


    def to_csv(list_c):
        chain = ""
        for line in list_c:
            count = 0
            for stats in line:
                if count != 0:
                    chain += "," + str(stats)
                else:
                    chain += str(stats.replace(",", "").replace("\n", ""))
                    count += 1
            chain += "\r"
        csv = open("comments.csv", "w+")
        csv.write(chain)
        csv.close()


to_csv(comment_list)
print("")
print("Paginas analizadas: " + str(pages))
