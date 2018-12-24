from django.shortcuts import render
from urllib.request import urlopen as uReq
import requests, json
from bs4 import BeautifulSoup as soup


def seo(request):
    if request.method=="POST":
        keyword=request.POST.get('keyword')

        r = requests.get('https://www.google.co.jp/search?hl=ja&num=10&q=' + keyword)

        res_google = requests.get(r)
        res_google.raise_for_status()
        bs4_google = soup(res_google.text, 'html.parser')
        link_google = bs4_google.select('div > h3.r > a')

        result = []
        for i in range(len(link_google)):
            #なんか変な文字が入るので除く
            site_url = link_google[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
            site_title=bs4_google.select('div > h3.r > a')[i].text#textで中身抽出。stringでもいいけど今回はnoneが返る
            if 'https://' in site_url or 'http://' in site_url:
                #サイトの内容を解析
                try:
                    result.append(i+1, site_title, site_url)
                    # print("[{}位:「{}」,URL「{}」]".format(i+1,site_title,site_url))
                except:
                    continue
                
        return render(request, 'seo/index.html', {'result':result})

    else:
            keyword='keyword'

            r = requests.get('https://www.google.co.jp/search?hl=ja&num=10&q=' + keyword)

            res_google = requests.get(r)
            res_google.raise_for_status()
            bs4_google = soup(res_google.text, 'html.parser')
            link_google = bs4_google.select('div > h3.r > a')

            result = []
            for i in range(len(link_google)):
                #なんか変な文字が入るので除く
                site_url = link_google[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
                site_title=bs4_google.select('div > h3.r > a')[i].text#textで中身抽出。stringでもいいけど今回はnoneが返る
                if 'https://' in site_url or 'http://' in site_url:
                    #サイトの内容を解析
                    try:
                        result.append(i+1, site_title, site_url)
                        # print("[{}位:「{}」,URL「{}」]".format(i+1,site_title,site_url))
                    except:
                        continue
                    
            return render(request, 'seo/index.html', {'result':result})
