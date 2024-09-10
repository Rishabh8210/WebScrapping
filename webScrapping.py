from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
    content = html_file.read()

    # Creating an instance of BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')
    # Print the content of html file in the terminal and prettify helps to beautify the content in html format
    # So it will print in html format 
    print(soup.prettify())

    # Find method helps to find the first occurence of the selected tag or given argumnet inside the find method
    pickParagraphTags = soup.find('p')
    
    # It will print the first occurence of 'p' tag 
    print(pickParagraphTags)

    # Find_all method helps to find all occurences of the selected tag or given argumnet inside the find_all method
    pickAllParagraphTags = soup.find_all('p')
    # It will print a list of selectd 'p' tag
    print(pickAllParagraphTags)

    #Use .text method to print the inner text of the selected tag
    for p in pickAllParagraphTags:
        print(p.text)

    # If you want to get data from nesting elements like this 
    # <div>
    #     <div>
    #         <div>
    #               <a></a>
    #         </div>
    #     </div>
    # </div>

    # So for that you need to pass filter object inside find methods
    productsSection = soup.find_all('div', class_="name")
    # print(productsSection)
    for productName in productsSection:
        print(f'Product name is {productName.p.text}')

