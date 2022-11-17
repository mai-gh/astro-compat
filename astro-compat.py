#!/usr/bin/env python3

import sys

signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
symbols = ["♈︎", "♉︎", "♊︎", "♋︎", "♌︎", "♍︎", "♎︎", "♏︎", "♐︎", "♑︎", "♒︎", "♓︎"]
dates = ["Mar 21 - Apr 19", "Apr 20 - May 20", "May 21 - Jun 20", "Jun 21 - Jul 22", "Jul 23 - Aug 22", "Aug 23 - Sep 22", "Sep 23 - Oct 22", "Oct 23 - Nov 21", "Nov 22 - Dec 21", "Dec 22 - Jan 19", "Jan 20 - Feb 18", "Feb 19 - Mar 20"]
elements = ["fire", "earth", "air", "water", "fire", "earth", "air", "water", "fire", "earth", "air", "water"]

def read_html_file(first_sign, second_sign):

    html_file = "./pages/" + first_sign + "-" + second_sign + ".html"

    fh = open(html_file, 'r') 
    html = fh.read() 
    fh.close() 

    tmp_dict = {}

    tmp_dict['first_sign'] = first_sign
    tmp_dict['second_sign'] = second_sign

    def get_dec(html, key_phrase):
        dec = html.split(key_phrase)[1]
        dec = dec.split('<div class="skills div inpage">')[0]
        dec = dec.split('<div class="vidider"></div>\n')[1]
        dec = dec.replace('<p>', '')
        dec = dec.replace('</p>\n', '\n\n')
        return dec

    def get_per(html, key_phrase):
        per =  html.split(key_phrase)[1]
        per = per.split('<div id')[0]
        per = per.split('percentual">')[1]
        per = per.split('<')[0]
        return per


    key_phrase = 'Sexual & Intimacy Compatibility</h2>' 
    tmp_dict['sicd'] = get_dec(html, key_phrase)
    tmp_dict['sicp'] = get_per(html, key_phrase)

    key_phrase = 'Trust</h2>'
    tmp_dict['td'] = get_dec(html, key_phrase)
    tmp_dict['tp'] = get_per(html, key_phrase)

    key_phrase = 'Communication and intellect</h2>'
    tmp_dict['cid'] = get_dec(html, key_phrase)
    tmp_dict['cip'] = get_per(html, key_phrase)

    key_phrase = 'Emotions</h2>'
    tmp_dict['ed'] = get_dec(html, key_phrase)
    tmp_dict['ep'] = get_per(html, key_phrase)

    key_phrase = 'Values</h2>'
    tmp_dict['vd'] = get_dec(html, key_phrase)
    tmp_dict['vp'] = get_per(html, key_phrase)

    key_phrase = 'Shared Activities</h2>'
    tmp_dict['sad'] = get_dec(html, key_phrase)
    tmp_dict['sap'] = get_per(html, key_phrase)

    key_phrase = 'Summary</h2>'
    tmp_dict['sd'] = get_dec(html, key_phrase)
    tmp_dict['sp'] = get_per(html, key_phrase)

    return tmp_dict    

# generate db
compat_dict = {}
for i in signs:
    compat_dict[i] = {}
    for j in signs:
        compat_dict[i][j] = read_html_file(i, j)


chart_title = """
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#print("\n\n    BASE SIGN = {}".format(my_sign))
print(chart_title)

for h in signs:
    a = 0
    my_sign = h
    for i in signs:
            d = compat_dict[my_sign][i]
            #print("{}\t    {}\t{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(dates[a], elements[a].ljust(5), i.ljust(12), d['sicp'], d['tp'], d['cip'], d['ep'], d['vp'], d['sap'], d['sp']))
    
            line = dates[a]
            line += "\t    "
            line += elements[a].ljust(5)
            line += "\t"
            line += i.ljust(12)
            line += "\t"
            line += d['sicp']
            line += "\t\t"
            line += d['tp']
            line += "\t\t"
            line += d['cip']
            line += "\t\t"
            line += d['ep']
            line += "\t\t"
            line += d['vp']
            line += "\t\t"
            line += d['sap']
            line += "\t\t"
            line += d['sp']
            line += "\t\t"
            line += my_sign

            print(line)
#            print("{}\t    {}\t{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(dates[a], elements[a].ljust(5), i.ljust(12), d['sicp'], d['tp'], d['cip'], d['ep'], d['vp'], d['sap'], d['sp'], my_sign))
            #print("{}\t{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(elements[a].ljust(5), i.ljust(12), d['sicp'], d['tp'], d['cip'], d['ep'], d['vp'], d['sap'], d['sp']))
            a += 1



print("\r")
