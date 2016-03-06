__author__ = 'zhengxiaoyu'
import urllib
import re
def get_html(url):
    '''
    return the html code of the url
    '''
    #print  "".join(str(urllib.urlopen(url).read()).split())
    try:
        return "".join(str(urllib.urlopen(url).read()).split())
    except IOError:
        print "Network Error"
        exit()
def get_syn(word):
    '''
    return the list of synonyms
    >>> get_syn("no")
    ['none', 'nary', 'zero', 'no_more', 'negative', 'ordinal', 'number_1', 'ordinal_number', 'number', 'number_one', 'first', 'element', 'atomic_number_102', 'chemical_element', 'nobelium', 'successful', 'direct', 'end', 'goal']
    '''
    re_synonyms_str = '''<ulclass="synonyms">(.*?)</ul>'''
    re_str = '''<ahref="/synonyms/(.*?)">'''
    html_code = get_html("http://www.synonym.com/synonyms/"+word)
    if html_code.find("Wecouldn'tfindanyexactmatches") > 0:
        print "Wrong word"
        return []
    else:
        synonyms_str = re.compile(re_synonyms_str).findall(get_html("http://www.synonym.com/synonyms/"+word))
        word_list = []
        for i in synonyms_str:
            word_list += re.compile(re_str).findall(i)
        return word_list

def print_syn(syn_list, word):
    '''
    print the synonyms
    >>> print_syn(['a'],'1')
    The synonyms:
    a
    '''
    if len(syn_list) == 0:
        print "There are no synonyms for word:", word
    else:
        print "The synonyms:"
        for i in syn_list:
            print i
import sys
if __name__ == '__main__':
    print "Welcomne, tpye a word to see its synonyms, (q) to exit:"
    while(True):
        word = raw_input("Input a Word:")
        if word == 'q':
            exit()
        if type(word) == str:
            print_syn(get_syn(word), word)
        else:
            print "You should input a word"