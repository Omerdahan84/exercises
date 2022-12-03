from typing import *
import argparse
import bs4
import requests
import urllib.parse
import sys
import pickle
# TODO maybe to check the arguments.

# help functions


def fix_line(line):
    """this function gets a line and remove \n from the end"""
    if line[len(line)-1:] == '\n':
        return line[:len(line)-1]
    else:
        return line


def creating_pickel(out_file, dict):
    """ creates a picke file with the traffic dict"""
    with open(out_file, 'wb') as f:
        pickle.dump(dict, f)


def open_pickle(dict_file):
    """open a pickle file and return a dictionary"""
    with open(dict_file, 'rb') as f:  # open the dict file and assing its value to traffic dict
        new_dict = pickle.load(f)
    return new_dict
# Section A find the links between the pages


def traffic_dict_builder(index_file, base_url):
    """this function build the traffic dictionart"""
    traffic_dict = dict()
    # open the file and go over the file
    with open(index_file) as index_file_read:
        # each line is a name page
        for line in index_file_read:
            # slicing the originial argument to remove \n in the end
            page_name = fix_line(line)

            traffic_dict[page_name] = get_relationship(
                page_name, index_file, base_url)  # set the value under the key page name to a dictionary. in that dictionary every key is a linked page and the value is the number of appearance of the linked page in page name
    return traffic_dict


def get_relationship(page_name, index_file, base_url):
    """get two pages and return the number of links in page name to linked page"""
    linked_dict = dict()
    # opneing the index file and for each index count how many times this link appear in page name
    with open(index_file) as index_file_read:
        """count the number of times linked page link appear in
        page name"""
        count = 0
        # creating the full url of page name
        full_url = urllib.parse.urljoin(base_url, page_name)
        page_name_response = requests.get(full_url)  # getting the url page
        html = page_name_response.text  # getting the htmk text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for line in index_file_read:
            # slicing the originial argument to remove \n in the end
            linked_page_name = fix_line(line)
            # irritating over the links in the main website
            # if the linked page appears we will update the value under the key of this linked page name
            for p in soup.find_all("p"):
                for link in p.find_all("a"):
                    if linked_page_name == link.get("href"):
                        if linked_page_name in linked_dict:
                            linked_dict[linked_page_name] += 1
                        else:
                            linked_dict[linked_page_name] = 1
    return linked_dict


def sum_links_from(page_name, traffic_dict):
    """return the sum of links to other pages in specig page"""
    sum = 0
    for linked_page in traffic_dict[page_name]:
        sum += traffic_dict[page_name][linked_page]

    return sum

# Section B page rank dictionary


def page_rank_builder(iterations, traffic_dict):
    """building the dictionary of ranks"""
    r = dict()
    # building the dictionary r
    for page_name in traffic_dict:
        r[page_name] = 1
    # irritating over the number of iterations inserted
    for i in range(iterations):
        # building the dictionary new_r
        new_r = dict()
        for page_name in traffic_dict:
            new_r[page_name] = 0

        # going over the links in traffic_dict
        for page_name in traffic_dict:
            # going over the links in traffic_dict
            for linked_page in traffic_dict:
                # checks if there is a connection between two pages
                if linked_page in traffic_dict[page_name].keys():
                    # updating new r in the linked page key according to the formula
                    new_r[linked_page] += r[page_name] * \
                        (traffic_dict[page_name][linked_page] /
                         sum_links_from(page_name, traffic_dict))

        # updating r

        r = new_r

    return r

# Section C word dictionary


def word_dictionary_builder(base_url, index_file):
    word_dict = dict()
    # open the file and go over the file
    with open(index_file) as index_file_read:
        # each line is a name page
        for line in index_file_read:
            # slicing the originial argument to remove \n in the end
            page_name = fix_line(line)
            # combine the name page with the base url to create the full adress
            full_url = urllib.parse.urljoin(base_url, page_name)
            page_name_response = requests.get(full_url)  # getting the url page
            html = page_name_response.text  # getting the html text
            soup = bs4.BeautifulSoup(html, 'html.parser')
            for p in soup.find_all("p"):  # irritating over the paragraphs
                content = p.text.split()  # 'cleaning' the paragraph content and put in a list
                for word in content:
                    # for each word
                    if word not in word_dict:
                        # if the word is not the the word dictionary add the word and the make the current page count equal to one
                        word_dict[word] = {page_name: 1}
                    else:
                        # if the word exist in the dict but not in this page before
                        if page_name not in word_dict[word]:
                            word_dict[word][page_name] = 1
                        else:
                            # if the current word already appeard in this page- update the count
                            word_dict[word][page_name] += 1
    return word_dict

# Section D query


def sort_dict(rank_dict):
    """return a dict sotted from the biggest value to the smallest value"""
    return {k: v for k, v in sorted(rank_dict.items(), key=lambda item: item[1], reverse=True)}


def max_ranks(query_words, rank_dict, word_dict, max_results):
    """this function return the max result number of pages which word in the qeurt appears in them"""
    lst_max_ranks = []
    sorted_rank_dict = sort_dict(rank_dict)  # sort the rank page
    # for each word if this word is in a page we append to the list the page name
    iterations = max_results
    for page in sorted_rank_dict:
        if iterations == 0:
            break
        for word in query_words:
            if page in lst_max_ranks:
                continue
            if word not in word_dict:
                break
        # for each word added the max result number of pages that the word appears in the and have the highest rank
            if page not in word_dict[word]:
                break
            lst_max_ranks.append(page)
            iterations -= 1
    return lst_max_ranks


def min_appearance(query_words, page, word_dict):
    """return the min appearance for a word in the query"""
    # sest the minumin value for refernce
    for i in range(len(query_words)):
        # checks if the word appears in the dict
        if query_words[i] in word_dict:
            # checks if the page is in the word dict
            if page in word_dict[query_words[i]]:
                min = word_dict[query_words[i]][page]
    # calc the min value if serval words in the query
    for word in query_words:
        if word not in word_dict:
            continue
        if page not in word_dict[word]:
            continue
        if word_dict[word][page] < min:
            min = word_dict[word][page]
    return min


def pages_values(lst_max_rank, query_words, word_dict, rank_dict):
    """create a dict with the pages and their values calculates according to the formula and print the values and names from high to low"""
    values_dict = dict()
    for page in lst_max_rank:
        z = min_appearance(query_words, page, word_dict)
        y = rank_dict[page]
        values_dict[page] = z*y

    sorted_value_dict = sort_dict(values_dict)
    # printing results
    for page in sorted_value_dict:
        print(f'{page} {sorted_value_dict[page]}')


def result(query_words, rank_dict, word_dict, max_results):
    lst_max_rank = max_ranks(query_words, rank_dict, word_dict, max_results)
    pages_values(lst_max_rank, query_words, word_dict, rank_dict)


# main
if __name__ == '__main__':
    command_name = sys.argv[1]  # getting the command name from user arguments

    if command_name == 'page_rank':
        iterations = sys.argv[2]  # taking number of iterations from arguments
        dict_file = sys.argv[3]  # the dict file adress
        out_file = sys.argv[4]  # the out file of the dictionary we will create
        traffic_dict = open_pickle(dict_file)
        creating_pickel(out_file, page_rank_builder(
            int(iterations), traffic_dict))
    if command_name == 'crawl':
        """this section running the command crawl"""
        base_url = sys.argv[2]  # taking the base url from user argumrnt
        index_file = sys.argv[3]  # taking the index file from user argumrnt
        out_file = sys.argv[4]  # the file choose to save the dictinary
        # bulfing the traffic dictionary
        creating_pickel(out_file, traffic_dict_builder(
            index_file, base_url))  # save the dictionary
    if command_name == 'words_dict':
        base_url = sys.argv[2]  # the base url
        index_file = sys.argv[3]  # assing the index file
        out_file = sys.argv[4]  # assing the name of the outfile
        word_dict = word_dictionary_builder(base_url, index_file)
        creating_pickel(out_file, word_dictionary_builder(
            base_url, index_file))  # save_dictionary

    if command_name == 'search':
        # Set the query parameter
        query_words = sys.argv[2].split()
        rank_dict = open_pickle(
            sys.argv[3])  # open the rank dict file
        word_dict = open_pickle(
            sys.argv[4])  # open the word dict file
        # assing the value of max result
        max_results = sys.argv[5]
        result(query_words, rank_dict, word_dict, int(max_results))
