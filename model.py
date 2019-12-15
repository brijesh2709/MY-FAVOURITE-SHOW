import ast
import urllib.request

all_epi = []
user_epi = []


class NotFoundError(Exception):
    pass

class Model:

    def __init__(self):
        self.List_of_epi = []
        self.select_epi = []

    def open_url(self, url):
        response = urllib.request.urlopen(url)
        inf = response.read()
        response.close()
        inf = inf.decode('utf-8')
        inf = ast.literal_eval(inf)
        return inf

    def user_search(self, search):
        self.search = str(search.replace(' ', '+'))
        try:
            url = 'http://www.omdbapi.com/?t=' + self.search
            url += '&episodes&apikey=8ae9454b'
            data = self.open_url(url)
            for i in range(1, int(data['totalSeasons']) + 1):
            
                try:
                    url = 'http://www.omdbapi.com/?t=' + self.search
                    url += '&type=series&season=' + str(i)
                    url += '&apikey=8ae9454b'
                    epi = self.open_url(url)

                    if epi['Response'] == 'True':
                        for j in epi['Episodes']:
                            k = {'Season': i, 'Episodes': j['Episode'],
                                 'Title': j['Title']}
                            all_epi.append(k)
                            self.List_of_epi.append(k)
                except:
                    pass
            return search
        except:
            raise NotFoundError()

    def storage(self):
        self.new_list = []
        for i in range(len(self.select_epi)):
            season = self.select_epi[i][8:10]
            rseason = ''
            for j in season:
                if j.isdigit():
                    rseason += j
                episode = self.select_epi[i][20:23]
                repisode=''
                for j in episode:
                    if j.isdigit():
                        repisode += j
                url1 = 'http://www.omdbapi.com/?t=' + self.search
                url1 += '&type=series&season='
                url1 += rseason + '&episode=' + repisode
                url1 += '&plot=short&apikey=8ae9454b'

                epi = self.open_url(url1)

                if epi['Response'] == 'True':
                    statement = 'Title: ' + epi['Title'] + ', Season:'
                    statement += epi['Season']
                    statement += ', Episode: ' + epi['Episode'] + ', Plot: '
                    statement += epi['Plot'] + '\n'
                    self.new_list.append(statement)
            return self.new_list

    def save_file(self, path1):
        try:
            f = open(path1, 'w')
            for i in self.new_list:
                f.write(i)
            f.close()
            return 1
        except:
            return 0
