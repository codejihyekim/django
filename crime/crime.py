from context.domains import Reader, File
import folium

class Solution(Reader):

    def __init__(self):
        self.file = File()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/'