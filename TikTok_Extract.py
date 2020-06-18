'''
Minimalist approach to extract TikTok video data from HARS
Jarrett Dev.
Working as of 6/18/2020

To use:
Open the network tab in your browser dev tools and navigate to tiktok.com/trending
Filter by 'api/item_list'
The list should be populated with GET requests.
Save all as HAR.
Run script.

'''
import json
import csv

tik_csv = open('tiktoks.csv','w')
tik_csv.write('author,desc,plays,likes,shares,comments,link,song\n') 
tik_csv.close()

tik_csv = open('tiktoks.csv','a',encoding='utf-8',newline='') #append data

out_json = json.loads(open('Tik.har','r',encoding='utf-8').read()) #replace 'Tik.har' with directory to har.
in_json = [json.loads(out_json['log']['entries'][entry]['response']['content']['text']) for entry in range(0,len(out_json['log']['entries']))] 
[[csv.DictWriter(tik_csv,['author','desc','plays','likes','shares','comments','link', 'song']).writerow({'author':str(inner_json['items'][vid]['author']['nickname']),'desc' : str(inner_json['items'][vid]['desc']), 'plays': str(inner_json['items'][vid]['stats']['playCount']),'likes': str(inner_json['items'][vid]['stats']['diggCount']), 'shares': str(inner_json['items'][vid]['stats']['shareCount']), 'comments': str(inner_json['items'][vid]['stats']['commentCount']), 'link' : str(inner_json['items'][vid]['video']['downloadAddr']), 'song' : str(inner_json['items'][vid]['music']['title'])}) for vid in range(0,len(inner_json['items']))]for inner_json in in_json]
open('Tik.har','r',encoding='utf-8').close
tik_csv.close()