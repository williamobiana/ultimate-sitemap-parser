# Find and Parse Sitemaps to Create List of all website's pages

# prerequisites
# pip install ultimate-sitemap-parser
from usp.tree import sitemap_tree_for_homepage

filename = 'report.txt'

def getPagesFromSitemap(fullDomain):
    #listPagesRaw = []
    tree = sitemap_tree_for_homepage(fullDomain)
    with open(filename, 'w') as file:
        for page in tree.all_pages():
            #listPagesRaw.append(page.url)
            file.write(page.url +"\n")


# Go through List Pages Raw output a list of unique pages links
def getListUniquePages(filename):
    listPages = []
    for page in filename:
        if page in listPages:
            pass
        else:
            listPages.append(page)
    print(listPages)